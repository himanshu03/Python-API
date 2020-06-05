import pytest
import requests
from numpy.random.mtrand import randint

import conftest

role_id = 'global'
group_id = 'global'



def test_incare_01_Assess_p1(Authorization, Base_Url):
	tc_desc = "Get Total Assessments count for a user"
	tc_status = "FAIL"
	tc_name = "TC01"
	print(tc_desc + " is Executing")
	try:
		url = Base_Url + "incare/assessment/patients/P2913414/assessments/_count"
		payload = {}
		headers = {
			'Authorization': Authorization
		}
		response = requests.request("GET", url, headers=headers, data=payload)
		assert response.status_code == 200 , "No assessment is found on this user"
		print(response.json())
		tc_status = "PASS"
	except Exception as e:
		tc_status = "FAIL"
		print(e)
		raise
	finally:
		print(tc_desc + "Status:- " + tc_status)
		conftest.updatedb(tc_name, tc_desc, tc_status)


def test_incare_02_Assess_p1(Authorization, Base_Url):
	tc_desc = "fetch summary of assessments attempted by patient"
	tc_status = "FAIL"
	tc_name = "TC02"
	print(tc_desc + " is Executing")
	try:
		url = Base_Url + "incare/assessment/patients/P2913414/assessments/5e97fb4f7f9b710a5cab6b4e/_summary"
		payload = {}
		headers = {
			'Authorization': Authorization
		}
		response = requests.request("GET", url, headers=headers, data=payload)
		assert response.status_code == 200, "No assessments attempted by patient"
		tc_status = "PASS"
	except Exception as e:
		tc_status = "FAIL"
		print(e)
		raise
	finally:
		print(tc_desc + "Status:- " + tc_status)
		conftest.updatedb(tc_name, tc_desc, tc_status)


def test_incare_03_Assess_p1(Authorization, Base_Url):
    tc_desc = "Get completed Assessments count for a user"
    tc_status = "FAIL"
    tc_name = "TC03"
    print(tc_desc + " is Executing")
    try:
        url = Base_Url + "incare/assessment/patients/P2913414/assessments/_count"
        payload = {}
        headers = {
            'Authorization': Authorization
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        assert response.status_code == 200, "No assessment is found on this user"
        print(response.json())
        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(e)
        raise
    finally:
        print(tc_desc + "Status:- " + tc_status)
        conftest.updatedb(tc_name, tc_desc, tc_status)


def test_incare_04_Assess_p1(Authorization, Base_Url):
    tc_desc = "summary of all the corresponding assessments completed by patient"
    tc_status = "FAIL"
    tc_name = "TC04"
    print(tc_desc + " is Executing")
    try:
        url = Base_Url + "incare/assessment/patients/P2913414/assessments/5e78bae37f9b715b42129f19/_fetch"
        payload = {}
        headers = {
            'Authorization': Authorization
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        assert response.status_code == 200, "No assessments attempted by patient"
        tc_status = "PASS"
    except Exception as e:
        tc_status = "FAIL"
        print(e)
        raise
    finally:
        print(tc_desc + "Status:- " + tc_status)
        conftest.updatedb(tc_name, tc_desc, tc_status)

def test_incare_05_Assess_p1(Authorization, Base_Url):
        tc_desc = "Get Total Assessments count for a user"
        tc_status = "FAIL"
        tc_name = "TC05"
        print(tc_desc + " is Executing")
        try:
            url = Base_Url + "incare/assessment/patients/P2913414/assessments/_count"
            payload = {}
            headers = {
                'Authorization': Authorization
            }
            response = requests.request("GET", url, headers=headers, data=payload)
            assert response.status_code == 200, "No assessment is found on this user"
            print(response.json())
            tc_status = "PASS"
        except Exception as e:
            tc_status = "FAIL"
            print(e)
            raise
        finally:
            print(tc_desc + "Status:- " + tc_status)
            conftest.updatedb(tc_name, tc_desc, tc_status)






