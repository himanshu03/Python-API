import json
import os
import logging
import time
from datetime import datetime

import pandas as pd
import pytest
import requests
import sqlalchemy

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
    # print("RS Connection successful")

    return Authorization


@pytest.fixture
def Base_Url():
    Base_Url = conf[cmd_arg]["baseurl"]
    return Base_Url

@pytest.fixture
def set_cookie(scope='session'):
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
    set_cookie = response.headers.get('set-cookie').split(';')[0]
    return set_cookie

#Script for updating DB
def updatedb(tc_name,tc_desc, tc_status, tc_priority):
    _sql = "INSERT INTO iq.test_api_automation_qa (module_name, tc_name,tc_desc,tc_status,time_of_execution, time_duration, priority) VALUES " \
           "('{}', '{}','{}', '{}', '{}', '{}', '{}');".format(module_name, tc_name,tc_desc,tc_status,ts, round(time.time() - start_time, 4), tc_priority)
    # print("SQL:- {} \n".format(_sql))
    try:
        pd.read_sql_query(_sql, rs_session)
    except:
        print("\n")


#Scripts for passing arguments
def pytest_addoption(parser):
    parser.addoption("--arg", action="store", default="Orlando", help="Option for making some stuff")

def pytest_configure(config):
    global option
    option = config.option

def init_logging():
    logfile_path = os.getcwd()+"/Logs/log_file.log"
    logging.basicConfig(filename=logfile_path,
                        format='%(levelname)s %(asctime)s %(message)s',
                        filemode='w')
    # Creating an object
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.info("Info Logs ")
    return logger

def pytest_sessionfinish(session, exitstatus):
    with open('Logs/log_file.log', 'r') as file:
        logs = file.read().replace('\\n', '\n')

    result = logs.find("collecting")
    text = logs[result:-1]

    url = conf[cmd_arg]["chat_url"]
    data_payload = {
        "text": text
    }
    data_payload = json.dumps(data_payload)
    headers = {'Content-Type': 'application/json'}
    requests.post(url, headers=headers, data=data_payload)
    print('script end')





