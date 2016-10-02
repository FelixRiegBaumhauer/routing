#everything concerning the verifying of logins is done here
import hashlib

#bringAccounts, brings you the accounts in a dictionary.
#the accounts are read in from passwords.csv, and are edited as needed
def bringAccounts():
    
    file = open("data/accounts.csv", "r")
    inputString = file.read()
    brokenString = str.split(inputString, "\n")
    accounts = {}
    
    for line in brokenString:
        username = ""
        password = ""
        if(line[0] == '"'):
            line = line[1:]
            run = len(line)-1
            while (run>=0):
                if(line[run] == '"'):
                    username = line[:run]
                    password = line[run+2:]
                    run = 0              
                    accounts[username] = password
                run-=1
        else:
            pos = line.index(",")
            username = line[:pos]
            password = line[pos+1:]
            accounts[username] = password

    file.close
    return accounts


    
    

