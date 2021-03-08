import re

def mysearch(ER):
    source = input(">>")
    while source != "": #while there is no input the source will be ""
        y = re.search(ER, source)
        if(y): #if it is found
            print("VALID")
        else:
            print("INVALID")
        source = input(">>")

#Problem 1
def alienUsername():
    mysearch(r'^[_.][0-9]+(?i:[a-z]){3,}_?$')

#Problem 2