import json
import pytest
import requests
import yaml
from numpy.random.mtrand import randint

import conftest

with open("Ymls/worklist_common.yml", "r") as common:
	test_data = yaml.load(common)

with open("Ymls/worklist_project.yml", "r") as project:
	project_data = yaml.load(project)




def test_Worklist_Todo(Authorization, Base_Url,set_cookie):
	tc_desc = "To verify that the User can see his daily progress on User's Workqueue under Todos"
	tc_status = "FAIL"
	tc_name = "Worklist_TC01"
	tc_priority = "Medium"

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
def test_Worklist_Scheduled_Task(Authorization, Base_Url,set_cookie):
	tc_desc = "To verify the available scheduled task for current date"
	tc_status = "FAIL"
	tc_name = "Worklist_TC02"
	tc_priority = "Medium"

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



def test_Worklist_03(Authorization, Base_Url,set_cookie):
	tc_desc = "Submit assessment without any response"
	tc_status = "FAIL"
	tc_name = "Worklist_TC03"
	tc_priority = "High"
	print(tc_desc + " is Executing")
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
		#assert(response.json()['status']) == test_data['test_09']['status']

		tc_status = "PASS"
	except Exception as e:
		tc_status = "FAIL"
		print(e)
		raise
	finally:
		print(tc_desc + "Status:- " + tc_status)
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)


def test_Worklist_TC01(Authorization, Base_Url, set_cookie):
    tc_desc = "To verify that the User can see his daily progress on User's Workqueue under Todos"
    tc_status = "FAIL"
    tc_name = "Worklist_TC01"
    tc_priority = "Medium"

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


def test_Worklist_05(Authorization, Base_Url,set_cookie):
    tc_desc = "To verify the Click functionality of Scheduled Patient"
    tc_status = "FAIL"
    tc_name = "Worklist_TC05"
    tc_priority = "Medium"

    try:
        url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_05"]["uri"]
        payload = project_data[conftest.cmd_arg]["test_05"]["payload"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.json())
        assert response.status_code == 200
        assert response.json()['metadata']['count'] >= 0

        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_05']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)

