import os
import csv

#path to collect csv data
bank_csv = os.path.join("Resources", "budget_data.csv")

#defining variables
total_months = 0
total_profits = 0
total_profit_change = 0
last_profit = 0
highest_profits = -999999999
lowest_profits = 999999999
highest_month = ""
lowest_month = ""


#read in csv file
with open (bank_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        profit = int(row[1])
        month = row[0]
        if total_months == 0:
            last_profit = profit
        else:
            total_profit_change = profit - last_profit
            last_profit = profit
        if profit > highest_profits:
            highest_profits = profit
            highest_month = row[0]
        if profit < lowest_profits:
            lowest_profits = profit
            lowest_month = row[0]

        total_months += 1
        total_profits = total_profits + profit
        avg_change = total_profit_change/total_months -1

    print(f"Total Months: {total_months}")
    print(f"Net Total Profit: ${total_profits:0,.0f}")
    print(f"Average Change: ${avg_change:0,.0f}")
    print(f"Greatest Increase: {highest_month} ${highest_profits}")
    print(f"Greatest Decrease: {lowest_month} ${lowest_profits}")
    
   
    

