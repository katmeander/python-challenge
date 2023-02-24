import os
import csv
#import modules

budget_csv_path = os.path.join("Resources", "budget_data.csv")
#create the path to the csv file

month_list = []
profit_loss_list = []
#create empty lists

with open(budget_csv_path) as csvfile:
#open the csv file from the defined path
        csvreader = csv.reader(csvfile, delimiter=",")
        #this creates the reader and denotes the comma delimiter
        csv_data = next(csv.reader(csvfile))
        #this stores header row
        
        for row in csvreader:
                month_list.append(row[0])
                #add dates to the list from csv reader

                profit_loss_list.append(row[1])
                #add numberical strings to the list from csv reader

        total_months = len(month_list)
        #gets the total number of months
                
        for i in range(0, len(profit_loss_list)):
                profit_loss_list[i] = int(profit_loss_list[i])
                #change numberical strings in list to integers
        
        total_profit_loss = sum(profit_loss_list)
        #sum the total of profits and losses

        change_list = []
       
        for b in range(0, len(profit_loss_list)-1):
                change = profit_loss_list[b+1] - profit_loss_list[b] 
                #get the change in profit or loss from month to month 
                #the total number of entries in the list minus 1 because
                #this is arithmatic
                change_list.append(change)
                #add the change to the change list

        average_change = sum(change_list) / (total_months - 1)
         #below change average change to currency
        average_change = round(average_change, 2)

        greatest_increase = max(change_list)

        increase_index = change_list.index(greatest_increase)

        increase_month = month_list[increase_index + 1]
        
        greatest_decrease = min(change_list)

        decrease_index = change_list.index(greatest_decrease)

        decrease_month = month_list[decrease_index + 1]
        
print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})")

with open("financial_analysis.txt", "w") as text:
        text.write("Financial Analysis")
        text.write('\n')
        text.write("------------------------------")
        text.write('\n')
        text.write(f"Total Months: {total_months}")
        text.write('\n')
        text.write(f"Total: ${total_profit_loss}")
        text.write('\n')
        text.write(f"Average Change: ${average_change}")
        text.write('\n')
        text.write(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})")
        text.write('\n')
        text.write(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})")