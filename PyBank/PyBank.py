#importing the necessary libraries
import os
import csv
import statistics

#getting the path set
csv_path = os.path.join("budget_data.csv")

#opening the CSV file
with open (csv_path, mode = "r", newline="") as csv_file:
    #reading the file
    csv_reader = csv.reader(csv_file)

    #designating the header
    csv_header = next(csv_reader)

    #creating the counters
    month_count = 0
    total = 0
    profits = []
    avg_change = []
    net_change_list = []
    month_of_change = []
    great_inc = ["",0]
    great_dec = ["",1000000]
    prev_net = int(row[1])
    #findig the counts
    for row in csv_reader:
        #calculatint the month count
        month_count += 1
        #calculating the total
        total  = total + int(row[1])

        #track the net change
        net_change = int(ow[1]) - prev_net
        prev_net = row[1]
        net_change_list.append(net_change)
        month_of_change.append(row[0])

        # greatest increase1
        if net_change > great_inc[1]:
            great_inc[0] = row[0]
            great_inc[1] = net_change

        #greatest decrease
        if net_change < great_dec[1]:
    
    #creating the readout
    line_1 = "Financial Analysis"
    line_2 = "~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~"
    line_3 = f"Toatal Months: {month_count}"
    line_4 = f"Total: ${total}"
    line_5 = f"Average Change: ${round(statistics.mean(avg_change),2)}"
    line_6 = f"Greatest Increase in Profits: (${great_inc_val})"
    line_7 = f"Greatest Decrease in Profits: (${great_dec_val})"

print(line_1 + "\n" + line_2 + "\n" + line_3 + "\n" + line_4 + 
"\n" + line_5 + "\n" + line_6 + "\n" + line_7)

with open ('financial_analysis.txt', mode = "w") as text:
    text.writelines(line_1 + "\n" + line_2 + "\n" + line_3 + "\n" + line_4 + 
"\n" + line_5 + "\n" + line_6 + "\n" + line_7)
