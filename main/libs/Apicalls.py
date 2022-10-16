import json
import requests
import os

from urllib3 import Retry
class Apicall():
    #parse json and set barer token
    def __init__(self):
        pwd=os.getcwd()
        #print(pwd) 
        f=open(pwd+"/auth/auth.json")
        data =json.loads(f.read())
        for i in data["token"]:
            if("access_token" in i):
                self.barerToken = data['token']['access_token']
                


    def startingAttack(self,):
        #add in request api
        pass


    def afterAttack(self,):
        pass

    def getAllOnGoingAttacks(self):
        onGoingAttackList =[]
        url = "https://kbgrunt.selfmade.lol/api/func/viewongoingattack"
        payload={}
        files={}
        headers = {
        'Authorization':"Bearer "+ self.barerToken,
        'Content-Type': 'application/json',
         'Accept':'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=json.dumps(payload), files=files)
        resjson =response.json()
        for unpackjson in resjson["ongoing attacks"]:
            onGoingAttackList.append(unpackjson['target'])
            
        return onGoingAttackList


    def getAllRequestedAttacks(self):
        requestedAttacks=[]
        url = "https://kbgrunt.selfmade.lol/api/func/viewrequestedattack"
        payload={}
        files={}
        headers = {
        'Authorization':"Bearer "+ self.barerToken,
        'Content-Type': 'application/json',
         'Accept':'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=json.dumps(payload), files=files)
        resjson =response.json()
        for unpackjson in resjson["requested attacks"]:
            requestedAttacks.append(unpackjson['target'])
            
        return requestedAttacks

    def availableAttack(self):
        finalList =[]
        ongoingAttacks =self.getAllOnGoingAttacks()
        requestedAttacks =self.getAllRequestedAttacks()
        return set(ongoingAttacks+requestedAttacks)

    def appendToOngoingList(self):
        pass