#Team Catbug -- Vincent Chi, Joyce Liao
#SoftDev1 pd8
#K15 -- Oh yes, perhaps I do...
#2018-10-03

from flask import Flask, render_template, request, flash, \
	session, url_for, redirect
import os

app = Flask(__name__)

combo = { "softdev" : "period8"}

app.secret_key = os.urandom(32)

@app.route('/')
def login():
    if session != {}:
        return redirect(url_for('welcome_user'))
    return render_template("login.html")

@app.route('/auth',methods=["POST"])
def authenticate():
    #print(request.form['username'])
    if not(request.form['username'] in combo):
        flash('That username does not exist!')
        return render_template('error.html')
    elif request.form['password'] != combo['softdev']:
        flash('That is the wrong password!')
        return render_template('error.html')
    else:
        flash('Welcome, Bravest Warrior!')
        session[request.form['username']] = request.form['password']
        return redirect(url_for('welcome_user'))


@app.route('/welcome')
def welcome_user():
    return render_template("welcome.html",
                           name = 'softdev')

@app.route('/exit')
def logout():
    session.pop('softdev')
    return redirect(url_for('login'))
    

if (__name__) == ("__main__"):
    app.debug = True
    app.run()

