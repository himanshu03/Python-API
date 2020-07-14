import json
import logging
import math
import os
import random
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
set_cookie = 'global'
payload = 'global'

@pytest.fixture
def Authorization(request, scope='session'):
    global rs_session
    global conf
    global ts
    global module_name
    global cmd_arg
    global start_time
    global set_cookie
    global payload

    start_time = time.time()

    with open(os.getcwd() + "/infra.conf") as config_file:
        config_file.seek(0)
        conf = json.load(config_file)

    cmd_arg = option.arg
    url = conf[cmd_arg]["authurl"]
    module_name = conf[cmd_arg]["module_name"]
    try:
        data_payload = encrypt_json({"email":conf[cmd_arg][request.param]["user_name"],"password": conf[cmd_arg][request.param]["pwd"]})
        payload = json.dumps(data_payload)
    except:
        data_payload = encrypt_json({"email": conf[cmd_arg]["user_name"], "password": conf[cmd_arg]["pwd"]})
        payload = json.dumps(data_payload)

    # TODO: Integrate with decrypt JSON code
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    token = response.json()["token"]
    Authorization = "a " + token

    set_cookie = response.headers.get('set-cookie').split(';')[0]

    # Redshift details
    user = conf[cmd_arg]["redshift"]["user"]
    password = conf[cmd_arg]["redshift"]["pwd"]
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
    try:
        pd.read_sql_query(_sql, rs_session)
    except:
        print("\n")

#Scripts for passing arguments
def pytest_addoption(parser):
    parser.addoption("--arg", action="store", default="Complete_Health", help="Option for making some stuff")

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

#Script for connection with ES and sql query execution
def execute_sql_query(sqlstring):
    try:
        url = "http://10.7.6.85:9200/_sql"
        payload = sqlstring
        headers = {
            'Content-Type': 'text/plain'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        assert response.status_code == 200
        return response.json()
    except Exception as e:
        raise
    finally:
        print("End")


#Script for converting credentials to hexadecimal
def encrypt_value(decrypted_value):
  random_number = math.floor(random.uniform(0, 1) * 89) + 10
  x = []
  for each_char in decrypted_value:
    char_to_ascii = ord(each_char)
    salted_ascii = char_to_ascii + int(random_number)
    ascii_to_hex = hex(salted_ascii)[2:]
    x.append(ascii_to_hex)
  x.append(int(random_number))
  final_value = ':'.join(str(y) for y in x)
  return final_value

def encrypt_json(decrypted_json):
  final_json = {}
  for each_key in decrypted_json:
    final_json.update({
      encrypt_value(each_key): encrypt_value(decrypted_json[each_key])
    })
  return final_json

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

