import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

with open('peeps.csv') as newFile:
    reader = csv.DictReader(newFile)
    people = {}
    for row in reader:
        people[row['name']]= row['age']
print(people)

with open('courses.csv') as newFile:
    reader = csv.DictReader(newFile)
    classes = {}
    for row in reader:
        classes[row['code']]= row['mark']
print(classes)
command = ""          #build SQL stmt, save as string
c.execute(command)    #run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
