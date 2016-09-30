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
    if(request.form["username"] == "Asterix" and request.form["password"] == "pass"):
        return render_template('success.html', response = "success", longResponse = 'Congrats user, you have hacked me password')
    else:
        return render_template('success.html', response = "Failure", longResponse = 'You failed, Lets leave you out in the cold')
    
    
    return "Knowledge Plzz"


    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
