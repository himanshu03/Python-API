import json
import pytest
import requests
import yaml
from numpy.random.mtrand import randint

import conftest

with open("Ymls/assessment_common.yml", "r") as common:
    test_data = yaml.load(common)

with open("Ymls/assessment_project.yml", "r") as project:
    project_data = yaml.load(project)


@pytest.mark.sanity
def test_Export_Assessment(Authorization, Base_Url, set_cookie):
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
def test_Assessment_Date(Authorization, Base_Url, set_cookie):
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
        assert str(response.json()['completedOn']).__contains__(
            project_data[conftest.cmd_arg]["test_02"]['completedOn'])
        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_02']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)


@pytest.mark.sanity
def test_Search_Assessment(Authorization, Base_Url, set_cookie):
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


@pytest.mark.sanity
def test_Worklist_04(Authorization, Base_Url, set_cookie):
    tc_desc = "Verify the In Progress Tab"
    tc_status = "FAIL"
    tc_name = "Worklist_TC04"
    tc_priority = "High"

    try:
        url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_04"]["uri"]
        print(url)
        payload = project_data[conftest.cmd_arg]["test_04"]["payload"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        json_data = response.json()
        ids = []
        ids1 = []
        for data in json_data["data"]:
            output = (data['assessmentId'])
            output1 = (data['assignmentId'])
            ids.append(output)
            ids1.append(output1)
        print("Assessment ids are:", ids)
        print("Assignment ids are", ids1)
        print("Length of assessment id are", len(ids))

        assert response.status_code == 200

        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_04']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)


@pytest.mark.sanity
def test_Worklist_05(Authorization, Base_Url, set_cookie):
    tc_desc = "Verify the Complete Tab under Assessment"
    tc_status = "FAIL"
    tc_name = "Worklist_TC05"
    tc_priority = "High"

    try:
        url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_05"]["uri"]
        print(url)
        payload = project_data[conftest.cmd_arg]["test_05"]["payload"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        json_data = response.json()
        ids = []
        ids1 = []
        for data in json_data["data"]:
            output = (data['assessmentId'])
            output1 = (data['assignmentId'])
            ids.append(output)
            ids1.append(output1)
        print("Assessment ids are:", ids)
        print("Assignment ids are", ids1)
        print("Length of assessment id are", len(ids))

        assert response.status_code == 200
        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_05']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)


@pytest.mark.sanity
def test_Worklist_06(Authorization, Base_Url, set_cookie):
    tc_desc = "Verify User is able to discard Assessment"
    tc_status = "FAIL"
    tc_name = "Worklist_TC06"
    tc_priority = "High"

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
        json_data = response.json()
        ids = []
        ids1 = []
        for data in json_data["data"]:
            output = (data['assessmentId'])
            output1 = (data['assignmentId'])
            ids.append(output)
            ids1.append(output1)
        print("Assessment ids are:", ids)
        print("Assignment ids are", ids1)
        print("Length of assessment id are", len(ids))

        url_1 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_06"]["uri1"] + ids1[0]
        print(url_1)
        payload_1 = {}
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_1 = requests.request("DELETE", url_1, headers=headers, data=payload_1)
        assert response.status_code == 200
        assert response_1.status_code == 200

        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_06']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)


@pytest.mark.sanity
def test_Worklist_07(Authorization, Base_Url, set_cookie):
    tc_desc = "Verify Discard functionality of new Assessment"
    tc_status = "FAIL"
    tc_name = "Worklist_TC07"
    tc_priority = "High"

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
        json_data = response.json()
        assignmentId = json_data['assignmentId']

        url_1 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_07"]["uri1"] + assignmentId
        print(url_1)
        payload_1 = {}
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_1 = requests.request("DELETE", url_1, headers=headers, data=payload_1)
        assert response.status_code == 200
        assert response_1.status_code == 200

        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_07']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)
