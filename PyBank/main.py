# Import modules
import os
import csv

# Set path for file
budget_csv = os.path.join("Resources", "budget_data.csv")

# Define financial analysis function
def financial_analysis():
    
    # Open the CSV file in read mode
    with open(budget_csv, 'r') as csvfile:

        # Split the data on commas
        budget = csv.reader(csvfile, delimiter=',')

        # Skip the header
        header = next(budget)
        
        # Create lists to host the data elements
        months = []
        profit_loss = []

        # From the CSV, assign elements to the lists
        for row in budget:
            months.append(row[0])
            profit_loss.append(int(row[1]))

        # Create a list of changes    
        difference = [profit_loss[i+1]-profit_loss[i] for i in range(len(profit_loss)-1)]
        
        # Find maximum change
        max_index = difference.index(max(difference))
        
        # Find minimum change
        min_index = difference.index(min(difference))
        
        # Find average of changes
        avg_difference = sum(difference)/len(difference)

        # Create output strings
        analysis = (
        'Financial Analysis\n'
        '-----------------------------------\n'
        f'Total Months: {len(months)}\n'  
        f'Total: ${sum(profit_loss)}\n'
        f'Average Change: ${round(avg_difference, 2)}\n'
        f'Greatest Increase in Profits: {months[max_index + 1]} (${max(difference)})\n'
        f'Greatest Decrease in Profits: {months[min_index + 1]} (${min(difference)})\n'
        )

        # Print analysis to terminal
        print(analysis)
        
        # Export text file with analysis results
        file = open("financial_analysis.txt","w")
        file.write(analysis)
        file.close()

# Run financial analysis function        
financial_analysis()