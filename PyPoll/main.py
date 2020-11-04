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

#percentage 
def percentage(parameter):
    percent = (parameter/total_votes) * 100     
    return (percent)


most_votes = candidate_count[0]
most_votes_count = 0
for x in range(len(candidates_list)):
    if candidate_count[x]> most_votes:
        most_votes_count = x
winner = candidates_list[most_votes_count]
           
print("Election Results")
print("---------------------------")    
print(f"Total Votes: {total_votes:0,}")
print("---------------------------")
for x in range(len(candidates_list)):
    print (f"{candidates_list[x]}: {percentage(candidate_count[x]):.2f}% ({candidate_count[x]:0,})")
print("---------------------------")
print(f"Winner: {winner}") 
print("---------------------------")

#write to txt file
output_file = os.path.join("Analysis", "poll_analysis.txt")

with open(output_file, 'w', newline='') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("---------------------------\n")
    txtfile.write(f"Total Votes: {total_votes:0,}\n")
    txtfile.write("---------------------------\n")
    for x in range(len(candidates_list)):
        txtfile.write(f"{candidates_list[x]}: {percentage(candidate_count[x]):.2f}% ({candidate_count[x]:0,})\n")
    txtfile.write("-----------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-----------------------------\n")