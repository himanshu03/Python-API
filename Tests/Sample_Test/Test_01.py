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
def test_Assessment_16(Authorization, Base_Url, set_cookie):
    tc_desc = "Switch the assessment"
    tc_status = "FAIL"
    tc_name = "Assessment_TC16"
    tc_priority = "High"

    try:
        url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_16"]["uri"]
        print(url)
        payload = project_data[conftest.cmd_arg]["test_16"]["payload"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        json_data = response.json()
        assessment_id = []
        assignment_id = []
        for data in json_data["data"]:
            output = (data['assessmentId'])
            output1 = (data['assignmentId'])
            assessment_id.append(output)
            assignment_id.append(output1)
        print("Assessment ids are:", assessment_id)
        print("Assignment ids are", assignment_id)
        print("Length of assessment id are", len(assessment_id))
        print("Length of assignment id are", len(assignment_id))

        url_1 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_16"]["uri1"] + assessment_id[
            0] + "/_fetch"
        print(url_1)
        payload_1 = {}
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_1 = requests.request("GET", url_1, headers=headers, data=payload_1)
        print("Response 1",response_1.status_code)

        url_2 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_16"]["uri1"] + \
                assignment_id[0]+"/response"
        print(url_2)
        payload_2 = {}
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_2 = requests.request("GET", url_2, headers=headers, data=payload_2)
        print("Response 2",response_2.status_code)

        url_3 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_16"]["uri1"] + assessment_id[
            1] + "/_fetch"
        print(url_3)
        payload_3 = {}
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_3 = requests.request("GET", url_3, headers=headers, data=payload_3)
        print("Response 3", response_3.status_code)

        url_4 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_16"]["uri1"] + \
                assignment_id[1]+"/response"
        print(url_4)
        payload_4 = {}
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_4 = requests.request("GET", url_4, headers=headers, data=payload_4)
        print("Response 4",response_4.status_code)

        url_5 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_16"]["uri1"] + assessment_id[
            2] + "/_fetch"
        print(url_5)
        payload_5 = {}
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_5 = requests.request("GET", url_5, headers=headers, data=payload_5)
        print("Response 5", response_5.status_code)

        url_6 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_16"]["uri1"] + \
                assignment_id[2]+"/response"
        print(url_6)
        payload_6 = {}
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_6 = requests.request("GET", url_6, headers=headers, data=payload_6)
        print("Response 6",response_6.status_code)

        url_7 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_16"]["uri1"] + assessment_id[
            3] + "/_fetch"
        print(url_7)
        payload_7 = {}
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_7 = requests.request("GET", url_7, headers=headers, data=payload_7)
        print("Response 7", response_5.status_code)

        url_8 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_16"]["uri1"] + \
                assignment_id[3]+"/response"
        print(url_8)
        payload_8 = {}
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_8 = requests.request("GET", url_8, headers=headers, data=payload_8)
        print("Response 8",response_8.status_code)


        assert response.status_code == 200
        assert response_1.status_code == 200
        assert response_2.status_code == 200
        assert response_3.status_code == 200
        assert response_4.status_code == 200
        assert response_5.status_code == 200
        assert response_6.status_code == 200
        assert response_7.status_code == 200
        assert response_8.status_code == 200

        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_16']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)
