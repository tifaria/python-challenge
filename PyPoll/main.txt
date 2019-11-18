import os
import csv
import statistics
#create path
election_data_csv = os.path.join('election_data.csv')

total_votes = []
k_votes = 0
c_votes = 0
l_votes = 0
o_votes = 0
candidates = []

with open(election_data_csv, 'r') as csvfile:

    csv_reader = csv.reader(csvfile, delimiter = ',')
    #skip first row
    header = next(csv_reader)

    for row in csv_reader:
        #add to list
        total_votes.append(row)
        #count the number of times a candidate name appears and add it to their variable
        if row[2] == "Khan":
            k_votes += 1
        elif row[2] == "Correy":
            c_votes += 1
        elif row[2] == "Li":
            l_votes += 1
        elif row[2] == "O'Tooley":
            o_votes += 1
        #add all candidate row to the cadidates list
        candidates.append(row[2])

    #calculate the win percentage of each candidate 
    k_win_percentage = (k_votes/len(total_votes))*100
    c_win_percentage = (c_votes/len(total_votes))*100
    l_win_percentage = (l_votes/len(total_votes))*100
    o_win_percentage = (o_votes/len(total_votes))*100
    #find winner by finding the most repetitive value (mode) in candidates list
    election_winner = statistics.mode(candidates)
        

#print final election results
print("Election Results")
print("--------------------------------")
print(f'Total Votes: {len(total_votes)}')
print("--------------------------------")
print(f'Khan: {round(k_win_percentage, 2)}% ({(k_votes)})')
print(f'Correy: {round(c_win_percentage,2)}% ({c_votes})')
print(f'Li: {round(l_win_percentage, 2)}% ({l_votes})')
print(f"O'Tooley: {round(o_win_percentage, 2)}% ({o_votes})")
print("--------------------------------")
print(f'Winner: {election_winner}')
