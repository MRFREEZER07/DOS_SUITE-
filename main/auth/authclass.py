import requests
import os
import subprocess
import datetime
import dateutil.relativedelta
import time



class Auth():
    
    def login(self,username,password):
        url = "https://kbgrunt.selfmade.lol/api/auth/login?username={}&password={}".format(username,password)
        payload={}
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload)
        pwd=os.getcwd()
        #print(pwd)
        with open(pwd +"/auth/auth.json",'w') as f:
            f.write(str(response.text))


    def refresh(self,refreshToken):
        url = "https://kbgrunt.selfmade.lol/api/auth/refresh?refresh_token={}".format(refreshToken)
        payload={}
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload)
        pwd=os.getcwd()
        #print(pwd)
        with open(pwd +"/auth/auth.json",'w') as f:
            f.write(str(response.text))


    def isAuthenticated(self):
        if(self.verifyTime()):
            return True
        else:
            return False

    def getLastUpdatedTime(self):
        pwd=os.getcwd()
        #print(pwd)
        modTime = os.path.getmtime(pwd+"/auth/auth.json")
        return modTime

    def timeDifference(self,d1,d2):

        dt1 = datetime.datetime.fromtimestamp(d1) # 1973-11-29 22:33:09
        dt2 = datetime.datetime.fromtimestamp(d2) # 1977-06-07 23:44:50
        rd = dateutil.relativedelta.relativedelta (dt2, dt1)
        return rd


    def epochTimeToNormal(self,time):
        value = datetime.datetime.fromtimestamp(time)
        return value.strftime('%Y-%m-%d %H:%M:%S')

    def verifyTime(self):
        createdTime = self.getLastUpdatedTime()
        currentTime = time.time()
        difference = self.timeDifference(createdTime,currentTime)
        if(difference.years>0 or difference.months>0 or difference.hours>0 or difference.minutes>30 ):
            print("token Expired relogin")
            return False
        else:
            return True
