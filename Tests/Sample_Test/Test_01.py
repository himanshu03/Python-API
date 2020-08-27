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


def test_Worklist_25(Authorization, Base_Url,set_cookie):
	tc_desc = "Verify the sorting on Insurance"
	tc_status = "FAIL"
	tc_name = "Worklist_TC25"
	tc_priority = "Medium"

	try:
		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_25"]["uri"]
		print(url)
		payload = project_data[conftest.cmd_arg]["test_25"]["payload"]
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
		print(test_data['test_25']['message'])
		raise
	finally:
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)
