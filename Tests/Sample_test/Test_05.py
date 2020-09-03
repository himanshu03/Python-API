import json
import pytest
import requests
import yaml
from numpy.random.mtrand import randint
import jsonpath

import conftest

with open("/Users/it000621/PycharmProjects/incareapisautomation/Ymls/worklist_common.yml", "r") as common:
    test_data = yaml.load(common)

with open("/Users/it000621/PycharmProjects/incareapisautomation/Ymls/worklist_project.yml", "r") as project:
    project_data = yaml.load(project)


