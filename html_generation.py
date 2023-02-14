from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('resources'))

execution_summary = {
    "total_number_of_tests": 10,
    "passed_tests": 7,
    "failed_tests": 3,
    "skipped_test": 0
}

test_results = [{
    "description": "Test 1",
    "run_time": "1.1",
    "status": "Passed"
    },
    {
        "description": "Test 2",
        "run_time": "1.3",
        "status": "Failed"
    },
    {
        "description": "Test 3",
        "run_time": "12.1",
        "status": "Passed"
    },
    {
        "description": "Test 4",
        "run_time": "4.1",
        "status": "Failed"
    },
]

parameters = {
    "test_env": "test",
    "execution_summary": execution_summary,
    "test_results": test_results
}
if __name__ == '__main__':
    env.get_template("email_template.html", globals=parameters).stream(name='foo').dump('report.html')
