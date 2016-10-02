

def bringAccounts():

    file = open("data/passwords.csv", "r")
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

#returns a bool, True if your account was made, False if not
def makeAccount(info = []): #info should be 2 fields, username, password
    accounts = bringAccounts()
    wantedUsername = info[0]
    if(wantedUsername in accounts):
        return False
    file = open("data/passwords.csv", "a")
    username = info[0]
    password = info[1]
    if("," in info[0]):
        username = '"'+info[0]+'"'
    outString = "\n"+username+","+password
    file.write(outString)
    file.close()
    
    return True
    
    

