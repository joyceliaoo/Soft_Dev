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
    #opens the file for reading as a csv file
    with open('occupations.csv') as csvfile:
        #special type of reading that uses the first row as labels for the columns
        reader = csv.DictReader(csvfile)
        for row in reader:
            #create key-value pairs for each row
            values[row['Job Class']] = float(row['Percentage']) 
        return values

dictionary = table('occupations.csv') #dictionary created from csv file

#returns a random occupation
def pick_job(dictionary):
     rand_float = random.uniform(0, 99.8) #generates a random float in range [0, 99.8]
     if rand_float < 6.1: #when it is less than the first percentage
         return "No job found :("
     for occupation in dictionary:
         rand_float -= dictionary[occupation] #subtract each percentage going down the list
         if rand_float <= 0: #has arrived at the right interval
             return occupation

@app.route("/")
def homepage():
    return "Hello, please go to /occupations"
@app.route("/occupations")
def display_occ():
    return render_template("template.html",
                           title = "Occupations" ,
			   head = " Table containing information about occupations in the United States (courtesy of Mr. Brooks) ",
                           randOccupation = pick_job(dictionary),
                           dict = dictionary)
	

if (__name__) == ("__main__"):
    app.debug = True
    app.run()

