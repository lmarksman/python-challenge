# Matthew Lett
# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

total_votes = 0
canidate_results ={}
winner_name = ""
winner_count = 0

csvpath = os.path.join('Resources', 'election_data.csv')

#open the file for reading
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    
    for row in csvreader:
        # count the total votes
        total_votes += 1

        # add each canditate that received a vote
        if row[2] in canidate_results:
            canidate_results[row[2]] +=1 
        else:
            canidate_results[row[2]] = 1


# print results to the screen
print('Election Results')
print('-------------------------')
print(f'Total Votes: {total_votes}')
print(f'------------------------')
for key, value in canidate_results.items():
    percentage_of_vote = (value / total_votes) * 100
    print(f'{key}: {round(percentage_of_vote, 3)}% ({value})')

    # find the winner
    if(winner_count < value):
        winner_count = value
        winner_name = key
print(f'------------------------')
print(f'Winner: {winner_name}')
print(f'------------------------')

# output the results to a file
results_file = os.path.join('Analysis', 'ElectionResults.txt')
with open(results_file, 'w+') as output:
    output.write('Election Results\n')
    output.write('-------------------------\n')
    output.write(f'Total Votes: {total_votes}\n')
    output.write(f'------------------------\n')
    for key, value in canidate_results.items():
        percentage_of_vote = (value / total_votes) * 100
        output.write(f'{key}: {round(percentage_of_vote, 3)}% ({value})\n')
    output.write(f'------------------------\n')
    output.write(f'Winner: {winner_name}\n')
    output.write(f'------------------------\n')