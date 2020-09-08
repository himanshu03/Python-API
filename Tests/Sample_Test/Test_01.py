import json
import pytest
import requests
import yaml
from numpy.random.mtrand import randint

import conftest

with open("/Users/it000621/PycharmProjects/incareapisautomation/Ymls/assessment_common.yml", "r") as common:
    test_data = yaml.load(common)

with open("/Users/it000621/PycharmProjects/incareapisautomation/Ymls/assessment_project.yml", "r") as project:
    project_data = yaml.load(project)


@pytest.mark.sanity
def test_Worklist_08(Authorization, Base_Url, set_cookie):
    tc_desc = "Submit assessment without any response"
    tc_status = "FAIL"
    tc_name = "Worklist_TC08"
    tc_priority = "High"

    try:
        url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_08"]["uri"]
        print(url)
        payload = project_data[conftest.cmd_arg]["test_08"]["payload"]
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

        url_1 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_08"]["uri1"] +ids1[0]+"/_submit"
        print(url_1)
        payload_1 = project_data[conftest.cmd_arg]["test_08"]["payload1"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_1 = requests.request("POST", url_1, headers=headers, data=payload_1)
        assert response.status_code == 200
        assert response_1.status_code == 200
        
        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_08']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)



