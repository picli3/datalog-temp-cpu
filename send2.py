import json
import requests
import time

f = requests.Session()

URL = 'https://firestore.googleapis.com/v1/projects/test-maykol-1/databases/(default)/documents/datos'
headers = {'content-type': 'application/json'}

while(1):
	file = open("/sys/class/hwmon/hwmon0/temp1_input", "r")
	temp=float(file.read())/1000

	now =time.time()

	my_data = { 
  		"fields": { 
                	"data": { "stringValue": str(temp) },
			"fecha":{ "stringValue": str(now) }
            		}
        	}

	get_data = f.post(URL, data=json.dumps(my_data), timeout=30, headers=headers, verify=False)
	print(get_data.text)
	time.sleep(60)

