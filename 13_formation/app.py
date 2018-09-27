#Team
#SoftDev1 pd8
#K
#2018

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    print(app)
    return render_template('template.html')

@app.route('/req')
def req():
    print(app)
    print(request)
    print(request.args)
    print(request.headers)
    print(request.args['username'])
    return render_template('

if (__name__) == ("__main__"):
    app.debug = True
    app.run()

