import allure
import logging
import os
from pathlib import Path

import pandas
import pytest

logger = logging.getLogger('glue-test-structure-poc')



class TestPoC:
    # resource_path = os.path.join(Path(os.getcwd()), "..", "..", "resources")
    resource_path = os.path.join(Path(os.getcwd()), "resources")

    @pytest.fixture(scope="module", autouse=True)
    def my_fixture(self):
        print('\nINITIALIZATION\n')
        # data generation
        # glue job execution
        df = pandas.read_csv(os.path.join(self.resource_path,"test_data.csv"))
        yield df
        print('\nTEAR DOWN\n')
    #     ...

    @pytest.mark.smoketest
    @pytest.mark.r5_1
    @allure.title("Custom test 1")
    def test_1(self, my_fixture):
        # alert validation
        jira_tag = "JRA-1"
        print("\n test 1")
        print(my_fixture)
        row = my_fixture[my_fixture["jira_id"] == jira_tag]
        data_dictionary = row.to_dict(orient='records')[0]
        print(data_dictionary)
    #     validation of alert

    @allure.title("Custom test 2")
    @pytest.mark.r5_1
    def test_2(self, my_fixture):
        jira_tag = "JRA-2"
        print("\n test 2")
        print(my_fixture)
        row = my_fixture[my_fixture["jira_id"] == jira_tag]
        data_dictionary = row.to_dict(orient='records')[0]
        print(data_dictionary)
        raise Exception

    @allure.title("Custom test 3")
    def test_3(self, my_fixture):
        jira_tag = "JRA-2"
        print("\n test 2")
        print(my_fixture)
        row = my_fixture[my_fixture["jira_id"] == jira_tag]
        data_dictionary = row.to_dict(orient='records')[0]
        print(data_dictionary)
        raise Exception

    @allure.title("Custom test 4")
    def test_4(self, my_fixture):
        jira_tag = "JRA-2"
        print("\n test 2")
        print(my_fixture)
        row = my_fixture[my_fixture["jira_id"] == jira_tag]
        data_dictionary = row.to_dict(orient='records')[0]
        print(data_dictionary)

    # @pytest.mark.skip
    @allure.title("Custom test 5")
    def test_5(self, my_fixture):
        jira_tag = "JRA-2"
        print("\n test 2")
        print(my_fixture)
        row = my_fixture[my_fixture["jira_id"] == jira_tag]
        data_dictionary = row.to_dict(orient='records')[0]
        print(data_dictionary)
