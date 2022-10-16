#!/bin/python3


import auth.authclass as auth1
import libs.Apicalls as api1

print("""██████╗  ██████╗ ███████╗    ███████╗██╗   ██╗██╗████████╗███████╗
██╔══██╗██╔═══██╗██╔════╝    ██╔════╝██║   ██║██║╚══██╔══╝██╔════╝
██║  ██║██║   ██║███████╗    ███████╗██║   ██║██║   ██║   █████╗  
██║  ██║██║   ██║╚════██║    ╚════██║██║   ██║██║   ██║   ██╔══╝  
██████╔╝╚██████╔╝███████║    ███████║╚██████╔╝██║   ██║   ███████╗
╚═════╝  ╚═════╝ ╚══════╝    ╚══════╝ ╚═════╝ ╚═╝   ╚═╝   ╚══════╝
                                                                    """)
print(""" ----commands-----
      [+] login

      [+] attack 
      """)

commands =["login","attack"]
command =""

#input segement
while True:
        command = input("ENTER THE COMMAND-->")
        if command in commands:
            command = command
            break





auth = auth1.Auth()
if(command=="login"):
    username =input("ENTER USERNAME -->")
    password =input("ENTER YOUR PASSWORD -->")
    
    auth.login(username,password)

if(command =="attack"):
    if(auth.isAuthenticated()):
        print("authenticated......")
        api=api1.Apicall()
        op =api.availableAttack()
        print("Sites To Attack")
        for sites in op:
            print('[-]'+sites)
        while True:
            target = input("ENTER THE SITE TO ATTACK -->")
            if(target not in op):
                print("Target no in list , if you want to attack a new site ,make a attack request in out site")
            else:
                break
    
        threads =input("ENTER NUMBER OF THREADS TO ATTACK -->")
        proxyNeed = input("DO U WANT TO USE PROXY (yes or no) -->")
        auth =auth1.Auth()
        if(proxyNeed == "yes"):
            if(auth.isAuthenticated()):
                #dos script with proxy
                pass
            else:
                print("you need to login before ur going to attack")

        if(proxyNeed =="no"):
            if(auth.isAuthenticated()):
                #dos script without proxy
                pass
            else:
                print("you need to login before ur going to attack")
    else:
        print("you need to login before ur going to attack")