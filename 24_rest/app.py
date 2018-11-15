#Joyce Liao
#SoftDev1 pd8
#K24 -- A RESTful Journey Skyward
#2018-11-14

from flask import Flask, render_template
import urllib.request
import json

app = Flask(__name__)

@app.route('/')
def home():
	obj = urllib.request.urlopen('https://api.nasa.gov/planetary/apod?date=2018-11-12&api_key=03XZMhIrwzaAFyGNInqzU0M9uCvttt56biaVYJEk')
	byte_data = obj.read() #reads data from response object
	data = json.loads(byte_data) #converts json format data into dictionary
	#print(data)
	#print(data['url'])
	return render_template("index.html", pic=data['url'], description=data['explanation'])

if (__name__ == "__main__"):
	app.debug = True
	app.run()

