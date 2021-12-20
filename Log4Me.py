##############
#LOG4ME
#EDUCATIONAL PURPOSES ONLY
#DONT DO ILLEGAL SHIT
#Dan, comment this shit when you get a chance pls
##############

import os
from git import Repo

downloaded = False

#get latest edition of marshalsec

Repo.clone_from("https://github.com/mbechler/marshalsec","./marshalsec")

#check to validate that marshalsec was cloned successfully

dirlist = os.listdir("./")

for i in dirlist:
    if i != "marshalsec-master":
        downloaded = False
        break
    else:
        downloaded = True
        print("Marshalsec downloaded!")
        continue

if downloaded == False:
    print("Marshalsec was not downloaded successfully, or the permissions in this directory are not configured "
          "correctly. Please download it manually from http://https://github.com/mbechler/marshalsec , or check your "
          "permissions.")
    exit(69)
#Script to get maven if not installed already, and then
def buildMSec():
    print("Checking for maven... ")
    os.system("sudo apt-get update")
    stream = os.popen("sudo apt-get install maven")
    print(stream.read())
    os.system("cd marshalsec-master")
    print("Building...")
    buildresult = os.system("mvn clean package -DskipTests")
    if buildresult != 0:
        print("Something went wrong when building marshalsec. Try again or manually build using mvn clean package "
              "-DskipTests when in the marshalsec-master directory.")
    else:
        print("Marshalsec built.")
def getInfo():
    global ip
    global port
    valid = False
    while valid == False:
        ip = input("Please enter the ip address of the target.")
        port = input("Please enter the port if known. (default 80)")

        if port != 80:
            if port >> 99999 or port.isdigit() == False:
                print("Invalid port specification. Defaulting to 80.")
                port = 80
        else:
            port = port


#TODO COMMENT YA DAMN CODE

#TODO Finish input system (make it a bit better maybe)

#TODO Check for marshalsec if its already built

#TODO Add compiler for the java file, would also be nice to have it auto generate the exploit for you

#TODO Spin up http server for hosting the exploit

#TODO Find a way to make the netcat listener spawn in the same shell window as this script

#TODO die maybe






