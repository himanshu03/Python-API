import pytest
import requests
import yaml

import conftest

with open("/Users/it000621/PycharmProjects/incareapisautomation/Ymls/assessment_common.yml", "r") as common:
    test_data = yaml.load(common)

with open("/Users/it000621/PycharmProjects/incareapisautomation/Ymls/assessment_project.yml", "r") as project:
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
def test_Assessment_04(Authorization, Base_Url, set_cookie):
    tc_desc = "Verify the In Progress Tab"
    tc_status = "FAIL"
    tc_name = "Assessment_TC04"
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
def test_Assessment_05(Authorization, Base_Url, set_cookie):
    tc_desc = "Verify the Complete Tab under Assessment"
    tc_status = "FAIL"
    tc_name = "Assessment_TC05"
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
def test_Assessment_06(Authorization, Base_Url, set_cookie):
    tc_desc = "Verify User is able to discard Assessment"
    tc_status = "FAIL"
    tc_name = "Assessment_TC06"
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
def test_Assessment_07(Authorization, Base_Url, set_cookie):
    tc_desc = "Verify Discard functionality of new Assessment"
    tc_status = "FAIL"
    tc_name = "Assessment_TC07"
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


@pytest.mark.sanity
def test_Assessment_08(Authorization, Base_Url, set_cookie):
    tc_desc = "Submit assessment without any response"
    tc_status = "FAIL"
    tc_name = "Assessment_TC08"
    tc_priority = "High"

    try:
        url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_08"]["uri"]
        print(url)
        payload = project_data[conftest.cmd_arg]["test_08"]["payload"]
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

        url_1 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_08"]["uri1"] + ids1[
            0] + "/_submit"
        print(url_1)
        payload_1 = project_data[conftest.cmd_arg]["test_08"]["payload1"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_1 = requests.request("POST", url_1, headers=headers, data=payload_1)
        assert response.status_code == 200
        assert response_1.status_code == 200

        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_08']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)


@pytest.mark.sanity
def test_Assessment_09(Authorization, Base_Url, set_cookie):
    tc_desc = "Submit assessment with invalid text"
    tc_status = "FAIL"
    tc_name = "Assessment_TC09"
    tc_priority = "High"

    try:
        url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_09"]["uri"]
        print(url)
        payload = project_data[conftest.cmd_arg]["test_09"]["payload"]
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

        url_1 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_09"]["uri1"] + ids1[
            0] + "/_submit"
        print(url_1)
        payload_1 = project_data[conftest.cmd_arg]["test_09"]["payload1"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_1 = requests.request("POST", url_1, headers=headers, data=payload_1)
        # print(response_1.json())
        assert response.status_code == 200
        assert response_1.status_code == 200

        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_09']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)


@pytest.mark.sanity
def test_Assessment_10(Authorization, Base_Url, set_cookie):
    tc_desc = "Verify after reassessing, all the previously selected option should get deleted"
    tc_status = "FAIL"
    tc_name = "Assessment_TC10"
    tc_priority = "High"

    try:
        url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_10"]["uri"]
        print(url)
        payload = project_data[conftest.cmd_arg]["test_10"]["payload"]
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
        print("Length of assignment id are", len(ids1))

        url_1 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_10"]["uri1"] + ids[
            0] + "/_fetch"
        print(url_1)
        payload_1 = {}
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_1 = requests.request("GET", url_1, headers=headers, data=payload_1)

        json_data1 = response_1.json()
        completed = []
        for data in json_data1["completed"]:
            output = (data['assignmentId'])
            completed.append(output)
        print("assignment ids are:", completed)
        print("Length of completed assignment id are", len(completed))

        ongoing = []
        for data in json_data1["ongoing"]:
            output = (data['assignmentId'])
            ongoing.append(output)
        print("assignment ids are:", ongoing)
        print("Length of ongoing assignment id are", len(ongoing))

        url_2 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_10"]["uri1"] + completed[
            0] + "/response"
        print(url_2)
        payload_2 = {}
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_2 = requests.request("GET", url_2, headers=headers, data=payload_2)
        print(response_2.json)

        url_3 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_10"]["uri2"]
        print(url_3)
        payload_3 = project_data[conftest.cmd_arg]["test_10"]["payload1"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_3 = requests.request("POST", url_3, headers=headers, data=payload_3)
        print(response_3.json())
        print(response_3.status_code)

        json_data3 = response_3.json()
        assignment3 = json_data3['assignmentId']

        url_4 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_10"]["uri1"] + assignment3 + \
                "/_submit"
        print(url_4)
        payload_4 = project_data[conftest.cmd_arg]["test_10"]["payload2"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_4 = requests.request("POST", url_4, headers=headers, data=payload_4)
        # print(response_4.json())
        print(response_4.status_code)

        # print(response_1.json())
        assert response.status_code == 200
        assert response_1.status_code == 200
        assert response_2.status_code == 200
        assert response_3.status_code == 200
        assert response_4.status_code == 200

        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_10']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)


@pytest.mark.sanity
def test_Assessment_11(Authorization, Base_Url, set_cookie):
    tc_desc = "To View and edit the saved assessment"
    tc_status = "FAIL"
    tc_name = "Assessment_TC11"
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
        print("Length of assignment id are", len(ids1))

        url_1 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_10"]["uri1"] + ids1[
            0] + "/response"
        print(url_1)
        payload_1 = {}
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_1 = requests.request("GET", url_1, headers=headers, data=payload_1)

        url_2 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_10"]["uri1"] + ids1[
            0] + "/_submit"
        print(url_2)
        payload_2 = project_data[conftest.cmd_arg]["test_11"]["payload1"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_2 = requests.request("POST", url_2, headers=headers, data=payload_2)

        assert response.status_code == 200
        assert response_1.status_code == 200
        assert response_2.status_code == 200

        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_11']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)


@pytest.mark.sanity
def test_Assessment_12(Authorization, Base_Url, set_cookie):
    tc_desc = "Verify the completed and In-progress section available under Assessment for every patient"
    tc_status = "FAIL"
    tc_name = "Assessment_TC12"
    tc_priority = "High"

    try:
        url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_12"]["uri"]
        print(url)
        payload = project_data[conftest.cmd_arg]["test_12"]["payload"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        json_data = response.json()
        ongoing_assessment = []
        ongoing_assignment = []
        for data in json_data["data"]:
            output = (data['assessmentId'])
            output1 = (data['assignmentId'])
            ongoing_assessment.append(output)
            ongoing_assignment.append(output1)
        print("Assessment ids are:", ongoing_assessment)
        print("Assignment ids are", ongoing_assignment)
        print("Length of ongoing assessment id are: ", len(ongoing_assessment))
        print("Length of ongoing assignment id are: ", len(ongoing_assignment))

        url_1 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_10"]["uri"]
        print(url_1)
        payload_1 = project_data[conftest.cmd_arg]["test_12"]["payload1"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_1 = requests.request("POST", url_1, headers=headers, data=payload_1)
        json_data1 = response_1.json()
        completed_assessment = []
        completed_assignment = []
        for data_1 in json_data1["data"]:
            output = (data_1['assessmentId'])
            output1 = (data_1['assignmentId'])
            completed_assessment.append(output)
            completed_assignment.append(output1)
        print("Assessment ids are:", completed_assessment)
        print("Assignment ids are", completed_assignment)
        print("Length of completed assessment id are: ", len(completed_assessment))
        print("Length of completed assignment id are: ", len(completed_assignment))

        assert response.status_code == 200
        assert response_1.status_code == 200

        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_12']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)


@pytest.mark.sanity
def test_Assessment_13(Authorization, Base_Url, set_cookie):
    tc_desc = "Create new assessment of type PHQ-9"
    tc_status = "FAIL"
    tc_name = "Assessment_TC13"
    tc_priority = "High"

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
        print(json_data)
        assert response.status_code == 200
        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_13']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)


@pytest.mark.sanity
def test_Assessment_14(Authorization, Base_Url, set_cookie):
    tc_desc = "Submit new assessment of type PHQ-9"
    tc_status = "FAIL"
    tc_name = "Assessment_TC14"
    tc_priority = "High"

    try:
        url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_14"]["uri"]
        print(url)
        payload = project_data[conftest.cmd_arg]["test_14"]["payload"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        json_data = response.json()
        assignment_id = json_data['assignmentId']

        url_1 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_14"]["uri1"] + assignment_id \
                + "/_submit"
        print(url_1)
        payload_1 = project_data[conftest.cmd_arg]["test_14"]["payload1"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_1 = requests.request("POST", url_1, headers=headers, data=payload_1)

        assert response.status_code == 200
        assert response_1.status_code == 200

        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_14']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)


@pytest.mark.sanity
def test_Assessment_15(Authorization, Base_Url, set_cookie):
    tc_desc = "Discard the assessment"
    tc_status = "FAIL"
    tc_name = "Assessment_TC15"
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
        json_data = response.json()
        assessment_id = []
        assignment_id = []
        for data in json_data["data"]:
            output = (data['assessmentId'])
            output1 = (data['assignmentId'])
            assessment_id.append(output)
            assignment_id.append(output1)
        print("Assessment ids are:", assessment_id)
        print("Assignment ids are", assignment_id)
        print("Length of assessment id are", len(assessment_id))
        print("Length of assignment id are", len(assignment_id))

        url_1 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_15"]["uri1"] + assignment_id[
            0] + "/response"
        print(url_1)
        payload_1 = {}
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_1 = requests.request("GET", url_1, headers=headers, data=payload_1)

        url_2 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_15"]["uri1"] + assignment_id[0]
        print(url_2)
        payload_2 = {}
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_2 = requests.request("DELETE", url_2, headers=headers, data=payload_2)

        assert response.status_code == 200
        assert response_1.status_code == 200
        assert response_2.status_code == 200

        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_15']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)


@pytest.mark.sanity
def test_Assessment_16(Authorization, Base_Url, set_cookie):
    tc_desc = "Switch the assessment"
    tc_status = "FAIL"
    tc_name = "Assessment_TC16"
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
        json_data = response.json()
        assessment_id = []
        assignment_id = []
        for data in json_data["data"]:
            output = (data['assessmentId'])
            output1 = (data['assignmentId'])
            assessment_id.append(output)
            assignment_id.append(output1)
        print("Assessment ids are:", assessment_id)
        print("Assignment ids are", assignment_id)
        print("Length of assessment id are", len(assessment_id))
        print("Length of assignment id are", len(assignment_id))

        url_1 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_16"]["uri1"] + assessment_id[
            0] + "/_fetch"
        print(url_1)
        payload_1 = {}
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_1 = requests.request("GET", url_1, headers=headers, data=payload_1)
        print("Response 1", response_1.status_code)

        url_2 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_16"]["uri1"] + \
                assignment_id[0] + "/response"
        print(url_2)
        payload_2 = {}
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_2 = requests.request("GET", url_2, headers=headers, data=payload_2)
        print("Response 2", response_2.status_code)

        url_3 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_16"]["uri1"] + assessment_id[
            1] + "/_fetch"
        print(url_3)
        payload_3 = {}
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_3 = requests.request("GET", url_3, headers=headers, data=payload_3)
        print("Response 3", response_3.status_code)

        url_4 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_16"]["uri1"] + \
                assignment_id[1] + "/response"
        print(url_4)
        payload_4 = {}
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_4 = requests.request("GET", url_4, headers=headers, data=payload_4)
        print("Response 4", response_4.status_code)

        url_5 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_16"]["uri1"] + assessment_id[
            2] + "/_fetch"
        print(url_5)
        payload_5 = {}
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_5 = requests.request("GET", url_5, headers=headers, data=payload_5)
        print("Response 5", response_5.status_code)

        url_6 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_16"]["uri1"] + \
                assignment_id[2] + "/response"
        print(url_6)
        payload_6 = {}
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_6 = requests.request("GET", url_6, headers=headers, data=payload_6)
        print("Response 6", response_6.status_code)

        url_7 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_16"]["uri1"] + assessment_id[
            3] + "/_fetch"
        print(url_7)
        payload_7 = {}
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_7 = requests.request("GET", url_7, headers=headers, data=payload_7)
        print("Response 7", response_5.status_code)

        url_8 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_16"]["uri1"] + \
                assignment_id[3] + "/response"
        print(url_8)
        payload_8 = {}
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_8 = requests.request("GET", url_8, headers=headers, data=payload_8)
        print("Response 8", response_8.status_code)

        assert response.status_code == 200
        assert response_1.status_code == 200
        assert response_2.status_code == 200
        assert response_3.status_code == 200
        assert response_4.status_code == 200
        assert response_5.status_code == 200
        assert response_6.status_code == 200
        assert response_7.status_code == 200
        assert response_8.status_code == 200

        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_16']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)


