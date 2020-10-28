import os
import csv

#path to collect csv data
bank_csv = os.path.join("Resources", "budget_data.csv")

#defining variables
total_months = 0
total_profits = 0

#read in csv file
with open (bank_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        month = row[0]
        total_months += 1 
        profit = int(row[1])
        total_profits = total_profits + profit

print(f"Total Months: {total_months}")
print(f"Net Total Profit: ${total_profits:0,.0f}")
    

