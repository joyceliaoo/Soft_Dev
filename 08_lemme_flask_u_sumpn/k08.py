#Joyce Liao
#SoftDev1 pd8
#K08 -- Fill Yer Flask
#2018-09-19

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Welcome home!"

@app.route('/kitchen')
def hello_food():
    return "The fridge is empty!"

@app.route('/bedroom')
def hello_bed():
    return "There's unfinished homework!"

if (__name__ == "__main__"):
    app.debug = True
    app.run()



