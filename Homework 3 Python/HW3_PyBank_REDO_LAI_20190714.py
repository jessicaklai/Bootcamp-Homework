#!/usr/bin/env python
# coding: utf-8

# ## PyBank
# 
# • In this challenge, you are tasked with creating a Python script for analyzing the financial records 
# of your company. You will give a set of financial data called budget_data.csv. The dataset is composed 
# of two columns: Date and Profit/Losses. (Thankfully, your company has rather lax standards for 
# accounting so the records are simple.)
# 
# • Your task is to create a Python script that analyzes the records to calculate each of the following:
# 
# o The total number of months included in the dataset
# o The net total amount of "Profit/Losses" over the entire period
# o The average of the changes in "Profit/Losses" over the entire period
# o The greatest increase in profits (date and amount) over the entire period 
# o The greatest decrease in losses (date and amount) over the entire period
# 
# • As an example, your analysis should look similar to the one below:
# 
# Financial Analysis
# ----------------------------
# #Total Months: 86
# #Total: $38382578
# #Average Change: $-2315.12
# #Greatest Increase in Profits: Feb-2012 ($1926159)
# #Greatest Decrease in Profits: Sep-2013 ($-2196167)
# 
# In addition, your final script should both print the analysis to the terminal and export a
# text file with the results.

# In[406]:


# Import dependencies
import csv
import os


# In[407]:


pybank = os.path.join("budget-data.csv")


# In[408]:


# Create lists to store info
months = []
# for something I attempted, but didn't work: revenue_index = []
pnl_changes = []
revenue=[]

# For CSV File
csv_total_months = []
csv_net_total = [] 
csv_avg_change = [] 
csv_greatest_profit =[] 
csv_greatest_loss =[] 


# In[409]:


with open (pybank, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader, None)
    
    for row in csvreader:
        # Gather months and revenues to lists and 
        months.append(row[0])
        revenue.append(int(row[1]))

        # I used this method for PyPoll to index the candidates/vote counts, so I 
        # tried to use it here to get sum of months while tying them to monthly revenue; 
        # figured I could use this for printing largest profit and largest loss. 
        # But I couldn't get this to work.
        #revenue = row[1]
        #if revenue in revenue_index:
            #month_index = revenues_index.index(revenue)
            #months[revenues_index] += 1
            
            
        change = int(row[1]) - int(monthly_change)
        monthly_change = row[1]
        pnl_changes.append(change)
        #print(pnl_changes)

# Greatest loss and profit
greatest_profit = max(pnl_changes)
csv_greatest_profit.append(greatest_profit)
#print("Greatest prof: " + str(greatest_profit))
greatest_loss = min(pnl_changes)    
csv_greatest_loss.append(greatest_loss)
#print("Greatest loss: " + str(greatest_loss))

# Net total of revenue
net_total = sum(revenue)
csv_net_total.append(net_total)
#print("Net total: " + str(net_total))

# Total months
total_months = len(months)
csv_total_months.append(total_months)
#print("Total Months: " + str(total_months))

# Average change
del pnl_changes[0]
#print("PNL Changes: " + str(pnl_changes))

sum_changes = sum(pnl_changes)
#print("Sum Change: " + str(sum_changes))

avg_change = round(sum_changes / len(pnl_changes),2)
csv_avg_change.append(avg_change)
#print("Average Change: " + str(avg_change))


# In[410]:


print("Financial Analysis")
print("-----------------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(net_total))
print("Average Change: $" + str(avg_change))
# JESS NOTES: Tried different variations to get respective months to print but it didn't work 
print("Greatest Increase in Profits: $" + str(greatest_profit))
print("Greatest Decrease in Profits: $" + str(greatest_loss))


# In[411]:


# Zip and create output file

clean_csv = zip(csv_total_months, csv_net_total, csv_avg_change, csv_greatest_profit, csv_greatest_loss)

output_file = os.path.join("PyBank_Analysis.csv")

with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    
    writer.writerow(["Total Months", "Total", "Average Change", "Greatest Increase in Profits", "Greatest Decrease in Profits"])
    
    writer.writerows(clean_csv)


# In[ ]:




