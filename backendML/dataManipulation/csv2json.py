import csv
import json

#csvfile = open('test.csv','r')
csvfile = open('usersClustered.csv','r')
jsonfile = open('usersClustered.json','w')

fieldnames = ("FirstName","LastName","Zip","Email","Earnings","Expenses","ID","Sallary", "Expense_Average", "Expense_Var" , "Employment_Var","Group_ID")

reader = csv.DictReader(csvfile,fieldnames,delimiter=';')
for row in reader:
        json.dump(row,jsonfile)
        jsonfile.write(',')
        jsonfile.write('\n')

