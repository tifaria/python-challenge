import os
import csv

budget_data_csv = os.path.join('budget_data.csv')

total_months = []
net_total = []
change = []


#loop for counting
with open(budget_data_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')
    #skip first row
    header = next(csvreader)

    for row in csvreader:
        #add to list
        total_months.append(row[0])
        #add to list
        net_total.append(int(row[1]))

    for i in range(0, len(net_total) - 1):
        change.append(int(net_total[i+1]) - int(net_total[i]))



    def average(numbers):
        value = sum(numbers)/len(numbers)
        return value
    
    #ask how to find average of changes


    greatest_increase = max(change)
    greatest_decrease = min(change)


    
#print total number of months
print(f'Total months: {len(total_months)}')
#print sum of values in net total list
print(f'Total: {sum(net_total)}')
print(average(change))
print(greatest_increase)
print(greatest_decrease)









