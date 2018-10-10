#Team Ferrero -- Cheryl Qian, Joyce Liao
#SoftDev1 pd8
#K17 -- Average
#2018-10-08

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

#create table for peeps.csv
with open('data/peeps.csv') as csvfile:
    command = "CREATE TABLE roster (name TEXT, age INTEGER, id INTEGER PRIMARY KEY)"        #build SQL stmt, save as string
    c.execute(command)    #run SQL statement
    reader = csv.DictReader(csvfile)
    for row in reader:
        command = "INSERT INTO roster Values(?,?,?)"
        c.execute(command, (row['name'], row['age'], row['id']))
        
#c.execute("SELECT * FROM roster")
#print( c.fetchall())

with open('data/courses.csv') as csvfile:
    command = "CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER);"        #build SQL stmt, save as string
    c.execute(command)    #run SQL statement
    reader = csv.DictReader(csvfile)
    for row in reader:
        command = "INSERT INTO courses Values(?,?,?)"
        c.execute(command, (row['code'], row['mark'], row['id']))

#c.execute("SELECT * FROM courses")
#print(c.fetchall())

#==========================================================
def grade_lookup(student):
    command = "SELECT id FROM roster WHERE name = '{0}'".format(student) 
    c.execute(command) #look up student by name
    id = c.fetchone()[0] #retrieve id
    #print(id)
    command = "SELECT code, mark FROM courses WHERE id = " + str(id)
    c.execute(command) #look up course name and grade by id
    return c.fetchall() #return list of courses and grades

#print(grade_lookup('alison'))
#print(grade_lookup('sasha'))    
#print(grade_lookup('tINI'))

#compute average for each student
def compute_average(student):
    grades = grade_lookup(student) #look up each student's grade
    sum = 0
    for grade in grades:
        sum += grade[1] #find the sum of grade in all classes
    avg = sum / len(grades)
    return avg


gradebook = {} #stores students' grades
command = "SELECT name, id FROM roster" 
c.execute(command) #get entire list of students
students = c.fetchall()
for student in students:
    avg = compute_average(student[0])
    gradebook[student[1]] = [student[0], avg] #add to dictionary as {id: [name, avg]}   

#print student name, id, and average
for entry in gradebook:
    print("id: {0}, name: {1}, average: {2}".format(entry, gradebook[entry][0], gradebook[entry][1]))

#create new table to store averages
command = "CREATE TABLE peeps_avg (id INTEGER PRIMARY KEY, average NUMERIC)"
c.execute(command)
for entry in gradebook:
    command = "INSERT INTO peeps_avg Values(?,?)"
    c.execute(command, (entry, gradebook[entry][1]))

#c.execute("SELECT * FROM peeps_avg")
#print(c.fetchall())

def add_courses(student, course, mark):
    command = "SELECT id FROM roster WHERE name = '{0}'".format(student)
    c.execute(command)
    target = c.fetchone()
    if target is not None: #check if student is listed on the roster
        id = target[0] #get id of selected student
        command = "INSERT INTO courses Values(?, ?, ?)" #add corresponding values into course table
        c.execute(command,(course, mark, id))
    else:
        print("Student is not on roster")

# add_courses('TOKiMONSTA', 'chem', '80')
# print(grade_lookup('TOKiMONSTA'))
# add_courses('bob', 'physics', '99')
# c.execute("SELECT * FROM courses")
# print(c.fetchall())
#==========================================================

db.commit() #save changes

db.close()  #close database

