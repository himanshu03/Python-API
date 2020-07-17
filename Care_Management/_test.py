import json
import pytest
import requests
import yaml
from numpy.random.mtrand import randint

import conftest

with open("Care_Management/care_management_common.yml", "r") as common:
	test_data = yaml.load(common)

with open("Care_Management/care_management_project.yml", "r") as project:
	project_data = yaml.load(project)

with open('Care_Management/care_management_expected.json') as json_file:
	expected_json = json.load(json_file)

@pytest.mark.sanity
def test_InCare_Navigation_To_Care_Management(Authorization, Base_Url,set_cookie):
	tc_desc = "To verify the navigation to Care management"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC01"
	tc_priority = "Normal"

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


def test_InCare_Care_Management_Health_Modules(Authorization, Base_Url,set_cookie):
	tc_desc = "To verify the available activities in care management_health_modules"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC02"
	tc_priority = "Normal"

	try:
		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_02"]
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
		print(test_data['test_02']['message'])
		raise
	finally:
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)

@pytest.mark.sanity
def test_InCare_Care_Management_Goals(Authorization, Base_Url,set_cookie):
	tc_desc = "To verify the available activities in care management_goals"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC03"
	tc_priority = "Normal"

	try:
		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_03"]
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
		print(test_data['test_03']['message'])
		raise
	finally:
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)

@pytest.mark.sanity
def test_InCare_Care_Management_Adhoc_Tasks(Authorization, Base_Url,set_cookie):
	tc_desc = "To verify the available activities in care management_Adhoc_Tasks"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC04"
	tc_priority = "Normal"

	try:
		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_04"]
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
		print(test_data['test_04']['message'])
		raise
	finally:
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)

@pytest.mark.sanity
def test_InCare_Care_Management_legacy_timeline(Authorization, Base_Url,set_cookie):
	tc_desc = "To verify the available activities in care management_legacy_timeline"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC05"
	tc_priority = "Normal"
	print(tc_desc + " is Executing")
	try:
		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_05"]
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
		print(test_data['test_05']['message'])
		raise
	finally:
		print(tc_desc + "Status:- " + tc_status)
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)

@pytest.mark.sanity
def test_InCare_Care_Management_Add_call_Note(Authorization, Base_Url,set_cookie):
	tc_desc = "Verify the User is able to Add call Note"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC06"
	tc_priority = "Normal"

	try:
		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_06"]
		payload = "{\n    \"type\": \"CALL\",\n    \"text\": \"API Health check for call note\"\n}"
		headers = {
			'Authorization': Authorization,
			'Content-Type': 'application/json',
			'Cookie': set_cookie
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		assert response.status_code == 200 or 201
		assert(response.json()['text']) == test_data['test_06']['text']
		assert (response.json()['noteType']) == test_data['test_06']['noteType']
		tc_status = "PASS"
	except Exception as e:
		tc_status = "FAIL"
		print(test_data['test_06']['message'])
		raise
	finally:
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)

@pytest.mark.sanity
def test_InCare_Care_Management_Visit_Adhoc_Task(Authorization, Base_Url,set_cookie):
	tc_desc = "Verify the User is able to create Visit Ad-hoc Task"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC07"
	tc_priority = "Normal"
	print(tc_desc + " is Executing")
	try:
		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_06"]
		payload = "{\n    \"type\": \"VISIT\",\n    \"text\": \"Visit Ad-hoc Task\",\n    \"visitType\": \"HRA (Health Risk Assessment)\"\n}"
		headers = {
			'Authorization': Authorization,
			'Content-Type': 'application/json',
			'Cookie': set_cookie
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		assert response.status_code == 200 or 201
		assert(response.json()['text']) == test_data['test_07']['text']
		assert (response.json()['metadata']['visitType'])== test_data['test_07']['visitType']
		assert (response.json()['noteType']) == test_data['test_07']['noteType']
		tc_status = "PASS"
	except Exception as e:
		tc_status = "FAIL"
		print(test_data['test_07']['message'])
		raise
	finally:
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)

@pytest.mark.sanity
def test_InCare_Care_Management_Note_Adhoc_Task(Authorization, Base_Url,set_cookie):
	tc_desc = "Verify the User is able to create Note Ad-hoc Task"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC08"
	tc_priority = "Normal"
	print(tc_desc + " is Executing")
	try:
		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_06"]
		payload = "{\n    \"type\": \"NOTE\",\n    \"text\": \"Ad-hoc Task \\\"API Health check for Note\\\"\"\n}"
		headers = {
			'Authorization': Authorization,
			'Content-Type': 'application/json',
			'Cookie': set_cookie
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		assert response.status_code == 200 or 201
		assert(response.json()['text']) == test_data['test_08']['text']
		assert (response.json()['noteType']) == test_data['test_08']['noteType']
		tc_status = "PASS"
	except Exception as e:
		tc_status = "FAIL"
		print(test_data['test_08']['message'])
		raise
	finally:
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)

