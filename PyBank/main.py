#Import dependencies
import os
import csv

# Choose the csv and outline the file path
csvpath = os.path.join("Resources" ,"budget_data.csv")

# Read csv
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

#Declare variables
    profit = []
    month = []
    total_profit = []
    profit_change = []
    average_change = []

#Count the total months and total profit 
    for row in csvreader:
        month.append(row[0])
        profit.append(float(row[1])) 
        total_profit += profit

#Summarize the changes in profit and determine the months with greatest increase/decrease in profits
    for r in range(1,len(profit)):
        profit_change.append(profit[r]-profit[r-1])
        profit_max_change = max(profit_change)
        profit_min_change = min(profit_change)
        month_max = str(month[profit_change.index(profit_max_change)+1])
        month_min = str(month[profit_change.index(profit_min_change)+1])
        average_change = sum(profit_change)/len(profit_change)

# Print results 
print ("---------------------------------")
print ("Financial Analysis")
print ("---------------------------------")
print ("Total Months: ", len(month))
print ("Total: $" , f"{sum(profit):.0f}")
print("Average Change: $", f"{average_change:.2f}")
print("Greatest Increases in Profits:", month_max,"($", f"{profit_max_change:.0f}",")")
print("Greatest Decrease in Profits:", month_min,"($", f"{profit_min_change:.0f}",")")

# Export results to a txt file
export = open("financial_summary.txt","w+")
# Print results 
print ("---------------------------------", file=export)
print ("Financial Analysis", file=export)
print ("---------------------------------", file=export)
print ("Total Months: ", len(month), file=export)
print ("Total: $" , f"{sum(profit):.0f}", file=export)
print("Average Change: $", f"{average_change:.2f}", file=export)
print("Greatest Increases in Profits:", month_max,"($", f"{profit_max_change:.0f}",")", file=export)
print("Greatest Decrease in Profits:", month_min,"($", f"{profit_min_change:.0f}",")", file=export)
export.close