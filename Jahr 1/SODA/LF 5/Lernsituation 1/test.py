import sys 
import csv
import json

nameEingabeDatei = input("Name Eingabedatei: ")
 
nameAusgabeDatei = input("Name Ausgabedatei: ")
nameEingabeDatei = sys.argv[1]
nameAusgabeDatei = sys.argv[2]
sys.setdefaultencoding("UTF-8") 
inputFile = open(nameEingabeDatei) #open json file
outputFile = open(nameAusgabeDatei, 'w') #load csv file
data = json.load(inputFile) #load json content
inputFile.close() #close the input file    
output = csv.writer(outputFile) #create a csv.write    
output.writerow(data[0].keys())  # header row    
for row in data:
    output.writerow(row.values()) #values row