# Import dependencies
import os
import csv

# Define PyBank's variables
date = []
profit_loss_changes = []

count_date = 0
net_profit_loss = 0
previous_date_profit_loss = 0
current_date_profit_loss = 0
profit_loss_change = 0


# Path to collect data from the Resources folder
budget_data_csv_path = os.path.join("..", "Resources", "budget_data.csv")

# Open and read csv
with open(budget_data_csv_path,'r', encoding='utf-8') as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

# Read the header row first
    csv_header = next(csvfile)

   #print(f"Header: {csv_header}")

   # Read through each row of data after the header
    for row in csv_reader:

    # Count of data
        count_date += 1

# Net total amount of "Profit/Losses" over the entire period
        current_date_profit_loss = int(row[1])
        net_profit_loss += current_date_profit_loss

        if (count_date == 1):
              # Make the value of previous date to be equal to current date
              previous_date_profit_loss = current_date_profit_loss
              continue
        else:
              
             # Comput change in profit loss
             profit_loss_change = current_date_profit_loss

             # Append each date to the date []
             date.append(row[0])

             #Append each profit_loss_change to the profit_loss_changes[]
             profit_loss_changes.append(profit_loss_change)

             #make the current_date_loss to the pervious_date_profit_loss for the next loop
             previous_date_profit_loss = current_date_profit_loss
        
#sum and average of the changes in "Profit/Losses" over the entire period
sum_profit_loss = sum(profit_loss_changes)
average_profit_loss = round(sum_profit_loss/(count_date - 1), 2) 

# highest and lowest changes in "Profit/Losses" over the entire period
highest_change = max(profit_loss_changes)
lowest_change = min(profit_loss_changes)

# Locate the index value of highest and lowest changes in "Profit/Losses" over the entire period
highest_date_index = profit_loss_changes.index(highest_change)
lowest_date_index = profit_loss_changes.index(lowest_change)

# Assign best and worst date
best_date = date[highest_date_index]
worst_date = date[lowest_date_index]

##### Print the analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {count_date}")
print(f"Total:  ${net_profit_loss}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {best_date} (${highest_change})")
print(f"Greatest Decrease in Losses:  {worst_date} (${lowest_change})")


##### Export the results to a text file
budget_results = os.path.join ('..', 'Solution', 'budget_results.text')
with open(budget_results, "w") as outfile:
      
      outfile.write("Financial Analysis\n")
      outfile.write("----------------------------\n")
      outfile.write(f"Total Months:  {count_date}\n")
      outfile.write(f"Total:  ${net_profit_loss}\n")
      outfile.write(f"Average Change:  ${average_profit_loss}\n")
      outfile.write(f"Greatest Increase in Profits:  {best_date} (${highest_change})\n")
      outfile.write(f"Greatest Decrease in Losses:  {worst_date} (${lowest_change})\n")