@pytest.mark.sanity
def test_InCare_Care_Management_create_New_Task(Authorization, Base_Url,set_cookie):
	tc_desc = "Verify the User is able to create New Task"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC09"
	tc_priority = "Normal"

	try:
		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_09"]["uri"]
		payload = project_data[conftest.cmd_arg]["test_09"]["payload"]
		headers = {
			'Authorization': Authorization,
			'Content-Type': 'application/json',
			'Cookie': set_cookie
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		assert response.status_code == 200
		assert(response.json()['status']) == test_data['test_09']['status']
		assert(response.json()['data']['type']) == test_data['test_09']['type']
		assert (response.json()['data']['note']) == test_data['test_09']['note']
		assert (response.json()['data']['task']) == test_data['test_09']['task']
		tc_status = "PASS"
	except Exception as e:
		tc_status = "FAIL"
		print(test_data['test_09']['message'])
		raise
	finally:
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)

@pytest.mark.sanity
def test_InCare_Care_Management_create_Letter(Authorization, Base_Url,set_cookie):
	tc_desc = "Verify the User is able to create Letter"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC010"
	tc_priority = "Normal"

	try:
		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_06"]
		payload = "{\n    \"type\": \"LETTER_SENT\",\n    \"text\": \"API Health Check for Letter\",\n    \"sendDate\": 1592937000000\n}"
		headers = {
			'Authorization': Authorization,
			'Content-Type': 'application/json',
			'Cookie': set_cookie
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		assert response.status_code == 200 or 201
		assert(response.json()['text']) == test_data['test_10']['text']
		assert (response.json()['noteType']) == test_data['test_10']['noteType']
		tc_status = "PASS"
	except Exception as e:
		tc_status = "FAIL"
		print(test_data['test_10']['message'])
		raise
	finally:
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)

@pytest.mark.sanity
def test_InCare_Care_Management_All_Activity_Filter_Select_Care_Protocol(Authorization, Base_Url,set_cookie):
	tc_desc = "Select Care Protocol in All Activity Filter"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC11"
	tc_priority = "Normal"

	try:
		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_11"]
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
		print(test_data['test_11']['message'])
		raise
	finally:
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)


@pytest.mark.sanity
def test_InCare_Care_Management_All_Activity_Filter_Select_Care_Protocol_Unit(Authorization, Base_Url,set_cookie):
	tc_desc = "Select Care Protocol Unit in All Activity Filter"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC12"
	tc_priority = "Normal"

	try:
		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_12"]
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
		print(test_data['test_12']['message'])
		raise
	finally:
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)

@pytest.mark.sanity
def test_InCare_Care_Management_All_Activity_Filter_Select_Task(Authorization, Base_Url,set_cookie):
	tc_desc = "Select Task in All Activity Filter"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC13"
	tc_priority = "Normal"

	try:
		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_13"]
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
		print(test_data['test_13']['message'])
		raise
	finally:
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)


@pytest.mark.sanity
def test_InCare_Care_Management_All_Activity_Filter_Select_Notes(Authorization, Base_Url,set_cookie):
	tc_desc = "Select Notes in All Activity Filter"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC14"
	tc_priority = "Normal"

	try:
		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_14"]
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
		print(test_data['test_14']['message'])
		raise
	finally:
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)


@pytest.mark.sanity
def test_InCare_Care_Management_All_Activity_Filter_Select_Call(Authorization, Base_Url,set_cookie):
	tc_desc = "Select call in All Activity Filter"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC15"
	tc_priority = "Normal"

	try:
		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_15"]
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
		print(test_data['test_15']['message'])
		raise
	finally:
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)


@pytest.mark.sanity
def test_InCare_Care_Management_All_Activity_Filter_Select_Visit(Authorization, Base_Url,set_cookie):
	tc_desc = "Select Visit in All Activity Filter"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC16"
	tc_priority = "Normal"

	try:
		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_16"]
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
		print(test_data['test_16']['message'])
		raise
	finally:
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)