@pytest.mark.sanity
def test_Assessment_17(Authorization, Base_Url, set_cookie):
    tc_desc = "Submit new assessment of type PHQ-9"
    tc_status = "FAIL"
    tc_name = "Assessment_TC17"
    tc_priority = "High"

    try:
        url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_17"]["uri"]
        print(url)
        payload = project_data[conftest.cmd_arg]["test_17"]["payload"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print("Response1", response.json())
        print("Response 1", response.status_code)

        json_data = response.json()
        assignment_id = json_data['assignmentId']
        assessment_id = json_data['assessmentId']

        url_1 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_17"]["uri1"] + assignment_id \
                + "/_submit"
        print(url_1)
        payload_1 = project_data[conftest.cmd_arg]["test_17"]["payload1"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_1 = requests.request("POST", url_1, headers=headers, data=payload_1)
        print("Response 2", response_1.status_code)

        url_2 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_17"]["uri1"] + assessment_id \
                + "/_fetch"
        print(url_2)
        payload_2 = {}
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_2 = requests.request("GET", url_2, headers=headers, data=payload_2)
        print("Response 3", response_2.status_code)

        result = response_2.json()
        print("Score of a patient assessment is:", result['completed'][0]['summaryTypeList'][0]['score'])
        print("ScoreDeviation of a patient assessment is:", result['completed'][0]['summaryTypeList'][0][
            'scoreDeviation'])
        print("Total Score of a patient assessment is:", result['completed'][0]['summaryTypeList'][0]['totalScore'])
        print("Rating Display String of a patient assessment is:", result['completed'][0]['summaryTypeList'][0][
            'ratingDisplayString'])
        #################################################################################################################
        url_3 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_17"]["uri"]
        print(url_3)
        payload_3 = project_data[conftest.cmd_arg]["test_17"]["payload"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_3 = requests.request("POST", url_3, headers=headers, data=payload_3)
        print("Response4", response_3.json())
        print("Response 4", response_3.status_code)

        json_data_1 = response_3.json()
        assignment_id_1 = json_data_1['assignmentId']
        assessment_id_1 = json_data_1['assessmentId']

        url_4 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_17"]["uri1"] + \
                assignment_id_1 \
                + "/_submit"
        print(url_4)
        payload_4 = project_data[conftest.cmd_arg]["test_17"]["payload2"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_4 = requests.request("POST", url_4, headers=headers, data=payload_4)
        print("Response 4", response_4.status_code)

        url_5 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_17"]["uri1"] + \
                assessment_id_1 \
                + "/_fetch"
        print(url_5)
        payload_5 = {}
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response_5 = requests.request("GET", url_5, headers=headers, data=payload_5)
        print("Response 5", response_5.status_code)

        result1 = response_5.json()
        print("Score of a patient assessment is:", result1['completed'][0]['summaryTypeList'][0]['score'])
        print("ScoreDeviation of a patient assessment is:", result1['completed'][0]['summaryTypeList'][0][
            'scoreDeviation'])
        print("Total Score of a patient assessment is:", result1['completed'][0]['summaryTypeList'][0]['totalScore'])
        print("Rating Display String of a patient assessment is:", result1['completed'][0]['summaryTypeList'][0][
            'ratingDisplayString'])

        assert response.status_code == 200
        assert response_1.status_code == 200
        assert response_2.status_code == 200
        assert response_3.status_code == 200
        assert response_4.status_code == 200
        assert response_5.status_code == 200

        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(test_data['test_17']['message'])
        raise
    finally:
        conftest.updatedb(tc_name, tc_desc, tc_status, tc_priority)
