# import json
#
# import pytest
# import requests
# import yaml
# from numpy.random.mtrand import randint
#
# import conftest
#
#
# with open("YML/common.yml", "r") as common:
# 	test_data = yaml.load(common)
#
# with open("YML/project.yml", "r") as project:
# 	project_data = yaml.load(project)
#
# with open('expected.json') as json_file:
# 	expected_json = json.load(json_file)
#
#
# def test_InCare_01_Assesment_p1(Authorization, Base_Url):
# 	tc_desc = test_data['test_01']['testcase']
# 	tc_status = "FAIL"
# 	tc_name = "TC01"
# 	tc_priority = "High"
# 	print(tc_desc + " is Executing")
# 	try:
# 		url = Base_Url + test_data['test_01']['uri'] + project_data[conftest.cmd_arg]["test_01"]
# 		payload = {}
# 		headers = {
# 			'Authorization': Authorization
# 		}
# 		response = requests.request("GET", url, headers=headers, data=payload)
# 		assert response.status_code == 200
# 		tc_status = "PASS"
# 		print(response.json())
#
# 	except Exception as e:
# 		tc_status = "FAIL"
# 		print(e)
# 		raise
# 	finally:
# 		print(tc_desc + " " + "Status:- " + tc_status + "\n")
# 		conftest.updatedb(tc_name, tc_desc, tc_status,tc_priority)
#
#
#
# def test_InCare_02_assessment_p1(Authorization, Base_Url):
# 	tc_desc = test_data['test_02']['testcase']
# 	tc_status = "FAIL"
# 	tc_name = "TC02"
# 	tc_priority = "High"
# 	print(tc_desc + " is Executing")
# 	try:
# 		url = Base_Url + test_data['test_02']['uri'] + project_data[conftest.cmd_arg]["test_02"]
# 		payload = {}
# 		headers = {
# 			'Authorization': Authorization
# 		}
# 		response = requests.request("GET", url, headers=headers, data=payload)
# 		assert response.status_code == test_data['test_02']['status']
# 		tc_status = "PASS"
# 	except Exception as e:
# 		tc_status = "FAIL"
# 		print(e)
# 		raise
# 	finally:
# 		print(tc_desc + "Status:- " + tc_status)
# 		conftest.updatedb(tc_name, tc_desc, tc_status,tc_priority)
#
#
# def test_InCare_03_assessment_p1(Authorization, Base_Url):
# 	tc_desc = test_data['test_03']['testcase']
# 	tc_status = "FAIL"
# 	tc_name = "TC03"
# 	tc_priority = "High"
# 	print(tc_desc + " is Executing")
# 	try:
# 		url = Base_Url + test_data['test_03']['uri'] + project_data[conftest.cmd_arg]["test_03"]
# 		payload = {}
# 		headers = {
# 			'Authorization': Authorization
# 		}
# 		response = requests.request("GET", url, headers=headers, data=payload)
# 		assert response.status_code == test_data['test_03']['status']
# 		tc_status = "PASS"
# 	except Exception as e:
# 		tc_status = "FAIL"
# 		print(e)
# 		raise
# 	finally:
# 		print(tc_desc + "Status:- " + tc_status)
# 		conftest.updatedb(tc_name, tc_desc, tc_status,tc_priority)
#
#
# def test_InCare_04_assessment_p1(Authorization, Base_Url):
# 	tc_desc = test_data['test_04']['testcase']
# 	tc_status = "FAIL"
# 	tc_name = "TC04"
# 	tc_priority = "High"
# 	print(tc_desc + " is Executing")
# 	try:
# 		url = Base_Url + test_data['test_04']['uri'] + project_data[conftest.cmd_arg]["test_04"]
# 		payload = {}
# 		headers = {
# 			'Authorization': Authorization
# 		}
# 		response = requests.request("GET", url, headers=headers, data=payload)
# 		assert response.status_code == test_data['test_04']['status']
# 		tc_status = "PASS"
# 	except Exception as e:
# 		tc_status = "FAIL"
# 		print(e)
# 		raise
# 	finally:
# 		print(tc_desc + "Status:- " + tc_status)
# 		conftest.updatedb(tc_name, tc_desc, tc_status,tc_priority)
#
#
# def test_InCare_05_assessment_p1(Authorization, Base_Url):
# 	tc_desc = test_data['test_05']['testcase']
# 	tc_status = "FAIL"
# 	tc_name = "TC05"
# 	tc_priority = "High"
# 	print(tc_desc + " is Executing")
# 	try:
# 		url = Base_Url + test_data['test_05']['uri'] + project_data[conftest.cmd_arg]["test_05"]
# 		payload = {}
# 		headers = {
# 			'Authorization': Authorization
# 		}
# 		response = requests.request("GET", url, headers=headers, data=payload)
# 		assert response.status_code == test_data['test_05']['status']
# 		tc_status = "PASS"
# 	except Exception as e:
# 		tc_status = "FAIL"
# 		print(e)
# 		raise
# 	finally:
# 		print(tc_desc + "Status:- " + tc_status)
# 		conftest.updatedb(tc_name, tc_desc, tc_status,tc_priority)
#
#
# def test_InCare_06_AdhocTask_p1(Authorization, Base_Url):
# 	tc_desc = test_data['test_06']['testcase']
# 	tc_status = "FAIL"
# 	tc_name = "TC06"
# 	tc_priority = "High"
# 	print(tc_desc + " is Executing")
# 	try:
# 		url = Base_Url + test_data['test_06']['uri']
# 		payload = {}
# 		headers = {
# 			'Authorization': Authorization
# 		}
# 		response = requests.request("GET", url, headers=headers, data=payload)
# 		assert response.status_code == 200
# 		tc_status = "PASS"
# 	except Exception as e:
# 		tc_status = "FAIL"
# 		print(e)
# 		raise
# 	finally:
# 		print(tc_desc + "Status:- " + tc_status)
# 		conftest.updatedb(tc_name, tc_desc, tc_status,tc_priority)
#
#
# def test_InCare_07_AdhocTask_p1(Authorization, Base_Url):
# 	global role_id
# 	tc_desc = test_data['test_07']['testcase']
# 	tc_status = "FAIL"
# 	tc_name = "TC07"
# 	tc_priority = "High"
# 	print(tc_desc + " is Executing")
# 	try:
# 		url = Base_Url + test_data['test_07']['uri']
# 		name = "test" + str(randint(0, 999))
#
#
# 		payload = "{\r\n\t\"name\": \"" + name + "\"\r\n}"
# 		headers = {
# 			'Authorization': Authorization,
# 			'Content-Type': 'application/json'
# 		}
# 		response = requests.request("POST", url, headers=headers, data=payload)
# 		assert response.status_code == test_data['test_07']['status']
# 		tc_status = "PASS"
# 	except Exception as e:
# 		tc_status = "FAIL"
# 		print(e)
# 		raise
# 	finally:
# 		print(tc_desc + "Status:- " + tc_status)
# 		conftest.updatedb(tc_name, tc_desc, tc_status,tc_priority)
#
#
#
# def test_InCare_08_AdhocTask_p1(Authorization, Base_Url):
# 	tc_desc = test_data['test_08']['testcase']
# 	tc_status = "FAIL"
# 	tc_name = "TC08"
# 	tc_priority = "High"
# 	print(tc_desc + " is Executing")
# 	try:
# 		url = Base_Url + test_data['test_08']['uri']
# 		payload = "{\r\n\t\"name\": \"Adhoc Api Test5\",\r\n\t\"active\": false\r\n}"
# 		headers = {
# 			'Authorization': Authorization,
# 			'Content-Type': 'application/json'
# 		}
# 		response = requests.request("PATCH", url, headers=headers, data=payload)
# 		assert response.status_code == test_data['test_08']['status']
# 		tc_status = "PASS"
# 	except Exception as e:
# 		tc_status = "FAIL"
# 		print(e)
# 		raise
# 	finally:
# 		print(tc_desc + "Status:- " + tc_status)
# 		conftest.updatedb(tc_name, tc_desc, tc_status,tc_priority)
#
#
# def test_InCare_09_AdhocTassk_p1(Authorization, Base_Url):
# 	tc_desc = test_data['test_09']['testcase']
# 	tc_status = "FAIL"
# 	tc_name = "TC09"
# 	tc_priority = "High"
# 	print(tc_desc + " is Executing")
# 	try:
# 		url = Base_Url + test_data['test_09']['uri']
# 		payload = "{\r\n\t\"adHocTaskIds\": [\"5ebd86917f9b711398ba4fbc\", \"5ebd86917f9b711398ba4fbe\"]\r\n}"
# 		headers = {
# 			'Authorization': Authorization,
# 			'content-type': "application/json"
# 		}
# 		response = requests.request("PATCH", url, data=payload, headers=headers)
# 		assert response.status_code == test_data['test_09']['status']
# 		tc_status = "PASS"
# 	except Exception as e:
# 		tc_status = "FAIL"
# 		print(e)
# 		raise
# 	finally:
# 		print(tc_desc + "Status:- " + tc_status)
# 		conftest.updatedb(tc_name, tc_desc, tc_status,tc_priority)
#
# def test_InCare_10_PatientNotes_p1(Authorization, Base_Url):
# 	tc_desc = test_data['test_10']['testcase']
# 	tc_status = "FAIL"
# 	tc_name = "TC10"
# 	tc_priority = "High"
# 	print(tc_desc + " is Executing")
# 	try:
# 		url = Base_Url + test_data['test_10']['uri'] + project_data[conftest.cmd_arg]["test_10"]
# 		payload = {}
# 		headers = {
# 			'Authorization': Authorization
# 		}
# 		response = requests.request("GET", url, headers=headers, data=payload)
# 		assert response.status_code == test_data['test_10']['status']
# 		tc_status = "PASS"
# 	except Exception as e:
# 		tc_status = "FAIL"
# 		print(e)
# 		raise
# 	finally:
# 		print(tc_desc + "Status:- " + tc_status)
# 		conftest.updatedb(tc_name, tc_desc, tc_status,tc_priority)
#
#
# def test_InCare_11_PatientNotes_p1(Authorization, Base_Url):
# 	global role_id
# 	tc_desc = test_data['test_11']['testcase']
# 	tc_status = "FAIL"
# 	tc_name = "TC11"
# 	tc_priority = "High"
# 	print(tc_desc + " is Executing")
# 	try:
# 		url = Base_Url + test_data['test_11']['uri']
# 		payload = "{\"cardTypes\":[]}"
# 		headers = {
# 			'Authorization': Authorization,
# 			'Content-Type': 'application/json'
# 		}
# 		response = requests.request("POST", url, headers=headers, data = payload)
# 		assert response.status_code == test_data['test_11']['status']
# 		tc_status = "PASS"
# 	except Exception as e:
# 		tc_status = "FAIL"
# 		print(e)
# 		raise
# 	finally:
# 		print(tc_desc + "Status:- " + tc_status)
# 		conftest.updatedb(tc_name, tc_desc, tc_status,tc_priority)
#
# def test_InCare_12_Assesment_p1(Authorization, Base_Url):
# 	tc_desc = test_data['test_12']['testcase']
# 	tc_status = "FAIL"
# 	tc_name = "TC12"
# 	tc_priority = "High"
# 	print(tc_desc + " is Executing")
# 	try:
# 		url = Base_Url + test_data['test_12']['uri'] + project_data[conftest.cmd_arg]["test_12"]
# 		payload = {}
# 		headers = {
# 			'Authorization': Authorization
# 		}
# 		response = requests.request("GET", url, headers=headers, data=payload)
# 		assert response.status_code == test_data['test_12']['status']
# 		tc_status = "PASS"
# 		print(response.json())
#
# 	except Exception as e:
# 		tc_status = "FAIL"
# 		print(e)
# 		raise
# 	finally:
# 		print(tc_desc + " " + "Status:- " + tc_status + "\n")
# 		conftest.updatedb(tc_name, tc_desc, tc_status,tc_priority)
#
# def test_InCare_13_CareProtocol_p1(Authorization, Base_Url):
# 	tc_desc = "Verify that user is able to view the care protocol on clicking Care management"
# 	tc_status = "FAIL"
# 	tc_name = "TC13"
# 	tc_priority = "High"
# 	print(tc_desc + " is Executing")
# 	try:
# 		url = Base_Url + test_data['test_13']['uri'] + project_data[conftest.cmd_arg]["test_13"]
# 		payload = {}
# 		headers = {
# 			'Authorization': Authorization
# 		}
# 		response = requests.request("GET", url, headers=headers, data=payload)
# 		assert response.status_code == test_data['test_13']['status']
# 		tc_status = "PASS"
#
#
# 	except Exception as e:
# 		tc_status = "FAIL"
# 		print(e)
# 		raise
# 	finally:
# 		print(tc_desc + " " + "Status:- " + tc_status + "\n")
# 		conftest.updatedb(tc_name, tc_desc, tc_status,tc_priority)
#
# def test_InCare_14_CareProtocol_p1(Authorization, Base_Url):
# 	tc_desc = " Verify that user is able to view the care protocol details on care timeline"
# 	tc_status = "FAIL"
# 	tc_name = "TC14"
# 	tc_priority = "High"
# 	print(tc_desc + " is Executing")
# 	try:
# 		url = Base_Url + test_data['test_14']['uri'] + project_data[conftest.cmd_arg]["test_14"]
# 		payload = {}
# 		headers = {
# 			'Authorization': Authorization
# 		}
# 		response = requests.request("GET", url, headers=headers, data=payload)
# 		assert response.status_code == test_data['test_14']['status']
# 		tc_status = "PASS"
#
#
# 	except Exception as e:
# 		tc_status = "FAIL"
# 		print(e)
# 		raise
# 	finally:
# 		print(tc_desc + " " + "Status:- " + tc_status + "\n")
# 		conftest.updatedb(tc_name, tc_desc, tc_status,tc_priority)
#
#
# def test_InCare_15_CareProtocol_p1(Authorization, Base_Url):
# 	tc_desc = "verify count of only active protocol is displaying on care protocol tab"
# 	tc_status = "FAIL"
# 	tc_name = "TC15"
# 	tc_priority = "High"
# 	print(tc_desc + " is Executing")
# 	try:
# 		url = Base_Url + test_data['test_15']['uri'] + project_data[conftest.cmd_arg]["test_15"]
# 		payload = {}
# 		headers = {
# 			'Authorization': Authorization
# 		}
# 		response = requests.request("GET", url, headers=headers, data=payload)
# 		assert response.json()['count'] == test_data['test_15']['count']
# 		tc_status = "PASS"
#
#
# 	except Exception as e:
# 		tc_status = "FAIL"
# 		print(e)
# 		raise
# 	finally:
# 		print(tc_desc + " " + "Status:- " + tc_status + "\n")
# 		conftest.updatedb(tc_name, tc_desc, tc_status,tc_priority)
#
# def test_InCare_16_CareProtocol_p1(Authorization, Base_Url):
# 	tc_desc = " verify user is able to see the list of protocols on clicking the Assign Care protocol button."
# 	tc_status = "FAIL"
# 	tc_name = "TC16"
# 	tc_priority = "High"
# 	print(tc_desc + " is Executing")
# 	try:
# 		url = Base_Url + test_data['test_16']['uri'] + project_data[conftest.cmd_arg]["test_16"]
# 		payload = {}
# 		headers = {
# 			'Authorization': Authorization
# 		}
# 		response = requests.request("GET", url, headers=headers, data=payload)
# 		assert response.json()['count'] == test_data['test_16']['count']
#
# 		print(response.json()['hits'])
# 		tc_status = "PASS"
#
#
#         except Exception as e:
#             tc_status = "FAIL"
#             print(e)
#             raise
#         finally:
#             print(tc_desc + " " + "Status:- " + tc_status + "\n")
#             conftest.updatedb(tc_name, tc_desc, tc_status,tc_priority)
#
#
#
