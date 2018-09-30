#Joyce Liao
#SoftDev1 pd8
#K13 -- Echo echo echo
#2018-09-27

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('template.html',
                            title = "Home",
                            home_page = True)

@app.route('/welcome', methods=['GET', 'POST'])
def greetings():
    rme = request.method
    uname = " "
    if (rme == 'GET'):
        uname = request.args['username']
    else:
        uname = request.form['username']
    return render_template('template.html',
                           title = "Welcome",
                           username = uname,
                           req_method = rme)

if (__name__) == ("__main__"):
    app.debug = True
    app.run()



