# Lists to store data
date = []
profitLoss = []
greatestIncrease = ['',0]
greatestDecrease = ['', 1000000]

# Path to collect data from the Resources folder
import csv

with open('C:/Users/saman/Documents/NU_Data_Science_Bootcamp/python-challenge/PyBank/Resources/budget_data.csv', 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',') 
    header = next(csvreader)
    firstRow = next(csvreader)

    date.append(firstRow[0])    
    profitLoss.append(int(firstRow[1]))
    previousRow=int(firstRow[1])

    if header != None:
        for row in csvreader:
        
            #Add date
            date.append(row[0])
    
            #Add profit/loss
            profitLoss.append(int(row[1])) 

            change=int(row[1])-previousRow
            previousRow=int(row[1])

            if change>greatestIncrease[1]:
                greatestIncrease[0]=row[0]
                greatestIncrease[1]=change
            
            if change<greatestDecrease[1]:
                greatestDecrease[0]=row[0]
                greatestDecrease[1]=change

# # Find the total number of months included in the dataset - count of items
totalMonths = len(date)

# #Find the net total amount of "Profit/Losses" over the entire period - sum of the values in [1]
totalAmount = sum(profitLoss)                    

# # Find the average of the changes in "Profit/Losses" over the entire period - average of the values in [1]
revenueChange = []
for x in range(0,totalMonths-1):
    revenueChange.append(profitLoss[x+1]-profitLoss[x])
averageChange=(sum(revenueChange)/(totalMonths-1))

# # # Print the analysis to the terminal and export a text file with the results
print('Financial Analysis\n----------------')
print('Total months : ' + str(totalMonths))
print('Average Change: $' + str(averageChange))
print('Greatest Increase in Profits: ' + str(greatestIncrease))
print('Greatest Descrease in Profits: ' + str(greatestDecrease))