@pytest.mark.sanity
def test_InCare_Care_Management_All_Activity_Filter_Select_Letters(Authorization, Base_Url,set_cookie):
	tc_desc = "Select Letters in All Activity Filter"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC17"
	tc_priority = "Normal"

	try:
		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_17"]
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
		print(test_data['test_17']['message'])
		raise
	finally:
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)

@pytest.mark.sanity
def test_InCare_Care_Management_All_Activity_Filter_Select_Encounters(Authorization, Base_Url,set_cookie):
	tc_desc = "Select Encounters in All Activity Filter"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC18"
	tc_priority = "Normal"

	try:
		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_18"]
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
		print(test_data['test_18']['message'])
		raise
	finally:
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)

@pytest.mark.sanity
def test_InCare_Care_Management_reedit_completed_task(Authorization, Base_Url,set_cookie):
	tc_desc = "Verify user is able to re-edit the completed task (completed after editing)"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC019"
	tc_priority = "Normal"
	print(tc_desc + " is Executing")
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
		print(e)
		raise
	finally:
		print(tc_desc + "Status:- " + tc_status)
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)

@pytest.mark.sanity
def test_InCare_Care_Management_edit_button(Authorization, Base_Url,set_cookie):
	tc_desc = "Verify edit button on closed care protocol"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC20"
	tc_priority = "Normal"
	print(tc_desc + " is Executing")
	try:
		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_02"]
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
		print(e)
		raise
	finally:
		print(tc_desc + "Status:- " + tc_status)
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)

@pytest.mark.sanity
def test_InCare_Care_Management_Editable_completed_task_engagement(Authorization, Base_Url,set_cookie):
	tc_desc = "Verify the status of completed Engagement/Task should become editable, if the user re-open any Care protocol"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC21"
	tc_priority = "Normal"
	print(tc_desc + " is Executing")
	try:
		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_03"]
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
		print(e)
		raise
	finally:
		print(tc_desc + "Status:- " + tc_status)
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)

@pytest.mark.sanity
def test_InCare_Care_Management_Activities_in_Adhoc_Tasks(Authorization, Base_Url,set_cookie):
	tc_desc = "To verify the available activities in care management_Adhoc_Tasks"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC22"
	tc_priority = "Normal"
	print(tc_desc + " is Executing")
	try:
		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_04"]
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
		print(e)
		raise
	finally:
		print(tc_desc + "Status:- " + tc_status)
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)

@pytest.mark.sanity
def test_InCare_Care_Management_Send_Button(Authorization, Base_Url,set_cookie):
	tc_desc = "Verify User is able to click on send button after typing the message"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC23"
	tc_priority = "Normal"
	print(tc_desc + " is Executing")
	try:
		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_05"]
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
		print(e)
		raise
	finally:
		print(tc_desc + "Status:- " + tc_status)
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)


def test_InCare_Care_Management_24(Authorization, Base_Url,set_cookie):
	tc_desc = "Verify the User is able to Add call Note"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC24"
	tc_priority = "Normal"
	print(tc_desc + " is Executing")
	try:
		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_06"]
		payload = "{\n    \"type\": \"CALL\",\n    \"text\": \"API Health check for call note\"\n}"
		headers = {
			'Authorization': Authorization,
			'Content-Type': 'application/json',
			'Cookie': set_cookie
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		assert response.status_code == 200 or 201
		assert(response.json()['text']) == test_data['test_06']['text']
		assert (response.json()['noteType']) == test_data['test_06']['noteType']
		tc_status = "PASS"
	except Exception as e:
		tc_status = "FAIL"
		print(e)
		raise
	finally:
		print(tc_desc + "Status:- " + tc_status)
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)


def test_InCare_Care_Management_25(Authorization, Base_Url,set_cookie):
	tc_desc = "Verify the functionality of Export icon"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC25"
	tc_priority = "Normal"
	print(tc_desc + " is Executing")
	try:
		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_06"]
		payload = "{\n    \"type\": \"VISIT\",\n    \"text\": \"Visit Ad-hoc Task\",\n    \"visitType\": \"HRA (Health Risk Assessment)\"\n}"
		headers = {
			'Authorization': Authorization,
			'Content-Type': 'application/json',
			'Cookie': set_cookie
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		assert response.status_code == 200 or 201
		assert(response.json()['text']) == test_data['test_07']['text']
		assert (response.json()['metadata']['visitType'])== test_data['test_07']['visitType']
		assert (response.json()['noteType']) == test_data['test_07']['noteType']
		tc_status = "PASS"
	except Exception as e:
		tc_status = "FAIL"
		print(e)
		raise
	finally:
		print(tc_desc + "Status:- " + tc_status)
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)