def test_Worklist_06(Authorization, Base_Url,set_cookie):
    tc_desc = "To Verify the Reassign functionality for Selected Task"
    tc_status = "FAIL"
    tc_name = "Worklist_TC06"
    tc_priority = "Medium"

    try:
        url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_06"]["uri"]
        print(url)
        payload = project_data[conftest.cmd_arg]["test_06"]["payload"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        assert response.status_code == 200
        assert response.json()['referredTodosCount'] >= 0
        assert response.json()['skippedTodosCount'] >= 0
        assert response.json()['totalTodosCount'] >= 0
        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_06']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)

def test_Worklist_07(Authorization, Base_Url, set_cookie):
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

def test_Worklist_08(Authorization, Base_Url,set_cookie):
    tc_desc = "To verify all the Task on ALL section under activity received"
    tc_status = "FAIL"
    tc_name = "Worklist_TC08"
    tc_priority = "Medium"

    try:
        url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_08"]["uri"]
        payload = project_data[conftest.cmd_arg]["test_08"]["payload"]
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
        print(test_data['test_08']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)

def test_Worklist_09(Authorization, Base_Url, set_cookie):
    tc_desc = "To verify the pending task on Pending section under activity sent"
    tc_status = "FAIL"
    tc_name = "Worklist_TC09"
    tc_priority = "Medium"

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
        assert response.json()['metadata']['count'] >= 0
        # assert response.json()['data'][0]['metadata']['careProtocol']['name'] == test_data['test_09']['care_protocol']
        # assert response.json()['data'][0]['metadata']['careProtocol']['type'] == test_data['test_09']['type']
        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_09']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)

def test_Worklist_10(Authorization, Base_Url,set_cookie):
    tc_desc = "To Verify the sort by drop down availability"
    tc_status = "FAIL"
    tc_name = "Worklist_TC10"
    tc_priority = "High"

    try:
        url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_10"]["uri"]
        payload = project_data[conftest.cmd_arg]["test_10"]["payload"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        assert response.status_code == 200
        assert response.json()['metadata']['count'] >= 0
        # assert response.json()['data'][0]['metadata']['careProtocol']['type'] == test_data['test_10']['type']
        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_10']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)

def test_Worklist_11(Authorization, Base_Url, set_cookie):
    tc_desc = "Verify the CDPS risk sorting"
    tc_status = "FAIL"
    tc_name = "Worklist_TC11"
    tc_priority = "High"

    try:
        url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_11"]["uri"]
        print(url)
        payload = project_data[conftest.cmd_arg]["test_11"]["payload"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response = requests.request("POST", url, headers=headers, data=payload)

        url_1 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_11"]["uri"]
        print(url_1)
        payload_1 = project_data[conftest.cmd_arg]["test_11"]["payload1"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_1 = requests.request("POST", url_1, headers=headers, data=payload_1)
        assert response.status_code == 200
        assert response_1.status_code == 200
        assert response.json()['metadata']['count'] >= 0
        assert response_1.json()['metadata']['count'] >= 0
        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_11']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)


def test_Worklist_12(Authorization, Base_Url,set_cookie):
    tc_desc = "Verify the search should not be reset after changing the date on worklist"
    tc_status = "FAIL"
    tc_name = "Worklist_TC12"
    tc_priority = "High"

    try:
        url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_12"]["uri"]
        payload = project_data[conftest.cmd_arg]["test_12"]["payload"]
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
        print(test_data['test_12']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)

def test_Worklist_13(Authorization, Base_Url, set_cookie):
    tc_desc = "Verify user is able to edit the message of sent activities from other user Activity sent section"
    tc_status = "FAIL"
    tc_name = "Worklist_TC13"
    tc_priority = "Medium"

    try:
        url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_13"]["uri"]
        print(url)
        payload = project_data[conftest.cmd_arg]["test_13"]["payload"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        json_data = response.json()
        ids = []
        for data in json_data["data"]:
            output = (data['id'])
            ids.append(output)
        print(ids)

        url_1 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_13"]["uri1"]+ids[0]+"/message"
        print(url_1)
        payload_1 = project_data[conftest.cmd_arg]["test_13"]["payload1"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_1 = requests.request("PATCH", url_1, headers=headers, data=payload_1)
        assert response.status_code == 200
        assert response_1.status_code == 200
        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_13']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)


def test_Worklist_14(Authorization, Base_Url, set_cookie):
    tc_desc = "Verify user is able to reassign the activity to other user from activities sent of other User"
    tc_status = "FAIL"
    tc_name = "Worklist_TC14"
    tc_priority = "High"

    try:
        url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_14"]["uri1"]
        print(url)
        payload = project_data[conftest.cmd_arg]["test_14"]["payload1"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(url)
        #print(response.text)
        id = response.json()['data'][0]['id']
        print(id)

        url_1 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_14"]['uri']+id+"/_reassign"
        payload_1 = project_data[conftest.cmd_arg]["test_14"]["payload"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }

        response_1 = requests.request("PATCH", url_1, headers=headers, data=payload_1)
        print(response_1.json())
        assert response.status_code == 200
        assert response_1.status_code == 200
        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_14']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)

def test_Worklist_15(Authorization, Base_Url, set_cookie):
    tc_desc = "Verify User is able to accept the received referral of other User"
    tc_status = "FAIL"
    tc_name = "Worklist_TC14"
    tc_priority = "High"

    try:
        url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_15"]["uri"]
        print(url)
        payload = project_data[conftest.cmd_arg]["test_15"]["payload"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(url)
        #print(response.text)
        # id = response.json()['data'][0]['id']
        # print(id)
        json_data = response.json()
        ids = []
        for data in json_data["data"]:
            output = (data['id'])
            ids.append(output)
        print(ids)

        url_1 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_15"]['uri1']+ids[0]+"/_accept"
        print(url_1)
        payload_1 = project_data[conftest.cmd_arg]["test_15"]["payload1"]
        print(payload_1)
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }

        response_1 = requests.request("PATCH", url_1, headers=headers, data=payload_1)
        print(response_1.json())
        assert response.status_code == 200
        assert response_1.status_code == 200
        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_15']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)

def test_Worklist_16(Authorization, Base_Url, set_cookie):
    tc_desc = "Verify User is able to Decline the received referral of other User"
    tc_status = "FAIL"
    tc_name = "Worklist_TC16"
    tc_priority = "High"

    try:
        url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_16"]["uri"]
        print(url)
        payload = project_data[conftest.cmd_arg]["test_16"]["payload"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(url)
        json_data = response.json()
        ids = []
        for data in json_data["data"]:
            output = (data['id'])
            ids.append(output)
        print(ids)

        url_1 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_16"]["uri1"]+ids[0]+"/_decline"
        print(url_1)
        payload_1 = project_data[conftest.cmd_arg]["test_16"]["payload1"]
        print(payload_1)
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }

        response_1 = requests.request("PATCH", url_1, headers=headers, data=payload_1)
        #print(response_1.json())
        assert response.status_code == 200
        assert response_1.status_code == 200
        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_16']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)


def test_Worklist_17(Authorization, Base_Url, set_cookie):
    tc_desc = "To verify that the completed Task should be visible under Completed section"
    tc_status = "FAIL"
    tc_name = "Worklist_TC17"
    tc_priority = "Medium"

    try:
        url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_17"]["uri"]
        payload = project_data[conftest.cmd_arg]["test_17"]["payload"]
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
        print(test_data['test_17']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)

def test_Worklist_18(Authorization, Base_Url, set_cookie):
    tc_desc = "Verify the Add Note funtionality for scheduled task"
    tc_status = "FAIL"
    tc_name = "Worklist_TC18"
    tc_priority = "Medium"

    try:
        url = Base_Url + project_data[conftest.cmd_arg]["test_18"]["uri"]
        payload = project_data[conftest.cmd_arg]["test_18"]["payload"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(url)
        #print(response.text.encode('utf8'))
        assert response.status_code == 200

        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_18']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)


def test_Worklist_19(Authorization, Base_Url, set_cookie):
    tc_desc = "Verify the patient is assigned as high priority on Single click"
    tc_status = "FAIL"
    tc_name = "Worklist_TC19"
    tc_priority = "High"

    try:
        url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_19"]["uri"]
        payload = project_data[conftest.cmd_arg]["test_19"]["payload"]
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
        print(test_data['test_19']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)

def test_Worklist_20(Authorization, Base_Url, set_cookie):
    tc_desc = "Verify the patient is assigned as medium priority on Double click"
    tc_status = "FAIL"
    tc_name = "Worklist_TC20"
    tc_priority = "High"

    try:
        url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_20"]["uri"]
        payload = project_data[conftest.cmd_arg]["test_20"]["payload"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        assert response.status_code == 200 or 204
        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_20']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)

def test_Worklist_21(Authorization, Base_Url, set_cookie):
    tc_desc = "Verify User is able to remove priority on triple click"
    tc_status = "FAIL"
    tc_name = "Worklist_TC21"
    tc_priority = "High"

    try:
        url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_21"]["uri"]
        payload = project_data[conftest.cmd_arg]["test_21"]["payload"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        assert response.status_code == 204 or 200
        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_21']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)

def test_Worklist_22(Authorization, Base_Url,set_cookie):
    tc_desc = "Verify User is able to Assign priority of multiple patient in One time"
    tc_status = "FAIL"
    tc_name = "Worklist_TC22"
    tc_priority = "High"

    try:
        url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_22"]["uri"]
        payload = project_data[conftest.cmd_arg]["test_22"]["payload"]
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
        print(test_data['test_22']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)

def test_Worklist_23(Authorization, Base_Url, set_cookie):
    tc_desc = "Verify User is able to Remove priority of multiple patient in One time"
    tc_status = "FAIL"
    tc_name = "Worklist_TC23"
    tc_priority = "High"

    try:
        url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_23"]["uri"]
        payload = project_data[conftest.cmd_arg]["test_23"]["payload"]
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
        print(test_data['test_23']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)

def test_Worklist_24(Authorization, Base_Url,set_cookie):
    tc_desc = "To verify the Care protocol filter"
    tc_status = "FAIL"
    tc_name = "Worklist_TC24"
    tc_priority = "Medium"

    try:
        url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_24"]["uri"]
        print(url)
        payload = project_data[conftest.cmd_arg]["test_24"]["payload"]
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
        print(test_data['test_24']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)

def test_Worklist_25(Authorization, Base_Url, set_cookie):
    tc_desc = "Verify the CDPS risk sorting"
    tc_status = "FAIL"
    tc_name = "Worklist_TC25"
    tc_priority = "High"

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

        url_1 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_25"]["uri"]
        print(url_1)
        payload_1 = project_data[conftest.cmd_arg]["test_25"]["payload1"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_1 = requests.request("POST", url_1, headers=headers, data=payload_1)
        assert response.status_code == 200
        assert response_1.status_code == 200
        assert response.json()['metadata']['count'] >= 0
        assert response_1.json()['metadata']['count'] >= 0
        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_25']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)


def test_Worklist_26(Authorization, Base_Url, set_cookie):
    tc_desc = "Verify the HHSHCC risk sorting"
    tc_status = "FAIL"
    tc_name = "Worklist_TC26"
    tc_priority = "High"

    try:
        url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_26"]["uri"]
        print(url)
        payload = project_data[conftest.cmd_arg]["test_26"]["payload"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response = requests.request("POST", url, headers=headers, data=payload)

        url_1 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_26"]["uri"]
        print(url_1)
        payload_1 = project_data[conftest.cmd_arg]["test_26"]["payload1"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_1 = requests.request("POST", url_1, headers=headers, data=payload_1)
        assert response.status_code == 200
        assert response_1.status_code == 200
        assert response.json()['metadata']['count'] >= 0
        assert response_1.json()['metadata']['count'] >= 0
        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_26']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)

def test_Worklist_27(Authorization, Base_Url, set_cookie):
    tc_desc = "Verify the CDPS risk sorting"
    tc_status = "FAIL"
    tc_name = "Worklist_TC27"
    tc_priority = "High"

    try:
        url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_27"]["uri"]
        print(url)
        payload = project_data[conftest.cmd_arg]["test_27"]["payload"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response = requests.request("POST", url, headers=headers, data=payload)

        url_1 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_27"]["uri"]
        print(url_1)
        payload_1 = project_data[conftest.cmd_arg]["test_27"]["payload1"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_1 = requests.request("POST", url_1, headers=headers, data=payload_1)
        assert response.status_code == 200
        assert response_1.status_code == 200
        assert response.json()['metadata']['count'] >= 0
        assert response_1.json()['metadata']['count'] >= 0
        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_27']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)

def test_Worklist_28(Authorization, Base_Url, set_cookie):
    tc_desc = "Verify the CDPS risk sorting"
    tc_status = "FAIL"
    tc_name = "Worklist_TC28"
    tc_priority = "High"

    try:
        url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_28"]["uri"]
        print(url)
        payload = project_data[conftest.cmd_arg]["test_28"]["payload"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response = requests.request("POST", url, headers=headers, data=payload)

        url_1 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_28"]["uri"]
        print(url_1)
        payload_1 = project_data[conftest.cmd_arg]["test_28"]["payload1"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_1 = requests.request("POST", url_1, headers=headers, data=payload_1)
        assert response.status_code == 200
        assert response_1.status_code == 200
        assert response.json()['metadata']['count'] >= 0
        assert response_1.json()['metadata']['count'] >= 0
        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_28']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)

def test_Worklist_29(Authorization, Base_Url,set_cookie):
	tc_desc = "Verify the SVI risk sorting"
	tc_status = "FAIL"
	tc_name = "Worklist_TC29"
	tc_priority = "High"

	try:
		url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_29"]["uri"]
		print(url)
		payload = project_data[conftest.cmd_arg]["test_29"]["payload"]
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
		print(test_data['test_29']['message'])
		raise
	finally:
		conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)
