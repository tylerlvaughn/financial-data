import os
import csv

#Path to Collect Data from the Resources Folder
budget_csv = os.path.join('Resources', 'budget_data.csv')

#Open CSV and Read the File
with open(budget_csv, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    header = next(csvreader)

    print(f"Header: {header}")

    #Start "profit" and "months"
    profit = []
    months = []

    #Loop Through Data
    for rows in csvreader:
        months.append(rows[0])
        profit.append(int(rows[1]))   

    #Revenue Change
    revenue = []

    for x in range(1, len(profit)):
        revenue.append((int(profit[x]) - int(profit[x-1])))
    
    #Calculate Average Revenue Change
    revenue_average = sum(revenue) / len(revenue)

    #Calculate Total Months
    total_months = len(months) 

    #Greatest Increase in Revenue
    greatest_increase = max(revenue)
    #Greatest Decrease in Revenue
    greatest_decrease = min(revenue)    

    #Print Results
    print("Financial Analysis")

    print("----------------------------------------------------")

    print("Total Months: " + str(total_months))

    print("Total: " + "$" + str(sum(profit)))

    print("Average Change: " + "$" + str(revenue_average))

    print("Greatest Increase in Profits: " + str(months[revenue.index(max(revenue))+1]) + " $" + str(greatest_increase))

    print("Greatest Decrease in Profits: " + str(months[revenue.index(min(revenue))+1]) + " $" + str(greatest_decrease))


    #Create Text File from Results

    file = open("output.txt","w")

    file.write("Financial Analysis" + "\n")

    file.write("---------------------------------------------------" + "\n")

    file.write("Total Months: " + str(total_months) + "\n")

    file.write("Total: " + "$" + str(sum(profit)) + "\n")

    file.write("Average Change: " + "$" + str(revenue_average) + "\n")

    file.write("Greatest Increase in Profits: " + str(months[revenue.index(max(revenue))+1]) + " $" + str(greatest_increase) + "\n")

    file.write("Greatest Decrease in Profits: " + str(months[revenue.index(min(revenue))+1]) + " $" + str(greatest_decrease) + "\n")

    file.close()