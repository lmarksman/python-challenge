# Matthew Lett
# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

#initialize variables
month_count = 0
total_amount = 0
current_month_amount = 0
previous_month_amount = 0
amount_change_list = []
average_change = 0
highest_change = {'Month': 'None',
                  'Change': 0}
lowest_change = {'Month': 'None',
                  'Change': 0}

csvpath = os.path.join('Resources', 'budget_data.csv')


#open the file for reading
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    
    for row in csvreader:
        # count the total months
        month_count += 1

        current_month_amount = int(row[1])
        
        # add the total amount for all profit / losses
        total_amount += current_month_amount

        # We don't want to see a change for the first month
        if month_count == 1:
            previous_month_amount = current_month_amount 
        
        # keep a list of all of the changes
        amount_change_list.append(current_month_amount - previous_month_amount)

        # see if the change is the highest change. store the results
        if(amount_change_list[month_count - 1] > highest_change['Change']):
            highest_change['Month'] = row[0]
            highest_change['Change'] = amount_change_list[month_count - 1]
        
        # see if the change is the lowest change. store the results
        if(amount_change_list[month_count - 1] < lowest_change['Change']):
            lowest_change['Month'] = row[0]
            lowest_change['Change'] = amount_change_list[month_count - 1]
        
        
        # Set the amount for the next loop
        previous_month_amount = current_month_amount

# total profit / loss 
total_change = sum(amount_change_list)    

# average change
average_change = total_change / (len(amount_change_list) - 1)
 

print('Financial Analysis')
print('---------------------')
print(f'Total Months: {month_count}')
print(f'Total: ${total_amount}')
print(f'Average Change: ${str(round(average_change, 2))}')
print(f'Greatest Increase in Profits: {highest_change["Month"]} (${highest_change["Change"]})')
print(f'Greatest Decrease in Profits: {lowest_change["Month"]} (${lowest_change["Change"]})')

# output the results to a file
results_file = os.path.join('Analysis', 'AnalysisResults.txt')
with open(results_file, 'w+') as output:
    output.write('Financial Analysis\n')
    output.write('---------------------\n')
    output.write(f'Total Months: {month_count}\n')
    output.write(f'Total: ${total_amount}\n')
    output.write(f'Average Change: ${str(round(average_change, 2))}\n')
    output.write(f'Greatest Increase in Profits: {highest_change["Month"]} (${highest_change["Change"]})\n')
    output.write(f'Greatest Decrease in Profits: {lowest_change["Month"]} (${lowest_change["Change"]})')