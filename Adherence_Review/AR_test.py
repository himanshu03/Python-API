import json
import pytest
import requests
import yaml
from numpy.random.mtrand import randint

import conftest

with open("Adherence_Review/adherence_review_common.yml", "r") as common:
	test_data = yaml.load(common)

with open("Adherence_Review/adherence_review_project.yml", "r") as project:
	project_data = yaml.load(project)

with open('Adherence_Review/adherence_review_expected.json') as json_file:
	expected_json = json.load(json_file)


def test_navigation_to_Adherence_reviews(Authorization, Base_Url,set_cookie):
	tc_desc = "To verify the navigation to Adherence reviews"
	tc_status = "FAIL"
	tc_name = "Adherence_Review_TC01"
	tc_priority = "High"

	try:
		url = Base_Url +  project_data[conftest.cmd_arg]["test_01"]
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


