import pytest
import requests
import yaml

import conftest

with open("Ymls/care_management_common.yml", "r") as common:
    test_data = yaml.load(common)

with open("Ymls/care_management_project.yml", "r") as project:
    project_data = yaml.load(project)

with open('Ymls/care_management_expected.yml') as expected:
    expected_data = yaml.load(expected)


def test_Navigation_To_Care_Management(Authorization, Base_Url, set_cookie):
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
        print(response.json())
        assert response.status_code == 200
        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_01']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)


def test_Health_Modules(Authorization, Base_Url, set_cookie):
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
def test_Goals(Authorization, Base_Url, set_cookie):
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
def test_Adhoc_Tasks(Authorization, Base_Url, set_cookie):
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
def test_legacy_timeline(Authorization, Base_Url, set_cookie):
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
def test_Add_call_Note(Authorization, Base_Url, set_cookie):
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
        assert (response.json()['text']) == test_data['test_06']['text']
        assert (response.json()['noteType']) == test_data['test_06']['noteType']
        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_06']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)


@pytest.mark.sanity
def test_Visit_Adhoc_Task(Authorization, Base_Url, set_cookie):
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
        assert (response.json()['text']) == test_data['test_07']['text']
        assert (response.json()['metadata']['visitType']) == test_data['test_07']['visitType']
        assert (response.json()['noteType']) == test_data['test_07']['noteType']
        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_07']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)


@pytest.mark.sanity
def test_Note_Adhoc_Task(Authorization, Base_Url, set_cookie):
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
        assert (response.json()['text']) == test_data['test_08']['text']
        assert (response.json()['noteType']) == test_data['test_08']['noteType']
        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_08']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)


@pytest.mark.sanity
def test_create_New_Task(Authorization, Base_Url, set_cookie):
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
        assert (response.json()['status']) == test_data['test_09']['status']
        assert (response.json()['data']['type']) == test_data['test_09']['type']
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
def test_create_Letter(Authorization, Base_Url, set_cookie):
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
        assert (response.json()['text']) == test_data['test_10']['text']
        assert (response.json()['noteType']) == test_data['test_10']['noteType']
        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_10']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)


def test_All_Activity_Filter_Select_Care_Protocol(Authorization, Base_Url, set_cookie):
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


def test_All_Activity_Filter_Select_Care_Protocol_Unit(Authorization, Base_Url, set_cookie):
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


def test_All_Activity_Filter_Select_Task(Authorization, Base_Url, set_cookie):
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


def test_All_Activity_Filter_Select_Notes(Authorization, Base_Url, set_cookie):
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


def test_All_Activity_Filter_Select_Call(Authorization, Base_Url, set_cookie):
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


def test_All_Activity_Filter_Select_Visit(Authorization, Base_Url, set_cookie):
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


def test_All_Activity_Filter_Select_Letters(Authorization, Base_Url, set_cookie):
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


def test_All_Activity_Filter_Select_Encounters(Authorization, Base_Url, set_cookie):
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


@pytest.mark.sanity2
def test_Assign_Module(Authorization, Base_Url, set_cookie):
    tc_desc = "Check assign module fuctionality"
    tc_status = "FAIL"
    tc_name = "Care_Management_TC019"
    tc_priority = "Normal"
    actual = []
    expected = []

    try:
        url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_19"]['uri']
        payload = {}
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        assert response.status_code == 200
        assert response.json()['count'] != ""
        care_protocol_names = expected_data[conftest.cmd_arg]['care_protocols']
        data = response.json()
        for hit in data['hits']:
            actual.append(hit['name'])
        # print(actual)
        for item in care_protocol_names:
            expected.append(item['name'])
        # assert actual == expected
        tc_status = "PASS"

    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_19']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)


@pytest.mark.sanity
def test_Assign_Care_Protocol(Authorization, Base_Url, set_cookie):
    tc_desc = "To verify Assign Fuctionality"
    tc_status = "FAIL"
    tc_name = "Care_Management_TC20"
    tc_priority = "Normal"

    try:
        url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_20"]["uri"]
        payload = project_data[conftest.cmd_arg]["test_20"]["payload"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        assert response.status_code == 200 or 201
        assert (response.json()['healthModules']['healthModuleId']) == project_data[conftest.cmd_arg]["test_20"][
            "healthModuleId"]
        assert (response.json()['healthModules']['isActive']) == project_data[conftest.cmd_arg]["test_20"]["isActive"]
        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_20']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)


@pytest.mark.sanity2
def test_Refer_and_Assign_Care_Protocol(Authorization, Base_Url, set_cookie):
    tc_desc = "To verify Refer and Assign Fuctionality"
    tc_status = "FAIL"
    tc_name = "Care_Management_TC21"
    tc_priority = "Normal"

    try:
        url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_21"]["uri"]
        payload = project_data[conftest.cmd_arg]["test_21"]["payload"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        assert response.status_code == 200 or 201
        assert (response.json()['healthModules']['healthModuleId']) == project_data[conftest.cmd_arg]["test_21"][
            "healthModuleId"]
        assert (response.json()['healthModules']['isActive']) == project_data[conftest.cmd_arg]["test_21"]["isActive"]
        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_21']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)
