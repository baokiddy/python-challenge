#You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses.
#Import important modules needed for this work
import os
import csv
import codecs


#Open and read file for analysis
csvpath = os.path.join("Resources", "budget_data.csv")


#Create empty lists for each column
date = []
profit_loss = []

with open(csvpath, newline='', encoding='utf8') as csvfile:

    #Read and pull data
    csvreader = csv.reader(csvfile, delimiter=',')

    # Then store the contents of the date and profit/loss columns.
    for row in csvreader:
        
            date.append(row[0])
            profit_loss.append(row[1])
        
    del date[0]
    del profit_loss[0]

    
#The total number of months included in the dataset
month_count = []

for m in date:
    month = m.split('-', 1)[0]
    
    month_count.append(month)
     
num_month = len(month_count)


#The total net amount of "Profit/Losses" over the entire period
total = 0

for i in profit_loss:
    
    total = total + int(i)


#The average change in "Profit/Losses" between months over the entire period
initial = profit_loss[0]

change_list = []

for j in profit_loss:
    
    change = int(j) - int(initial)
    
    initial = j
    
    change_list.append(change)
    
del change_list[0]
    
avg_change = sum(change_list)/len(change_list)


#The greatest increase in profits (date and amount) over the entire period
count = 0
rec_profit = int(change_list[0])

for amount in change_list:
    
    value = int(amount)
    count = count + 1
    
    if value> rec_profit:
        rec_profit = value
        inc_date = date[count]


#The greatest decrease in losses (date and amount) over the entire period
count = 0
rec_loss = int(change_list[0])

for amount in change_list:
    
    value = int(amount)
    count = count + 1
    
    if value< rec_loss:
        rec_loss = value
        dec_date = date[count]


#Print out all recorded answers
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {num_month}')
print(f'Total: {total}') 
print(f'Average  Change: {round(avg_change, 2)}')
print(f'Greatest Increase in Profits: {inc_date} (${rec_profit})')
print(f'Greatest Decrease in Profits: {dec_date} (${rec_loss})')


#Export a text file with the results
# save the output file path
output_file = os.path.join("financial_analysis.csv")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Financial Analysis"])
    writer.writerow(["Total Months", num_month])
    writer.writerow(["Total", total])
    writer.writerow(["Average  Change", round(avg_change, 2)])
    writer.writerow(["Greatest Increase in Profits", inc_date, rec_profit])
    writer.writerow(["Greatest Decrease in Profits", dec_date, rec_loss])