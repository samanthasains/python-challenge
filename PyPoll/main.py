#In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

#The dataset is composed of three columns: Voter ID, County, and Candidate.

#Analyze the votes and calculates each of the following:

#The total number of votes cast

#A complete list of candidates who received votes

#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote.

print('start!')


#create lists
candidate = []

# Path to collect data from the Resources folder
import csv

with open('C:/Users/saman/Documents/NU_Data_Science_Bootcamp/python-challenge/PyPoll/Resources/election_data.csv', 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
 
    if header != None:
        for row in csvreader:
        
            #Add candidates
            candidate.append(row[2])
    
#Read data to python lists from Voter ID row[0] and Candidate (row[2])

#Count of items in list totalVotes=(len)

#Generate unique entries from list of candidates

#Somehow create dictionary of voter ID associated with each candidate?

#candidatePercent = len(each_candidate)/totalVotes

#