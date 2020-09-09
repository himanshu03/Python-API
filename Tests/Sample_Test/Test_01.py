import json
import pytest
import requests
import yaml
import pprint
from numpy.random.mtrand import randint

import conftest

with open("/Users/it000621/PycharmProjects/incareapisautomation/Ymls/assessment_common.yml", "r") as common:
    test_data = yaml.load(common)

with open("/Users/it000621/PycharmProjects/incareapisautomation/Ymls/assessment_project.yml", "r") as project:
    project_data = yaml.load(project)


@pytest.mark.sanity
def test_Assessment_17(Authorization, Base_Url, set_cookie):
    tc_desc = "Submit new assessment of type PHQ-9"
    tc_status = "FAIL"
    tc_name = "Assessment_TC17"
    tc_priority = "High"

    try:
        url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_17"]["uri"]
        print(url)
        payload = project_data[conftest.cmd_arg]["test_17"]["payload"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print("Response1",response.json())
        print("Response 1",response.status_code)

        json_data = response.json()
        assignment_id = json_data['assignmentId']
        assessment_id = json_data['assessmentId']

        url_1 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_17"]["uri1"] +assignment_id \
                + "/_submit"
        print(url_1)
        payload_1 = project_data[conftest.cmd_arg]["test_17"]["payload1"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_1 = requests.request("POST", url_1, headers=headers, data=payload_1)
        print("Response 2", response_1.status_code)

        url_2 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_17"]["uri1"] + assessment_id \
                + "/_fetch"
        print(url_2)
        payload_2 = {}
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_2 = requests.request("GET", url_2, headers=headers, data=payload_2)
        print("Response 3", response_2.status_code)

        result = response_2.json()
        print("Score of a patient assessment is:",result['completed'][0]['summaryTypeList'][0]['score'])
        print("ScoreDeviation of a patient assessment is:", result['completed'][0]['summaryTypeList'][0][
            'scoreDeviation'])
        print("Total Score of a patient assessment is:", result['completed'][0]['summaryTypeList'][0]['totalScore'])
        print("Rating Display String of a patient assessment is:", result['completed'][0]['summaryTypeList'][0][
            'ratingDisplayString'])
        #################################################################################################################
        url_3 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_17"]["uri"]
        print(url_3)
        payload_3 = project_data[conftest.cmd_arg]["test_17"]["payload"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_3 = requests.request("POST", url_3, headers=headers, data=payload_3)
        print("Response4", response_3.json())
        print("Response 4", response_3.status_code)

        json_data_1 = response_3.json()
        assignment_id_1 = json_data_1['assignmentId']
        assessment_id_1 = json_data_1['assessmentId']

        url_4 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_17"]["uri1"] + \
                assignment_id_1 \
                + "/_submit"
        print(url_4)
        payload_4 = project_data[conftest.cmd_arg]["test_17"]["payload2"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_4 = requests.request("POST", url_4, headers=headers, data=payload_4)
        print("Response 4", response_4.status_code)

        url_5 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_17"]["uri1"] + \
                assessment_id_1 \
                + "/_fetch"
        print(url_5)
        payload_5 = {}
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_5 = requests.request("GET", url_5, headers=headers, data=payload_5)
        print("Response 5", response_5.status_code)

        result1 = response_5.json()
        print("Score of a patient assessment is:", result1['completed'][0]['summaryTypeList'][0]['score'])
        print("ScoreDeviation of a patient assessment is:", result1['completed'][0]['summaryTypeList'][0][
            'scoreDeviation'])
        print("Total Score of a patient assessment is:", result1['completed'][0]['summaryTypeList'][0]['totalScore'])
        print("Rating Display String of a patient assessment is:", result1['completed'][0]['summaryTypeList'][0][
            'ratingDisplayString'])

        assert response.status_code == 200
        assert response_1.status_code == 200
        assert response_2.status_code == 200
        assert response_3.status_code == 200
        assert response_4.status_code == 200
        assert response_5.status_code == 200

        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_17']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)

