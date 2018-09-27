#Joyce Liao
#SoftDev1 pd8
#K13 -- Echo echo echo
#2018-09-27

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('template.html',
                            title = "Welcome",
                            home_page = True)

@app.route('/welcome')
def greetings():
    return render_template('template.html',
                           title = "Welcome",
                           username = request.args['username'],
                           req_method = request.method)

if (__name__) == ("__main__"):
    app.debug = True
    app.run()



