#Felix Rieg-Baumhauer
#Softdev pd8
#HW06 -- I Got Issues, You Got Issues
#2016-10-10    



#importing things, not to be touched
import utils.verifyLogin, utils.createAccount, hashlib, os

from flask import Flask, render_template, request, session, redirect, url_for
app = Flask(__name__)    #crts Flask object


#Special things for special sessions
app.secret_key=os.urandom(32)
secret = "felixwebsite"#NOT THE REAL ONE, THAT ONE IS A SECRET,

#This is how we logout, is activated by a button being pushed
@app.route("/logout")
def loggerOuter():
    print session
    session.pop(secret)
    return redirect(url_for("showFront"))

#the home page, presents login.html
@app.route("/")
def showFront():
    #--------------------------------------------------------------
    #print "\n\n\n"
    #print "::::DIAG: this Flask obj::::"
    #print app
    #print "::::DIAG: request obj::::"
    #print request
    #print "::::DIAG: request.args::::"
    #print request.args
    #print "::::DIAG: request.args['username'] ::::"
    #print request.args['username'] #only works if username submitted
    #print "::::DIAG: request.headers ::::"
    #print request.headers          #only works for POST
    #--------------------------------------------------------------

    if(secret in session):
        return render_template('success.html', response = "Success", permission = True, longResponse = 'You have used a cookie to stay logged in')
    else:
        return render_template( 'login.html' )#the only important line, whips up tmplate
    #return render_template( 'login.html' )#the only important line, whips up tmplate

#presents the make account page, make_account.html
@app.route("/make_account")
def makeMeOne():
    return render_template('make_account.html')

#informUser(), route account_status, is used to process the given future usernames and passwords, passing them on to createAccount in utils, and pulling up account_status
@app.route("/account_status", methods=['POST'])
def infomUser():
    newUser = request.form["newUsername"]
    statusOfApp=(utils.createAccount.checkUser(newUser) and
                 (request.form["newPassword"] == request.form["newPassword2"]) and ((newUser or request.form["newPassword"]) != ""))
    
    if(statusOfApp == True):
        rawPass = request.form["newPassword"]
        hashPassObj = hashlib.sha1()
        hashPassObj.update(rawPass)
        hashedPass = hashPassObj.hexdigest()
        
        wantedAccount = []
        wantedAccount.append(newUser)
        wantedAccount.append(hashedPass)
        statusOfApp = utils.createAccount.makeAccount(wantedAccount)
        
        if(statusOfApp == True): # should allways be true
            return render_template('account_status.html',title="Welcome", statusOfApp=statusOfApp)
        else:
            return error #----THIS SHOULD NEVER HAPPEN-----#
    else:
        return render_template('make_account.html',title="Failure", statusOfApp=statusOfApp)

    return "failsafe"  #----THIS SHOULD NEVER HAPPEN-----#


#@app.route("/auth")
#@app.route("/auth", methods=['GET'])

#/auth authenticates if your account exists, and the if your password is correct for that account
@app.route("/auth", methods=['POST'])
def authenticate():
    
    #-----------------------------------------------------------
    #print "\n\n\n"
    #print "::::DIAG: this Flask obj::::"
    #print app
    #print "::::DIAG: request obj::::"
    #print request
    #print "::::DIAG: request.args::::"
    #print request.args
    #print "::::DIAG: request.args['username']::::"
    #print request.args['username'] #only works if username submitted
    #print "::::DIAG: request.headers::::"
    #print request.headers          #only works for POST
    #------------------------------------------------------------

    #---------------------------Testing Purposes
    #secret = os.urandom(32)
    #print secret
    #session["felix"] ="here"
    #print session
    #------------------------------------------------------------

    
    accounts = utils.verifyLogin.bringAccounts()
    givenUser = request.form["username"]
    givenPass = request.form["password"]

    #hashing
    hashGPassObj = hashlib.sha1()
    hashGPassObj.update(givenPass)
    hashedGPass = hashGPassObj.hexdigest() 
    
    if( givenUser in accounts  and hashedGPass == accounts[givenUser] ):
        
        session[secret]=givenUser
        #print session
        
        return render_template('success.html', response = "Success", permission = True, longResponse = 'Congrats user, you have hacked me password')
    else:
        return render_template('login.html', permission = False)
        #return render_template('success.html', response = "Failure", authLvl = False, longResponse = 'You dont have a password here, to make one click, <a href="/auth">here</a>')
        
    #----------------------------------------------------#
    return "Knowledge Plzz"  #----THIS SHOULD NEVER HAPPEN-----#


    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
