import os
import csv

budget_data_csv = os.path.join('budget_data.csv')

total_months = []
net_total = []
change = []
increase_month = 0
decrease_month = 0
greatest_increase = 0
greatest_decrease = 0


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
        #find greatest increase month
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            increase_month = row[0]
        #find greatest decrease month
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            decrease_month = row[0]
    #calculate de change in profit/losses
    for i in range(0, len(net_total) - 1):
        change.append(int(net_total[i+1]) - int(net_total[i]))
    #create average function
    def average(numbers):
        value = sum(numbers)/len(numbers)
        return value
    
    greatest_increase = max(change)
    greatest_decrease = min(change)


#Print final report
print("Financial Analysis")   
print("------------------------")
print(f'Total months: {len(total_months)}')
print(f'Total: ${sum(net_total)}')
print(f'Average change: ${average(change)}')
print(f'Greatest Increase in Profits: {increase_month}  (${greatest_increase})')
print(f'Greatest decrease in Profits: {decrease_month}  (${greatest_decrease})')