def test_InCare_Care_Management_26(Authorization, Base_Url,set_cookie):
	tc_desc = "Verify the User is able to create Note Ad-hoc Task"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC26"
	tc_priority = "Normal"
	print(tc_desc + " is Executing")
	try:
		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_06"]
		payload = "{\n    \"type\": \"NOTE\",\n    \"text\": \"Ad-hoc Task \\\"API Health check for Note\\\"\"\n}"
		headers = {
			'Authorization': Authorization,
			'Content-Type': 'application/json',
			'Cookie': set_cookie
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		assert response.status_code == 200 or 201
		assert(response.json()['text']) == test_data['test_08']['text']
		assert (response.json()['noteType']) == test_data['test_08']['noteType']
		tc_status = "PASS"
	except Exception as e:
		tc_status = "FAIL"
		print(e)
		raise
	finally:
		print(tc_desc + "Status:- " + tc_status)
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)


def test_InCare_Care_Management_27(Authorization, Base_Url,set_cookie):
	tc_desc = "Verify the User is able to create New Task"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC27"
	tc_priority = "Normal"
	print(tc_desc + " is Executing")
	try:
		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_09"]["uri"]
		payload = project_data[conftest.cmd_arg]["test_09"]["payload"]
		headers = {
			'Authorization': Authorization,
			'Content-Type': 'application/json',
			'Cookie': set_cookie
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		assert response.status_code == 200
		assert(response.json()['status']) == test_data['test_09']['status']
		assert(response.json()['data']['type']) == test_data['test_09']['type']
		assert (response.json()['data']['note']) == test_data['test_09']['note']
		assert (response.json()['data']['task']) == test_data['test_09']['task']
		tc_status = "PASS"
	except Exception as e:
		tc_status = "FAIL"
		print(e)
		raise
	finally:
		print(tc_desc + "Status:- " + tc_status)
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)


def test_InCare_Care_Management_48(Authorization, Base_Url,set_cookie):
	tc_desc = "Select Care Protocol Unit in All Activity Filter"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC48"
	tc_priority = "Normal"
	print(tc_desc + " is Executing")
	try:
		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_12"]
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
		print(e)
		raise
	finally:
		print(tc_desc + "Status:- " + tc_status)
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)



def test_InCare_Care_Management_49(Authorization, Base_Url,set_cookie):
	tc_desc = "Select Task in All Activity Filter"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC49"
	tc_priority = "Normal"
	print(tc_desc + " is Executing")
	try:
		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_13"]
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
		print(e)
		raise
	finally:
		print(tc_desc + "Status:- " + tc_status)
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)



def test_InCare_Care_Management_50(Authorization, Base_Url,set_cookie):
	tc_desc = "Select Notes in All Activity Filter"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC50"
	tc_priority = "Normal"
	print(tc_desc + " is Executing")
	try:
		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_14"]
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
		print(e)
		raise
	finally:
		print(tc_desc + "Status:- " + tc_status)
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)



def test_InCare_Care_Management_51(Authorization, Base_Url,set_cookie):
	tc_desc = "Select call in All Activity Filter"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC51"
	tc_priority = "Normal"
	print(tc_desc + " is Executing")
	try:
		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_15"]
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
		print(e)
		raise
	finally:
		print(tc_desc + "Status:- " + tc_status)
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)



def test_InCare_Care_Management_52(Authorization, Base_Url,set_cookie):
	tc_desc = "Select Visit in All Activity Filter"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC52"
	tc_priority = "Normal"
	print(tc_desc + " is Executing")
	try:
		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_16"]
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
		print(e)
		raise
	finally:
		print(tc_desc + "Status:- " + tc_status)
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)



def test_InCare_Care_Management_53(Authorization, Base_Url,set_cookie):
	tc_desc = "Select Letters in All Activity Filter"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC53"
	tc_priority = "Normal"
	print(tc_desc + " is Executing")
	try:
		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_17"]
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
		print(e)
		raise
	finally:
		print(tc_desc + "Status:- " + tc_status)
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)


def test_InCare_Care_Management_54(Authorization, Base_Url,set_cookie):
	tc_desc = "Select Encounters in All Activity Filter"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC54"
	tc_priority = "Normal"
	print(tc_desc + " is Executing")
	try:
		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_18"]
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
		print(e)
		raise
	finally:
		print(tc_desc + "Status:- " + tc_status)
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)