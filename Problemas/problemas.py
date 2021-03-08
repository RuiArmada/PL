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
def ipAdress():
    file = open("../Ficheiros/Ip.txt" , "r")
    
    for line in file:
        y = re.search(r'((2[0-4][0-9]|25[0-5]|1[0-9][0-9]|[1-9][0-9])\.){3}(2[0-4][0-9]|25[0-5]|1[0-9][0-9]|[1-9][0-9])', line)
        x = re.search(r'([0-9a-f]{1,4}:){7}[0-9a-f]{1,4}', line)
        if y:
            print("IPv4",end=" - ")
        elif x:
            print("IPv6",end=" - ")
        else:
            print("ERROR",end=" - ")
        print(line,end="")
    file.close()



