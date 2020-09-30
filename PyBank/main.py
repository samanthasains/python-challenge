# Lists to store data
date = []
profitLoss = []

# Path to collect data from the Resources folder
import csv

with open('C:/Users/saman/Documents/NU_Data_Science_Bootcamp/python-challenge/PyBank/Resources/budget_data.csv', 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',') 
    header = next(csvreader)
    if header != None:
        for row in csvreader:
        
            #Add date
            date.append(row[0])
    
            #Add profit/loss
            profitLoss.append(int(row[1])) 

# Find the total number of months included in the dataset - count of items
totalMonths = len(date)

#Find the net total amount of "Profit/Losses" over the entire period - sum of the values in [1]
totalAmount = sum(profitLoss)                    

# Find the average of the changes in "Profit/Losses" over the entire period - average of the values in [1]
revenueChange = []
for x in range(0,totalMonths-1):
    revenueChange.append(profitLoss[x+1]-profitLoss[x])
averageChange=(sum(revenueChange)/(totalMonths-1))

# Find the greatest increase in profits (date and amount) over the entire period - maximum value
For i in profitLoss:
    if i > i-1, then :
        greatestIncrease = i
        increaseDate = date[i]

#Find greatest decrease in losses (date and amount) over the entire period - minimum value
For i in profitLoss:
    if i < i-1, then:
        greatestDecrease = i
        decreaseDate = date[i]

# Print the analysis to the terminal and export a text file with the results
print('Financial Analysis\n----------------')
print('Total Months: ' + str(totalMonths))
print('Average Change: $' +str(averageChange))
print('Greatest Increase in Profits: ' + increaseDate' ' + greatestIncrease)
print('Greatest Descrease in Profits: ' + decreaseDate' ' + greatestDecrease)