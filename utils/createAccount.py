#Used to create acounts, ie, check if they allready exist, and then add them to the csv 

import hashlib, verifyLogin

#checkUser takes the wanted username (wUser), and checks if the wUSer allready exists in the dictonary of existing users, created by bringAccounts in verifyLogin.py
#returns false if the username is taken, true otherwise

def checkUser(wUser):
    accounts = verifyLogin.bringAccounts()
    if(wUser in accounts):
        return False
    return True
    
#makeAccounts, takes a list, with wanted Username in he first field, and the wanted password in the secondfield. The fxn assumes that the username is not taken, see checkUser. The fxn hashes the password, and writes out to passwords.csv

def makeAccount(info = []): #info should be 2 fields, username, password
    accounts = verifyLogin.bringAccounts()
    file = open("data/accounts.csv", "a")
    username = info[0]
    password = info[1]
    if("," in info[0]):
        username = '"'+info[0]+'"'
    outString = "\n"+username+","+password
    file.write(outString)
    file.close()  
    return True
