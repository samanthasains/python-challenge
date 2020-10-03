#In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

#The dataset is composed of three columns: Voter ID, County, and Candidate.

#Analyze the votes and calculates each of the following:

#The total number of votes cast (done)

#A complete list of candidates who received votes (done)

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
    
#Count of items in list totalVotes=(len)
totalVotes=len(candidate)

#Generate unique entries from list of candidates
candidate_names=set(candidate)
candidate_names=list(candidate_names)

# Set vote counters for candidates
candidateOne=0
candidateTwo=0
candidateThree=0
candidateFour=0

#Generate vote numbers for each candidate
for name in candidate:
    if name == candidate_names[0]:
        candidateOne = candidateOne + 1
    if name == candidate_names[1]:
        candidateTwo=candidateTwo+1
    if name == candidate_names[2]:
        candidateThree=candidateThree+1
    if name==candidate_names[3]:
        candidateFour=candidateFour+1

#candidatePercent = len(each_candidate)/totalVotes

#Print results to text file
print('Elections Results\n----------------')
print('Total Votes : ' + str(totalVotes))
print('\n----------------')
print(str(candidate_names[0])": " str(candidateOne/totalVotes) + ' ('str(candidateOne):')')
