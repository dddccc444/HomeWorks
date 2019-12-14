import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

total_months = 0
total_sum = 0
previous = 0
change = []
with open(csvpath, newline="") as Hmwk3Buget:
    csvreader = csv.reader(Hmwk3Buget, delimiter=",")
    next(csvreader)

    for row in csvreader:
        total_months = total_months + 1
        total_sum = total_sum + int(row[1])
        difference = int(row[1]) - previous
        previous = int(row[1])
        change.append(difference)
        average = sum(change)/len(change)
        profit_increase = max(change)  
        profit_decrease = min(change)
    print(total_months)
    print(total_sum)
    print(average)
    print(profit_increase)
    print(profit_decrease)


output_path = os.path.join("Resources", "BankOutput.csv")

with open(output_path, 'w', newline='') as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(["Total Months", "Total Sum", "Average", "Profit Decrease", "Profit Increase"])
    csvwriter.writerow([total_months, total_sum, average, profit_decrease, profit_increase])
    