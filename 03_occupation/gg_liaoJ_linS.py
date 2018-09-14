#Team GG -- Joyce Liao and Susan Lin
#SoftDev1 pd8
#K#06: StI/O: Divine your Destiny!
#2018-09-14

import random 
diction = {}

def convertToDict(filename):
    f = open(filename, 'r')
    text = f.read().split("\n")
    for x in range (1, len(text)- 2):
        cat = text[x].rsplit(',', 1)
        title = cat[0]
        percent = float(cat[-1]) 
        diction[title] = percent

def randomOcc():
    randlist = []
    for key in diction:
        current = diction[key]
        freq = int(current *10)
        for i in range (freq):
            randlist.append(key)
    print (random.choice(randlist))
       

def main():
    convertToDict('occupations.csv')
    print (diction)
    randomOcc() 

main()

