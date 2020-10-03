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
voteTotals=0

#Generate vote numbers for each candidate
for name in candidate:
    if name == candidate_names[0]:
        candidateOne = candidateOne + 1
        if candidateOne > voteTotals:
            voteTotals=candidateOne
            winner=candidate_names[0]    
    if name == candidate_names[1]:
        candidateTwo=candidateTwo+1
        if candidateTwo > voteTotals:
            voteTotals=candidateTwo
            winner=candidate_names[1]   
    if name == candidate_names[2]:
        candidateThree=candidateThree+1
        if candidateThree > voteTotals:
            voteTotals=candidateThree
            winner=candidate_names[2]   
    if name==candidate_names[3]:
        candidateFour=candidateFour+1
        if candidateFour > voteTotals:
            voteTotals=candidateFour
            winner=candidate_names[3]   

#Print results to text file
print('Elections Results\n----------------')
print('Total Votes : ' + str(totalVotes) + '\n----------------')
print(candidate_names[0] + ': ' + ("{:.0%}".format(candidateOne/totalVotes)) + ' (' + str(candidateOne) + ')')
print(candidate_names[1] + ': ' + ("{:.0%}".format(candidateTwo/totalVotes)) + ' (' + str(candidateTwo) + ')')
print(candidate_names[2] + ': ' + ("{:.0%}".format(candidateThree/totalVotes)) + ' (' + str(candidateThree) + ')')
print(candidate_names[3] + ': ' + ("{:.0%}".format(candidateFour/totalVotes)) + ' (' + str(candidateFour) + ')')
print('----------------')
print('Winner: ' + winner + '\n----------------')

