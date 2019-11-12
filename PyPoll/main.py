import os
import csv
#create path
election_data_csv = os.path.join('election_data.csv')

total_votes = []

with open(election_data_csv, 'r') as csvfile:

    csv_reader = csv.reader(csvfile, delimiter = ',')
    #skip first row
    header = next(csv_reader)

    for row in csv_reader:
        #add to list
        total_votes.append(row)

print(f'Total Votes: {len(total_votes)}')

