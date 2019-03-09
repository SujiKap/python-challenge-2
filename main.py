
#Import modules
#Import modules
import os
import csv

# #Locate the file
csvpath = "C:/Users/kapali_s/Documents/SMU/Homeworks/Assignment_3/python-challenge-2/py_poll/election_data.csv"

#Open the file 
with open (csvpath, newline = "" ) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

## The total number of votes cast
    header = next(csvreader)
    num_rows = list(csvreader)
    
    #count the rows
    row_count = len(num_rows)

    print("Election Results")   
    print("-------------------------------")
    print("Total Votes : " + str(row_count))
    print("-------------------------------")

    # A complete list of candidates who received votes
    #Get the list of candidates
    #create a new list 
    candidates = []
    for row in num_rows:
        candidates.append(row[2])   #last names

    uniqueCandidates = set(candidates)

    #print(uniqueCandidates) #print unique last names

    maxVoteCount = 0
    winner = ""
    
    for candidate in uniqueCandidates:        
        votesPerCandidate = candidates.count(candidate)

        if votesPerCandidate > maxVoteCount:
            maxVoteCount = votesPerCandidate
            winner = candidate


        percentVotePerCandidate = round((votesPerCandidate/row_count)*100, 3)
        print(candidate + " :" + str(percentVotePerCandidate) + "%" + "("+ str(votesPerCandidate) + ")")
                

    print("----------------------------------------------")
    
    print("Winner :" + winner)

   



        
    