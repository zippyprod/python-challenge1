# Import the os,csv and a Staics module a friend showed me
# This will allow us to create file paths across operating systems
import os
import csv
import statistics

#Set path for bank data and outputpath
bank_data = os.path.join('PyBank','Resources',"budget_data.csv")
outputpath=os.path.join('PyBank','Analysis',"Finacial_Analysis.txt")

#Set valeus
monthCount = 0
totalVolume = 0
greatestIncrease = 0
bestMonth = ''
greatestDecrease = 0
worstMonth = ''

change = []
monthToMonthChange = []

with open(outputpath, newline='') as csvfile:


    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        monthCount += 1
        totalVolume += int(row[1])
        if int(row[1]) > greatestIncrease:
            bestMonth = (row[0])
            greatestIncrease = int(row[1])
        elif int(row[1]) < greatestDecrease:
            worstMonth = (row[0])
            greatestDecrease = int(row[1])
        change.append(int(row[1]))

  
# track monthly changes
for i in range(len(change)-1):
    monthlyChange = (change[i+1] - change[i])
    monthToMonthChange.append(monthlyChange)   

averageChange = statistics.mean(monthToMonthChange)

print("\n")
print("Financial Analysis\n")
print("------------------------------------")
print("\n")
print("Total Months: " + str(monthCount))
print("Total: $" + str(totalVolume))
print("Average Change is: $" + str(round(averageChange, 2)))
print("Greatest Increase in Profits: " + str(bestMonth) + "  ($" + str(greatestIncrease) + ")")
print("Greatest Decrease in Profits: " + str(worstMonth) + "  ($" + str(greatestDecrease) + ")")
print("\n")
print("-------------------------------------")

# now write this to an output file
f = open("financial_analysis.txt", "w")
f.write("Financial Analysis")
f.write("___________________________________")

f.write("Total Months: " + str(monthCount))
f.write("Average Change is: $" + str(round(averageChange, 2)))
f.write("Total: $" + str(totalVolume))
f.write("Greatest Increase in Profits: " + str(bestMonth) + "  ($" + str(greatestIncrease) + ")")
f.write("Greatest Decrease in Profits: " + str(worstMonth) + "  ($" + str(greatestDecrease) + ")")

