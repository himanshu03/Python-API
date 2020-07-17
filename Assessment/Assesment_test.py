import json
import pytest
import requests
import yaml
from numpy.random.mtrand import randint

import conftest

with open("Assessment/assessment_common.yml", "r") as common:
	test_data = yaml.load(common)

with open("Assessment/assessment_project.yml", "r") as project:
	project_data = yaml.load(project)

with open('Assessment/assessment_expected.json') as json_file:
	expected_json = json.load(json_file)

@pytest.mark.sanity
def _test_Export_Assessment(Authorization, Base_Url,set_cookie):
	tc_desc = "Verify the Export functionality for the assessment which will include responses and risk/score"
	tc_status = "FAIL"
	tc_name = "Assessment_TC01"
	tc_priority = "High"

	try:
		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_01"]
		payload = {}
		headers = {
			'Authorization': Authorization,
			'Content-Type': 'application/json',
			'Cookie': set_cookie
		}
		response = requests.request("GET", url, headers=headers, data=payload)
		assert response.status_code == 200
		tc_status = "PASS"
	except Exception as e:
		tc_status = "FAIL"
		print(test_data['test_01']['message'])
		raise
	finally:
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)

@pytest.mark.sanity
def _test_Assessment_Date(Authorization, Base_Url,set_cookie):
	tc_desc = "Verify the Completed date of the available Completed Assessment"
	tc_status = "FAIL"
	tc_name = "Assessment_TC02"
	tc_priority = "High"

	try:
		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_01"]
		payload = {}
		headers = {
			'Authorization': Authorization,
			'Content-Type': 'application/json',
			'Cookie': set_cookie
		}
		response = requests.request("GET", url, headers=headers, data=payload)
		assert response.status_code == 200
		assert str(response.json()['completedOn']).__contains__(project_data[conftest.cmd_arg]["test_02"]['completedOn'])
		tc_status = "PASS"
	except Exception as e:
		tc_status = "FAIL"
		print(test_data['test_02']['message'])
		raise
	finally:
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)


@pytest.mark.sanity
def _test_Search_Assessment(Authorization, Base_Url,set_cookie):
	tc_desc = "Search a assessment with invalid text"
	tc_status = "FAIL"
	tc_name = "Assessment_TC03"
	tc_priority = "High"

	try:
		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_03"]["uri"]
		payload = project_data[conftest.cmd_arg]["test_03"]["payload"]
		headers = {
			'Authorization': Authorization,
			'Content-Type': 'application/json',
			'Cookie': set_cookie
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		assert response.status_code == 200
		assert str(response.json()['metadata']['count']) == test_data["test_03"]["count"]

		tc_status = "PASS"
	except Exception as e:
		tc_status = "FAIL"
		print(test_data['test_03']['message'])
		raise
	finally:
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)


