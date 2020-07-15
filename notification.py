import json
import os
import sys

import requests

with open(os.getcwd() + "/infra.conf") as config_file:
    config_file.seek(0)
    conf = json.load(config_file)

with open('Logs/log_file.log', 'r') as file:
    logs = file.read().replace('\\n','\n')

result = logs.find("collecting")

text = logs[result:-1]

url= conf[sys.argv[1]]["chat_url"]
payload = {
        "text":text
      }

payload=json.dumps(payload)
headers={'Content-Type':'application/json'}
response=requests.post(url,headers=headers,data=payload)
print('\nscript end')
