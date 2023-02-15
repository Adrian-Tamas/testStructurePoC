import os

import pytest
from email_helper.email_client import EmailClient
from jinja2 import Environment, FileSystemLoader
from datetime import datetime


def pytest_sessionstart(session):
    session.results = dict()
    session.test_names = dict()
    session.test_results = []


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == 'call':
        item.session.results[result.nodeid] = result
        try:
            item.session.test_names[result.nodeid] = item._obj.__allure_display_name__
        except:
            print("test does not have an allure title")


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    print('run status code:', exitstatus)
    passed = sum(1 for result in session.results.values() if result.passed)
    failed = sum(1 for result in session.results.values() if result.failed)
    print(f'There are {passed=} and {failed=} tests')

    # Build execution summary information
    execution_summary = {
        "total_number_of_test": ("Total number of tests", len(session.results)),
        "passed_tests": ("Passed tests", passed),
        "failed_test": ("Failed tests", failed)

    }

    # Build Environment section information
    environment_information = {
        "Environment": os.getenv("test_env", default="test")
    }

    # Build test case details information
    test_results = []
    for result in session.results.values():
        test_results.append({
                "description": session.test_names.get(result.nodeid, result.nodeid),
                "run_time": round(result.duration, 2),
                "status": result.outcome
            })

    # Build parameters dict to send to the jinja template
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    parameters = {
        "title": f"Automated Test Execution Summary {now}",
        "environment_information": environment_information,
        "execution_summary": execution_summary,
        "test_results": test_results
    }
    env = Environment(loader=FileSystemLoader('resources'))
    env.get_template("email_template.html", globals=parameters).stream(name='foo').dump('report.html')


    # TODO: read the data from env.vars
    email_client = EmailClient(email_address="",
                               email_password="",
                               smtp_server="",
                               port="465") #587 for StarTTLS

    recipients = ["a@a.com", "b@b.com", "c@c.com"] # TODO: read this in from a config file

    with open("report.html", "rb") as email_html_content:
        email_client.send_email(to=recipients,
                                subject="Run summary",
                                message=email_html_content,
                                file_path="report.html",
                                attachment_name="ExecutionReport.zip")
