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


def test_InCare_Care_Management_01(Authorization, Base_Url,set_cookie):
	tc_desc = "To verify the navigation to Care management"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC01"
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
def test_InCare_Care_Management_02(Authorization, Base_Url,set_cookie):
	tc_desc = "To verify the available activities in care management_health_modules"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC02"
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

def test_InCare_Care_Management_03(Authorization, Base_Url,set_cookie):
	tc_desc = "To verify the available activities in care management_goals"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC03"
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

def test_InCare_Care_Management_04(Authorization, Base_Url,set_cookie):
	tc_desc = "To verify the available activities in care management_Adhoc_Tasks"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC04"
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

def test_InCare_Care_Management_05(Authorization, Base_Url,set_cookie):
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
		print(e)
		raise
	finally:
		print(tc_desc + "Status:- " + tc_status)
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)


def test_InCare_Care_Management_06(Authorization, Base_Url,set_cookie):
	tc_desc = "Verify the User is able to Add call Note"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC06"
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


def test_InCare_Care_Management_07(Authorization, Base_Url,set_cookie):
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
		print(e)
		raise
	finally:
		print(tc_desc + "Status:- " + tc_status)
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)

def test_InCare_Care_Management_08(Authorization, Base_Url,set_cookie):
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
		print(e)
		raise
	finally:
		print(tc_desc + "Status:- " + tc_status)
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)


def test_InCare_Care_Management_09(Authorization, Base_Url,set_cookie):
	tc_desc = "Verify the User is able to create New Task"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC09"
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


def test_InCare_Care_Management_10(Authorization, Base_Url,set_cookie):
	tc_desc = "Verify the User is able to create Letter"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC010"
	tc_priority = "Normal"
	print(tc_desc + " is Executing")
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
		print(e)
		raise
	finally:
		print(tc_desc + "Status:- " + tc_status)
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)


def test_InCare_Care_Management_11(Authorization, Base_Url,set_cookie):
	tc_desc = "Select Care Protocol in All Activity Filter"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC11"
	tc_priority = "Normal"
	print(tc_desc + " is Executing")
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
		print(e)
		raise
	finally:
		print(tc_desc + "Status:- " + tc_status)
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)



def test_InCare_Care_Management_12(Authorization, Base_Url,set_cookie):
	tc_desc = "Select Care Protocol Unit in All Activity Filter"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC12"
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



def test_InCare_Care_Management_13(Authorization, Base_Url,set_cookie):
	tc_desc = "Select Task in All Activity Filter"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC13"
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



def test_InCare_Care_Management_14(Authorization, Base_Url,set_cookie):
	tc_desc = "Select Notes in All Activity Filter"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC14"
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



def test_InCare_Care_Management_15(Authorization, Base_Url,set_cookie):
	tc_desc = "Select call in All Activity Filter"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC15"
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



def test_InCare_Care_Management_16(Authorization, Base_Url,set_cookie):
	tc_desc = "Select Visit in All Activity Filter"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC16"
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



def test_InCare_Care_Management_17(Authorization, Base_Url,set_cookie):
	tc_desc = "Select Letters in All Activity Filter"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC17"
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


def test_InCare_Care_Management_18(Authorization, Base_Url,set_cookie):
	tc_desc = "Select Encounters in All Activity Filter"
	tc_status = "FAIL"
	tc_name = "Care_Management_TC18"
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

