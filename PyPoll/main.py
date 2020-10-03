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

#create dictionary to store candidate data
voteDict = {}

#Generate vote numbers for each candidate & print to dictionary
for name in candidate:
    if name == candidate_names[0]:
        candidateOne = candidateOne + 1
        voteDict[candidate_names[0]]=candidateOne, "{:.0%}".format(candidateOne/totalVotes)
        if candidateOne > voteTotals:
            voteTotals=candidateOne
    if name == candidate_names[1]:
        candidateTwo=candidateTwo+1
        voteDict[candidate_names[1]]=candidateTwo, "{:.0%}".format(candidateTwo/totalVotes)
        if candidateTwo > voteTotals:
            voteTotals=candidateTwo 
    if name == candidate_names[2]:
        candidateThree=candidateThree+1
        voteDict[candidate_names[2]]=candidateThree, "{:.0%}".format(candidateThree/totalVotes)
        if candidateThree > voteTotals:
            voteTotals=candidateThree  
    if name==candidate_names[3]:
        candidateFour=candidateFour+1
        voteDict[candidate_names[3]]=candidateFour, "{:.0%}".format(candidateFour/totalVotes)  
        if candidateFour > voteTotals:
            voteTotals=candidateFour  

#Sort dictionary by votes
results=dict(sorted(voteDict.items(), key=lambda x: x[1], reverse=True))    

#Print results to terminal
print('Elections Results\n----------------')
print('Total Votes : ' + str(totalVotes) + '\n----------------')
for k,v in results.items():
    print(k,v) 
print('----------------')
print('Winner: ' + str(next(iter(results))) + '\n----------------')


#Print results to text file
f= open("PyPollResults.txt", "a")
f.write(str('Elections Results\n----------------\n'))
f.write(str('Total Votes : ' + str(totalVotes) + '\n----------------\n'))
for k,v in results.items():
    f.write(str((k,v)))
f.write(str(('\n----------------\n')))
f.write(str('Winner: ' + str(next(iter(results))) + '\n----------------'))
f.close()