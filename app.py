import utils.accountPasser
from flask import Flask, render_template, request
app = Flask(__name__)    #crts Flask object



@app.route("/")
def showFront():
    print "\n\n\n"
    print "::::DIAG: this Flask obj::::"
    print app
    print "::::DIAG: request obj::::"
    print request
    print "::::DIAG: request.args::::"
    print request.args
    #print "::::DIAG: request.args['username'] ::::"
    #print request.args['username'] #only works if username submitted
    #print "::::DIAG: request.headers ::::"
    #print request.headers          #only works for POST
    return render_template( 'login.html' )#the only important line, whips up tmplate

@app.route("/make_account")
def makeMeOne():
    #test = ["Mickey", "mouse"]
    return render_template('makeAccount.html')
    #return (utils.accountPasser.makeAccount(test))

@app.route("/accountStatus", methods=['POST'])
def infomUser():
    wantedAccount = []
    wantedAccount.append(request.form["newUsername"])
    wantedAccount.append(request.form["newPassword"])
    statusOfApp = utils.accountPasser.makeAccount(wantedAccount)
    if(statusOfApp == True):
        return render_template('accountStatus.html',title="Welcome", text="Welcome to your new account", statusOfApp=statusOfApp)
    else:
        return render_template('accountStatus.html',title="NO Account For You", text="That username is allready taken", statusOfApp=statusOfApp)

    return "failsafe"

#@app.route("/auth")
#@app.route("/auth", methods=['GET'])
@app.route("/auth", methods=['POST'])
def authenticate():
    print "\n\n\n"
    print "::::DIAG: this Flask obj::::"
    print app
    print "::::DIAG: request obj::::"
    print request
    print "::::DIAG: request.args::::"
    print request.args
    #print "::::DIAG: request.args['username']::::"
    #print request.args['username'] #only works if username submitted
    #print "::::DIAG: request.headers::::"
    #print request.headers          #only works for POST

    accounts = utils.accountPasser.bringAccounts()
    
    #if(request.form["username"] == "Asterix" and request.form["password"] == "pass"):

    givenUser = request.form["username"]
    givenPass = request.form["password"]
    if( givenUser in accounts  and givenPass == accounts[givenUser] ):
        return render_template('success.html', response = "Success", authLvl = True, longResponse = 'Congrats user, you have hacked me password')
    else:
        return render_template('success.html', response = "Failure", authLvl = False, longResponse = 'You dont have a password here, to make one click, <a href="/auth">here</a>')
    
    
    return "Knowledge Plzz" #this should never fire


    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
