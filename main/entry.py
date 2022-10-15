#!/bin/python3


import auth.authclass as auth1


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
            print(command)
            break





auth = auth1.Auth()
if(command=="login"):
    username =input("ENTER USERNAME -->")
    password =input("ENTER YOUR PASSWORD -->")
    
    auth.login(username,password)

if(command =="attack"):
    if(auth.isAuthenticated()):
        print("authenticated......")
        target = input("ENTER THE SITE TO ATTACK -->")
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