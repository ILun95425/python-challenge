import os
import pandas as pd

fa= pd.read_csv('PyBank/Resources/budget_data.csv')

total_months= fa['Date'].nunique()

total= fa['Profit/Losses'].sum()

fa['Change']= fa['Profit/Losses'].diff()

average_change= fa['Change'].mean()

max_increase_month= fa.loc[fa['Change'].idxmax(), 'Date']

max_increase_amount= fa['Change'].max()

max_decrease_month= fa.loc[fa['Change'].idxmin(), 'Date']

max_decrease_amount= fa['Change'].min()

#print

print("Financial Analysis")
print("---------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {max_increase_month} (${max_increase_amount:.2f})")
print(f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease_amount:.2f})")


#addition

results= (
    "Financial Analysis\n"
    "---------------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {max_increase_month} (${max_increase_amount:.2f})\n"
    f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease_amount:.2f})"
)

print(results)


output_file= 'Financial Analysis.txt'
with open(output_file, 'w') as file: file.write(results)
