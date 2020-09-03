import json

import pytest
import requests
import yaml

import conftest

test_data_zip_codes = [
    ("us", "90210", "Beverly Hills"),
    ("ca", "B2A", "North Sydney South Central"),
    ("it", "50123", "Firenze")
]

@pytest.mark.skip
@pytest.mark.parametrize("country_code, zip_code, expected_place_name", test_data_zip_codes)
def test_using_test_data_object_get_location_data_check_place_name(country_code, zip_code, expected_place_name):
    response = requests.get(f"http://api.zippopotam.us/{country_code}/{zip_code}")
    print(response)
    response_body = response.json()
    assert response_body["places"][0]["place name"] == expected_place_name


with open("/Users/it000621/PycharmProjects/incareapisautomation/Ymls/worklist_common.yml", "r") as common:
    test_data = yaml.load(common)

with open("/Users/it000621/PycharmProjects/incareapisautomation/Ymls/worklist_project.yml", "r") as project:
    project_data = yaml.load(project)


def test_Worklist_14(Authorization, Base_Url, set_cookie):
    tc_desc = "Verify the sorting on Insurance"
    tc_status = "FAIL"
    tc_name = "Worklist_TC14"
    tc_priority = "High"

    try:
        url = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_31"]["uri"]
        print(url)
        payload = project_data[conftest.cmd_arg]["test_31"]["payload"]
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json',
            'Cookie': set_cookie
        }
        response = requests.request("POST", url, headers=headers, data=payload,verify=False)
        json_data = response.json()
        ids = []
        for data in json_data["data"]:
            output = (data['id'])
            ids.append(output)
        print(ids)

        url_1 = Base_Url + test_data['test_care'] + project_data[conftest.cmd_arg]["test_31"][
            "payload1"]+ +id+"_test"
        url_2 = Base_Url + test_data['test_care'] + "/users/c8221e60-ff0f-443b-acf8-2761cb45fd96/referrals/" + id + "_test"
        print(url_1)
        payload_1 = project_data[conftest.cmd_arg]["test_31"]["payload1"]
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
        print(test_data['test_16']['message'])
