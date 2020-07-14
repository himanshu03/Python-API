import json
import pytest
import requests
import yaml
from numpy.random.mtrand import randint

import conftest

with open("Worklist/worklist_common.yml", "r") as common:
	test_data = yaml.load(common)

with open("Worklist/worklist_project.yml", "r") as project:
	project_data = yaml.load(project)

with open('Worklist/worklist_expected.json') as json_file:
	expected_json = json.load(json_file)

@pytest.mark.sanity
def test_InCare_Worklist_01(Authorization, Base_Url,set_cookie):
	tc_desc = "To verify that the User can see his daily progress on User's Workqueue under Todos"
	tc_status = "FAIL"
	tc_name = "Worklist_TC01"
	tc_priority = "High"

	try:
		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_01"]["uri"]
		payload = project_data[conftest.cmd_arg]["test_01"]["payload"]
		headers = {
			'Authorization': Authorization,
			'Content-Type': 'application/json',
			'Cookie': set_cookie
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		assert response.status_code == 200
		assert(response.json()['data']['allTodosCount'])>=0
		assert (response.json()['data']['pendingTodosCount'])>=0
		assert (response.json()['data']['completedTodosCount'])>=0

		tc_status = "PASS"
	except Exception as e:
		tc_status = "FAIL"
		print(test_data['test_01']['message'])
		raise
	finally:
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)

@pytest.mark.sanity
def test_InCare_Worklist_02(Authorization, Base_Url,set_cookie):
	tc_desc = "To verify the available scheduled task for current date"
	tc_status = "FAIL"
	tc_name = "Worklist_TC02"
	tc_priority = "High"

	try:
		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_02"]["uri"]
		payload = project_data[conftest.cmd_arg]["test_02"]["payload"]
		headers = {
			'Authorization': Authorization,
			'Content-Type': 'application/json',
			'Cookie': set_cookie
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		assert response.status_code == 200
		#print(response.json()['data']['empi'])
		# assert (response.json()['data']['pendingTodosCount'])>=0
		# assert (response.json()['data']['completedTodosCount'])>=0

		tc_status = "PASS"
	except Exception as e:
		tc_status = "FAIL"
		print(test_data['test_02']['message'])
		raise
	finally:
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)



# def test_InCare_Worklist_03(Authorization, Base_Url,set_cookie):
# 	tc_desc = "Submit assessment without any response"
# 	tc_status = "FAIL"
# 	tc_name = "Assessment_TC03"
# 	tc_priority = "High"
# 	print(tc_desc + " is Executing")
# 	try:
# 		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_03"]["uri"]
# 		payload = project_data[conftest.cmd_arg]["test_03"]["payload"]
# 		headers = {
# 			'Authorization': Authorization,
# 			'Content-Type': 'application/json',
# 			'Cookie': set_cookie
# 		}
# 		response = requests.request("POST", url, headers=headers, data=payload)
# 		assert response.status_code == 200
# 		#assert(response.json()['status']) == test_data['test_09']['status']
#
# 		tc_status = "PASS"
# 	except Exception as e:
# 		tc_status = "FAIL"
# 		print(e)
# 		raise
# 	finally:
# 		print(tc_desc + "Status:- " + tc_status)
# 		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)
#
#
# def test_InCare_Worklist_04(Authorization, Base_Url,set_cookie):
# 	tc_desc = "Search a assessment with invalid text"
# 	tc_status = "FAIL"
# 	tc_name = "Assessment_TC04"
# 	tc_priority = "High"
# 	print(tc_desc + " is Executing")
# 	try:
# 		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_04"]["uri"]
# 		payload = project_data[conftest.cmd_arg]["test_04"]["payload"]
# 		headers = {
# 			'Authorization': Authorization,
# 			'Content-Type': 'application/json',
# 			'Cookie': set_cookie
# 		}
# 		response = requests.request("POST", url, headers=headers, data=payload)
# 		assert response.status_code == 200
# 		assert(response.json()['metadata']['count']) == test_data["test_04"]["count"]
#
# 		tc_status = "PASS"
# 	except Exception as e:
# 		tc_status = "FAIL"
# 		print(e)
# 		raise
# 	finally:
# 		print(tc_desc + "Status:- " + tc_status)
# 		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)
#
#
