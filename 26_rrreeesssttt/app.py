#Joyce Liao
#SoftDev1 pd8
#K26 -- Getting more REST
#2018-11-15

from urllib import request
import json

from flask import Flask, render_template

app = Flask(__name__)

USDA_API = "https://api.nal.usda.gov/ndb/reports/?ndbno=45288872&api_key="
USDA_KEY = "LSwsFBYAj6DAx8ChR6hy5420iIX8IyQCPoDMGt3G"

CTY_URL = "https://restcountries.eu/rest/v2/name/china"

ACT_URL = "https://www.boredapi.com/api/activity"

@app.route('/')
def home():
	URL = USDA_API + USDA_KEY
	r = request.urlopen(URL)
	data = r.read()
	dict0 = json.loads(data)
	dict0 = dict0["report"]
	food_name = dict0["food"]["name"]
	ing = dict0["food"]["ing"]["desc"].title()
	# print("USDA: ", food_name, ing)

	r = request.urlopen(CTY_URL)
	data = r.read()
	dict1 = json.loads(data)
	dict1 = dict1[0]
	cty = dict1["name"]
	capital = dict1["capital"]
	region = dict1["region"]
	subregion = dict1["subregion"]
	population = dict1["population"]
	time = dict1["timezones"][0]
	# print(cty, capital, region, subregion, population, time)

	r = request.urlopen(ACT_URL)
	data = r.read()
	dict2 = json.loads(data)
	act = dict2["activity"]
	tp = dict2["type"]
	price = dict2["price"]
	# print(act, tp, price)

	return render_template("index.html", name=food_name, igd=ing, place=cty, cpt=capital, rg=region, srg=subregion, p=population, tz=time, task=act, at=tp, pc=price)

if (__name__ == "__main__"):
	app.debug = True
	app.run()

