# Export results to a txt file
export = open("poll_summary.txt","w+")

#Import dependecies 
import os
import csv

# Choose the csv and outline the file path
csvpath = os.path.join("Resources" ,"election_data.csv")

# Read csv
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

# Print header for results 
    print("---------------------")
    print ("Election Results")
    print("---------------------")
    print("---------------------",file=export)
    print ("Election Results", file=export)
    print("---------------------",file=export)

# Define variables
    total_votes = 0
    candidate_list = []
    candidate_votes = {}
    winner_votes = 0
    winner =[]

# Find total votes in election, votes for each candidate, and percent of votes for each candidate.
    for row in csvreader:
        total_votes += 1
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            candidate_votes[row[2]] = 0
        candidate_votes[row[2]] += 1

# Print and write total votes
    print (f"Total Votes: {total_votes}")
    print("---------------------") 
    print (f"Total Votes: {total_votes}",file=export)
    print("---------------------",file=export) 
    
    for candidate_list in candidate_votes: 
        votes = candidate_votes.get(candidate_list)
        percent_votes = float(votes)/(total_votes) * 100
         
# Print candidate, percentage of votes they won, and votes they received
        print(f"{candidate_list}: {percent_votes:.3f}% ({votes}) ")
        print(f"{candidate_list}: {percent_votes:.3f}% ({votes})", file = export)
# Find the winner
    for candidate_list in candidate_votes: 
           if (float(votes) > winner_votes):
            winner_votes = float(votes)
            winner = candidate_list

# Declare the winner 
print("---------------------")
print("Winner: "+ str(winner))
print("---------------------")
print("---------------------", file=export)
print("Winner: "+ str(winner), file=export)
print("---------------------", file=export)

export.close