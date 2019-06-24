#Python Code to run an as3 declaration
#
import requests
import os
from requests.auth import HTTPBasicAuth

# Get rid of annoying insecure requests waring
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Declaration location
GITDRC = 'https://raw.githubusercontent.com/RuncibleSpoon/as3/master/declarations/payload.json'
IP = 'bigip.example.com'
#IP = '10.1.10.89'
PORT = '8443'
USER = 'admin'
PASS = os.environ['BIGPASS']
URLBASE = 'https://' + IP + ':' + PORT
TESTPATH = '/mgmt/shared/appsvcs/info'
AS3PATH = '/mgmt/shared/appsvcs/declare'

print("########### Fetching Declaration ###########")
d = requests.get(GITDRC)

# Check we have connectivity and AS3 is installed
print('########### Checking that AS3 is running on ', IP ,' #########')
url = URLBASE + TESTPATH

r = requests.get(url, auth=HTTPBasicAuth(USER, PASS), verify=False)



if r.status_code == 200:
   data = r.json()
   if data["version"]:
      print('AS3 version is ', data["version"])
      print('########## Runnig Declaration #############')
      url = URLBASE + AS3PATH
      headers = { 'content-type': 'application/json',
              'accept': 'application/json' }
      r = requests.post(url, auth=HTTPBasicAuth(USER, PASS), verify=False,
         data=d.text, headers=headers)
      print('Status Code:', r.status_code,'\n', r.text)
   else:
      print('AS3 test to ',IP, 'failed: ', r.text)
