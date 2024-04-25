import os
import csv


filein = r"C:\Users\ilun1\OneDrive\桌面\GitHub\python-challenge\PyBank\Resources\budget_data.csv"


# define required variables

months = []
changes_pNl =[]
net_pNl = 0
avg_change = 0
counter_month = 0
grt_loss_month = 0
grt_profit_month = 0
current_month_pNl = 0
previous_month_pNl = 0
grt_loss = 0
grt_profit = 0


with open(filein, 'r') as input_data:
    read = csv.reader(input_data, delimiter= ',')

# skip the header

    header = next(read)
    

# loop csv

    for rows in read:
        months.append(rows[0])     
     
        net_pNl += int(rows[1])    
        
        counter_month  += 1        
        
        current_month_pNl = int(rows[1])      
       
        if(counter_month == 1) :
            previous_month_pNl = current_month_pNl       
            
        else :                                           
            change = current_month_pNl - previous_month_pNl              
            previous_month_pNl = current_month_pNl                       
            
            changes_pNl.append(change)                     
               

avg_change = round(sum(changes_pNl)/(counter_month-1),2)   
grt_profit = max(changes_pNl)                             
grt_profit_month = months[changes_pNl.index(grt_profit)+1]   
grt_loss = min(changes_pNl)                               
grt_loss_month = months[changes_pNl.index(grt_loss)+1] 

# print method 1

print("Financial Analysis")
print("---------------------------------")
print(f"Total Months: {counter_month}")
print(f"Total: ${net_pNl}")
print(f"Average Change: ${avg_change:.2f}")
print(f"Greatest Increase in Profits: {grt_profit_month} (${grt_profit})")
print(f"Greatest Decrease in Profits: {grt_loss_month} (${grt_loss})")


# output text file method 1

results= (
    "Financial Analysis\n"
    "---------------------------------\n"
    f"Total Months: {counter_month}\n"
    f"Total: ${net_pNl}\n"
    f"Average Change: ${avg_change:.2f}\n"
    f"Greatest Increase in Profits: {grt_profit_month} (${grt_profit:.2f})\n"
    f"Greatest Decrease in Profits: {grt_loss_month} (${grt_loss:.2f})\n"
)

print(results)

output_folder = r"C:\Users\ilun1\OneDrive\桌面\GitHub\python-challenge\PyBank"
output_file = os.path.join(output_folder, 'Financial Analysis.txt')

with open(output_file, 'w') as file: file.write(results)
