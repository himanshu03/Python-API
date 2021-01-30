import pytest
import requests
import yaml

import conftest

with open("/Users/it000621/PycharmProjects/incareapisautomation/Ymls/CreatePatient_common.yml", "r") as common:
    test_data = yaml.load(common)

with open("/Users/it000621/PycharmProjects/incareapisautomation/Ymls/CreatePatient_Project.yml", "r") as project:
    project_data = yaml.load(project)


@pytest.mark.sanity
def test_create_01(Authorization, Base_Url, set_cookie):
    tc_desc = "To create new patient"
    tc_status = "FAIL"
    tc_name = "Create_TC01"
    tc_priority = "Medium"

    try:
        url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_01"]["uri"]
        print(url)
        payload = project_data[conftest.cmd_arg]["test_01"]["payload"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        assert response.status_code == 200

        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_01']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)
