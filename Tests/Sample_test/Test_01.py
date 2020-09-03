import json
import pytest
import requests
import yaml
from numpy.random.mtrand import randint
import jsonpath

import conftest

empi_data = ['P026/notes']

with open("/Users/it000621/PycharmProjects/incareapisautomation/Ymls/worklist_common.yml", "r") as common:
    test_data = yaml.load(common)

with open("/Users/it000621/PycharmProjects/incareapisautomation/Ymls/worklist_project.yml", "r") as project:
    project_data = yaml.load(project)


def test_Worklist_02(Authorization, Base_Url, set_cookie):
    tc_desc = "To verify the available scheduled task for current date"
    tc_status = "FAIL"
    tc_name = "Worklist_TC02"
    tc_priority = "High"

    try:
        url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_02"]["uri"]
        print(url)
        payload = project_data[conftest.cmd_arg]["test_02"]["payload"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        json_data = response.json()
        ids = []
        for data in json_data["data"]:
            output = (data['empi'])
            ids.append(output)
        print(ids)
        assert response.status_code == 200
        assert ids[1] == project_data[conftest.cmd_arg]["test_02"]["empi"]
        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_02']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)
