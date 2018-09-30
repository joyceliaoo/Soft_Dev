#Team Matcha Dog -- Shin Bamba, Joyce Liao
#SoftDev1 pd8
#K10 -- Jinja Tuning
#2018-09-22

from flask import Flask ,  render_template
from util import occupation
#import util as occupation

app = Flask(__name__) #instantiates the Flask class using a constructor

dictionary = occupation.table('data/occupations.csv') #dictionary created from csv file

@app.route("/")
def homepage():
    return "Hello, please go to /occupations"
@app.route("/occupations")
def display_occ():
    return render_template("template.html",
                           title = "Occupations" ,
			   head = " Table containing information about occupations in the United States (courtesy of Mr. Brooks) ",
                           randOccupation = occupation.pick_job(dictionary),
                           dict = dictionary)
	

if (__name__) == ("__main__"):
    app.debug = True
    app.run()

