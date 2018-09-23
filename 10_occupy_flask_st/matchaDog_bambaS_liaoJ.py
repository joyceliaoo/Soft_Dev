#Team Matcha Dog -- Shin Bamba, Joyce Liao
#SoftDev1 pd8
#K10 -- Jinja Tuning
#2018-09-22

from flask import Flask ,  render_template
import csv
import random
app = Flask(__name__) #instantiates the Flask class using a constructor

def table(file_name):
    values = {} #initialize dictionary
    with open('occupations.csv') as csvfile: #opens the file for reading as a csv file
        reader = csv.DictReader(csvfile) #special type of reading that lets us use the first row as labels for the columns
        for row in reader:
            values[row['Job Class']] = float(row['Percentage']) #for each row put each column pair in the dictionary
        del values['Total'] #delete the last "total" value
        return values

dictionary = table('occupations.csv') #dictionary created from csv file

#returns a random occupation
def pick_job(dictionary):
    list_jobs = [] #makes empty list
    for key in dictionary:
        num_jobs = int(10*dictionary[key]) #takes the value of each key and makes it put 10x that number of keys into the list
        while num_jobs > 0:
            list_jobs.append(key)
            num_jobs -= 1
    return random.choice(list_jobs) #choose a random value in the mega list

@app.route("/")
def homepage():
    return "Hello, please go to /occupations"
@app.route("/occupations")
def display_occ():
    return render_template("template.html",
                           title = "Occupations" ,
			   head = " Table containing information about occupations in the United States  (courtesy of Mr. Brooks) ",
                           randOccupation = pick_job(dictionary),
                           dict = dictionary)
	

if (__name__) == ("__main__"):
    app.debug = True
    app.run()

