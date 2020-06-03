import json
import os
import pytest
import pandas as pd
import requests
import sqlalchemy as sqlalchemy
import datetime
from datetime import datetime

rs_session = 'global'
conf = 'global'
now = datetime.now()
ts = now.strftime("%d/%m/%Y %H:%M:%S")
module_name = 'global'

@pytest.fixture
def Authorization():
    global rs_session
    global conf
    global ts
    global module_name

    with open(os.getcwd() + "/infra.conf") as config_file:
        config_file.seek(0)
        conf = json.load(config_file)

    url = conf["authurl"]
    module_name = conf["module_name"]
    payload = "{\"bc:ba:cd:be:c0:c8:cb:d2:89\":\"c2:c7:c7:c8:cf:ba:bc:bc:be:cb:89\",\"be:c6:ba:c2:c5:89\":\"c6:ba:c6:cd:ba:87:c0:c2:cb:c2:84:8e:99:c2:c7:c7:c8:cf:ba:bc:bc:be:cb:87:bc:c8:c6:89\",\"c9:ba:cc:cc:d0:c8:cb:bd:89\":\"9d:c2:cc:c1:99:8a:8b:8c:89\",\"cc:c8:ce:cb:bc:be:89\":\"c2:c7:c7:c8:cf:ba:bc:bc:be:cb:89\"}"
    # TODO: Integrate with decrypt JSON code
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    token = response.json()["token"]
    Authorization = "a " + token

    # Redshift details
    user = conf["redshift"]["user"]
    password = conf["redshift"]["password"]
    db = conf["redshift"]["db"]
    host = conf["redshift"]["host"]
    port = conf["redshift"]["port"]
    engine = sqlalchemy.create_engine(
        'postgres://' + user + ':' + password + '@' + host + ':' + port + '/'
        + db)
    rs_session = engine.connect()
    print("RS Connection successful")

    return Authorization


@pytest.fixture
def Base_Url():
    Base_Url = conf["baseurl"]
    return Base_Url


def updatedb(tc_name,tc_desc, tc_status):
    _sql = "INSERT INTO test_api_automation_qa (module_name, tc_name,tc_desc,tc_status,time_of_execution) VALUES " \
           "('{}', '{}','{}', '{}','{}');".format(module_name, tc_name,tc_desc,tc_status,ts)
    print("SQL:- {} \n".format(_sql))
    try:
        pd.read_sql_query(_sql, rs_session)
    except:
        print(tc_desc+" DB Status Updated")
