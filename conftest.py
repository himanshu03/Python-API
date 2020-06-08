import json
import os
from datetime import datetime

import pandas as pd
import pytest
import requests
import sqlalchemy as sqlalchemy
import time

rs_session = 'global'
conf = 'global'
now = datetime.now()
ts = now.strftime("%d/%m/%Y %H:%M:%S")
module_name = 'global'
cmd_arg = 'global'
option = None
start_time = 'global'

@pytest.fixture
def Authorization(scope='session'):
    global rs_session
    global conf
    global ts
    global module_name
    global cmd_arg
    global start_time

    start_time = time.time()

    with open(os.getcwd() + "/infra.conf") as config_file:
        config_file.seek(0)
        conf = json.load(config_file)

    cmd_arg = option.arg
    url = conf[cmd_arg]["authurl"]
    module_name = conf[cmd_arg]["module_name"]
    payload = conf[cmd_arg]["payload"]

    # TODO: Integrate with decrypt JSON code
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    token = response.json()["token"]
    Authorization = "a " + token

    #Redshift details
    user = conf[cmd_arg]["redshift"]["user"]
    password = conf[cmd_arg]["redshift"]["password"]
    db = conf[cmd_arg]["redshift"]["db"]
    host = conf[cmd_arg]["redshift"]["host"]
    port = conf[cmd_arg]["redshift"]["port"]
    engine = sqlalchemy.create_engine(
        'postgres://' + user + ':' + password + '@' + host + ':' + port + '/'
        + db)
    rs_session = engine.connect()
    print("RS Connection successful")

    return Authorization


@pytest.fixture
def Base_Url():
    Base_Url = conf[cmd_arg]["baseurl"]
    return Base_Url


#Script for updating DB
def updatedb(tc_name,tc_desc, tc_status):
    _sql = "INSERT INTO test_api_automation_qa (module_name, tc_name,tc_desc,tc_status,time_of_execution, time_duration) VALUES " \
           "('{}', '{}','{}', '{}','{}', '{}');".format(module_name, tc_name,tc_desc,tc_status,ts, time.time() - start_time)
    print("SQL:- {} \n".format(_sql))
    try:
        pd.read_sql_query(_sql, rs_session)
    except:
        print(tc_desc+" DB Status Updated")

#Scripts for passing arguments
def pytest_addoption(parser):
    parser.addoption("--arg", action="store", default="Orlando", help="Option for making some stuff")

def pytest_configure(config):
    global option
    option = config.option


