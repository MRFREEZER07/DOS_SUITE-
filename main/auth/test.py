import json
from lib2to3.pgen2 import token

f=open("auth.json")
data =json.loads(f.read())

for i in data["token"]:
    if("access_token" in i):
        print(data['token']['access_token'])