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
	NASA_KEY = "03XZMhIrwzaAFyGNInqzU0M9uCvttt56biaVYJEk"
	NASA_URL = "https://api.nasa.gov/planetary/apod?date=2018-11-12&api_key="
	URL = NASA_URL + NASA_KEY
	obj = urllib.request.urlopen(URL)
	c = obj.read() #reads data from response object
	nasa_data = json.loads(c) #converts json format data into dictionary
	#print(nasa_data)
	#print(nasa_data['url'])

	MBTA_KEY = "bf9307a2e18e43d4a9f50ae8162e0f8c"
	MBTA_URL = "https://api-v3.mbta.com/routes/Red?api_key="
	URL = MBTA_URL + MBTA_KEY
	r = urllib.request.urlopen(URL)
	content = r.read()
	# print("content:")
	# print(content)
	mbta_data = json.loads(content)
	mbta_data = mbta_data['data']
	# print("mbta_data:")
	# print(mbta_data)

	return render_template("index.html", pic=nasa_data['url'], description=nasa_data['explanation'], name=mbta_data['attributes']['long_name'], tcolor=mbta_data['attributes']['color'], info=mbta_data['attributes']['description'], type=mbta_data['attributes']['type'])

if (__name__ == "__main__"):
	app.debug = True
	app.run()

