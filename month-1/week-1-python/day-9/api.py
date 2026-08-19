#API- application programming interface.
#Can refer to python files or folders but they in general refere to third party services that we can write code talk to.Many API live on internet these days
#Requests- popular package in python can be installed via pip and is used for using api in python or to make web requests
#json --> javascript object notation(text based format)
import json
import requests
import sys
if len(sys.argv)!=2:
    sys.exit()
response=requests.get("https://itunes.apple.com/search?entity=songs&limit=1&term="+sys.argv[1])
#print(json.dumps(response.json(),indent=2))
o=response.json()
for result in o["result"]:
    print(result["trackname"])
