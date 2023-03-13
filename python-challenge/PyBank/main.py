# import pandas

import pandas as pd

# read in data file as a dataframe

budget_df = pd.read_csv("/Users/nels.jacobson2/Desktop/Analytics_Class_Folder/031323/python-challenge/PyBank/Resources/budget_data.csv")
budget_df.head()

# get the total number of months

num_months = budget_df['Date'].count()
num_months

# get the net total amount of "Profit/Losses" over the period

net_profit = budget_df['Profit/Losses'].sum()
net_profit

# The changes in "Profit/Losses" over the entire period

profit_losses = budget_df['Profit/Losses']
changes = profit_losses.diff()
profit_losses.diff()

# The average of those changes

avg_change = changes.mean()
avg_change

# The greatest increase in profits (date and amount) over the entire period

greatest_increase = profit_losses.max()
increase_date = budget_df.loc[profit_losses.idxmax(), 'Date']

# The greatest decrease in profits (date and amount) over the entire period

greatest_decrease = profit_losses.min()
decrease_date = budget_df.loc[profit_losses.idxmin(), 'Date']

# Print analysis to terminal

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {num_months}")
print(f"Total: ${net_profit}")
print(f"Average Change: ${round(avg_change, 2)}")
print(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})")

# Set the path for the output file
output_path = "/Users/nels.jacobson2/Desktop/Analytics_Class_Folder/031323/python-challenge/PyBank/Analysis/financial_analysis.txt"

# Open the output file
with open(output_path, 'w') as file:
    # Write the analysis results to the file
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {num_months}\n")
    file.write(f"Total: ${net_profit}\n")
    file.write(f"Average Change: ${round(avg_change, 2)}\n")
    file.write(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})\n")
