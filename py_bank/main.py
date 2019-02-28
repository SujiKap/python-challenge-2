#PyBank
#Analyse financial records of the company
#Datafile is budget_data.csv
#Columns are Date and Profit/Losses
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period
#Save the datafile 

#Import modules
import os
import csv

# #Locate the file
csvpath = "C:/Users/kapali_s/Documents/SMU/Homeworks/Assignment_3/python-challenge-2/py_bank/budget_data.csv"

#Open the file 
with open (csvpath, newline = "" ) as csvfile:

    #Read the csvfile
    csvreader = csv.reader(csvfile, delimiter=",")

#The total number of months included in the dataset
    header = next(csvreader)
    num_rows = list(csvreader)
    
    #count the rows
    row_count = len(num_rows)
        
    print("Total Months : " + str(row_count))

  #The net total amount of "Profit/Losses" over the entire period
    #start the total
    total_PL = 0

    for row in num_rows:
        total_PL += int(row[1])
        #print(row[1])
             
    print(total_PL)

#The average of the changes in "Profit/Losses" over the entire period
    PL_average = total_PL / row_count

    print(PL_average)
        #average_change = average(row[1])
        #print(average_change)

#The greatest increase in profits (date and amount) over the entire period
    #Go to row 3
    #num_rows[1][1]
    #print(num_rows[1][1])
       
    #Go to row 2
    #num_rows[0][1]
    #print(num_rows[0][1])

    #Substract row 2 from row 3
    #num_rows[1][1] - num_rows[0][1]
    #print(int(num_rows[1][1]) - int(num_rows[0][1]))

    #Repeat for all rows
    repeat=[]
    for i in range(0,row_count-1):
        repeat.append(int(num_rows[i+1][1]) - int(num_rows[i][1]))
        #print(repeat)

        #Get max value
    max_value = max(repeat)
    print("Greatest Increase in Profits: " + str(max_value))

    maxPLvalue = repeat.index(max_value) + 1
    #print(maxPLvalue)
    print(num_rows[maxPLvalue][0])
  




    



        
#The greatest decrease in losses (date and amount) over the entire period
  