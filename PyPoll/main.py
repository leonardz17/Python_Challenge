import os 
import csv

#path to collect csv data
poll_csv = os.path.join("Resources", "election_data.csv")

#variables
total_votes = 0
candidate = {}

with open (poll_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        total_votes += 1
        if row[2] not in candidate:
            candidate[row[2]] = 1 
        else:
            candidate[row[2]] += 1 
            
           
    print(f"Total Votes: {total_votes}")
    print(candidate)