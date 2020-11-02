import os 
import csv

#path to collect csv data
poll_csv = os.path.join("Resources", "election_data.csv")

#variables
total_votes = 0
candidates_list = []
candidate_count = []


# get data and read file
with open (poll_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    next(csvreader)

    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        if candidate not in candidates_list:
            candidates_list.append(candidate)
            candidate_count.append(1)
        else:
            candidate_count[candidates_list.index(candidate)] += 1

def percentage(parameter):
    percent = (parameter/total_votes) * 100     
    return (percent)
    
print("Election Results")
print("---------------------------")    
print(f"Total Votes: {total_votes}")
print("---------------------------")
for x in range(len(candidates_list)):
    print (f"{candidates_list[x]}: {percentage(candidate_count[x]):.2f}% ({candidate_count[x]})")
    

    