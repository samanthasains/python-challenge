# Lists to store data
date = []
profitLoss = []
greatestIncrease = ['',0]
greatestDecrease = ['', 1000000]
revenueChange = []

# Path to collect data from the Resources folder
import csv

with open('C:/Users/saman/Documents/NU_Data_Science_Bootcamp/python-challenge/PyBank/Resources/budget_data.csv', 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',') 
    
    #skip header row when reading data into lists
    header = next(csvreader)
    
    #Write just the first row to account for off by one when calculating differences
    firstRow = next(csvreader)
    date.append(firstRow[0])    
    profitLoss.append(int(firstRow[1]))
    previousRow=int(firstRow[1])

    #skipping header, iterate through each row from csv file
    if header != None:
        for row in csvreader:
        
            #Add date
            date.append(row[0])
    
            #Add profit/loss
            profitLoss.append(int(row[1])) 
            
            #Write difference between profit/loss to previousRow list
            change=int(row[1])-previousRow
            previousRow=int(row[1])

            #If change row value is higher than previous max value, set as greatest increase
            if change>greatestIncrease[1]:
                greatestIncrease[0]=row[0]
                greatestIncrease[1]=change
            
            #If change row value is lower than previous min value, set as greatest decrease
            if change<greatestDecrease[1]:
                greatestDecrease[0]=row[0]
                greatestDecrease[1]=change

# Find the total number of months included in the dataset
totalMonths = len(date)

#Find total profits
totalProfit=sum(profitLoss)

# Find the net total amount of "Profit/Losses" over the entire period
totalAmount = sum(profitLoss)                    

# Find the average of the changes in "Profit/Losses" over the entire period 
for x in range(0,totalMonths-1):
    revenueChange.append(profitLoss[x+1]-profitLoss[x])
averageChange=format((sum(revenueChange)/(totalMonths-1)), '.2f')

# Print the analysis to the terminal
print('Financial Analysis\n----------------')
print('Total Profits: ' + str(totalProfit))
print('Total months : ' + str(totalMonths))
print('Average Change: $' + str(averageChange))
print('Greatest Increase in Profits: ' + str(greatestIncrease[0]) + ' ($' + str(greatestIncrease[1]) + ')')
print('Greatest Descrease in Profits: ' + str(greatestDecrease[0]) + ' ($' + str(greatestDecrease[1]) + ')')

# Export analysis to text file with the results
f= open("PyBankResults.txt", "a")
f.write(str('Financial Analysis\n----------------\n'))
f.write(str('Total Profits: ' + str(totalProfit)))
f.write(str('Total months : ' + str(totalMonths)))
f.write(str('\nAverage Change: $' + str(averageChange)))
f.write(str('\nGreatest Increase in Profits: ' + str(greatestIncrease[0]) + ' ($' + str(greatestIncrease[1]) + ')'))
f.write(str('\nGreatest Descrease in Profits: ' + str(greatestDecrease[0]) + ' ($' + str(greatestDecrease[1]) + ')'))
f.close()