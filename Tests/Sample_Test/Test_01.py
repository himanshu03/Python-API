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
def test_Worklist_10(Authorization, Base_Url, set_cookie):
    tc_desc = "Submit assessment with invalid text"
    tc_status = "FAIL"
    tc_name = "Worklist_TC10"
    tc_priority = "High"

    try:
        url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_10"]["uri"]
        print(url)
        payload = project_data[conftest.cmd_arg]["test_10"]["payload"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        json_data = response.json()
        ids = []
        ids1 = []
        for data in json_data["data"]:
            output = (data['assessmentId'])
            output1 = (data['assignmentId'])
            ids.append(output)
            ids1.append(output1)
        print("Assessment ids are:", ids)
        print("Assignment ids are", ids1)
        print("Length of assessment id are", len(ids))
        print("Length of assignment id are", len(ids1))

        url_1 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_10"]["uri1"] +ids[0]+"/_fetch"
        print(url_1)
        payload_1 = {}
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_1 = requests.request("GET", url_1, headers=headers, data=payload_1)

        json_data1 = response_1.json()
        completed = []
        for data in json_data1["completed"]:
            output = (data['assignmentId'])
            completed.append(output)
        print("assignment ids are:", completed)
        print("Length of completed assignment id are", len(completed))

        ongoing = []
        for data in json_data1["ongoing"]:
            output = (data['assignmentId'])
            ongoing.append(output)
        print("assignment ids are:", ongoing)
        print("Length of ongoing assignment id are", len(ongoing))

        url_2 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_10"]["uri1"] + completed[
            0] + "/response"
        print(url_2)
        payload_2 = {}
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_2 = requests.request("GET", url_2, headers=headers, data=payload_2)
        print(response_2.json)

        url_3 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_10"]["uri2"]
        print(url_3)
        payload_3 = project_data[conftest.cmd_arg]["test_10"]["payload1"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_3 = requests.request("POST", url_3, headers=headers, data=payload_3)
        print(response_3.json())
        print(response_3.status_code)

        json_data3 = response_3.json()
        assignment3 = json_data3['assignmentId']

        url_4 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_10"]["uri1"] +assignment3 + \
                "/_submit"
        print(url_4)
        payload_4 = project_data[conftest.cmd_arg]["test_10"]["payload2"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_4 = requests.request("POST", url_4, headers=headers, data=payload_4)
        #print(response_4.json())
        print(response_4.status_code)

        #print(response_1.json())
        assert response.status_code == 200
        assert response_1.status_code == 200
        assert response_2.status_code == 200
        assert response_3.status_code == 200
        assert response_4.status_code == 200
        
        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_10']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)



