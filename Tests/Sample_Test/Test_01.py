import json
import pytest
import requests
import yaml
from numpy.random.mtrand import randint

import conftest

with open("/Users/it000621/PycharmProjects/incareapisautomation/Ymls/worklist_common.yml", "r") as common:
	test_data = yaml.load(common)

with open("/Users/it000621/PycharmProjects/incareapisautomation/Ymls/worklist_project.yml", "r") as project:
	project_data = yaml.load(project)



@pytest.mark.skip
def test_Worklist_24(Authorization, Base_Url,set_cookie):
	tc_desc = "To verify that the completed Task should be visible under Completed section"
	tc_status = "FAIL"
	tc_name = "Worklist_TC24"
	tc_priority = "Medium"

	try:
		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_24"]["uri"]
		payload = project_data[conftest.cmd_arg]["test_24"]["payload"]
		headers = {
			'Authorization': Authorization,
			'Content-Type': 'application/json',
			'Cookie': set_cookie
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		assert response.status_code == 200
		assert response.json()['data'][0]['empi'] == test_data['test_24']['empi']
		tc_status = "PASS"
	except Exception as e:
		tc_status = "FAIL"
		print(test_data['test_24']['message'])
		raise
	finally:
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)

def test_Worklist_07(Authorization, Base_Url,set_cookie):
	tc_desc = "To verify the pending task on Pending section under activity received"
	tc_status = "FAIL"
	tc_name = "Worklist_TC07"
	tc_priority = "Medium"

	try:
		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_07"]["uri"]
		print(url)
		payload = project_data[conftest.cmd_arg]["test_07"]["payload"]
		headers = {
			'Authorization': Authorization,
			'Content-Type': 'application/json',
			'Cookie': set_cookie
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		assert response.status_code == 200
		assert response.json()['metadata']['count'] >= 0
		tc_status = "PASS"
	except Exception as e:
		tc_status = "FAIL"
		print(test_data['test_07']['message'])
		raise
	finally:
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)
