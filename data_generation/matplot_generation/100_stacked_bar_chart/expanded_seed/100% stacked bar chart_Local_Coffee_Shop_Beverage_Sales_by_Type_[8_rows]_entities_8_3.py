
import matplotlib.pyplot as plt
import numpy as np

# Data from the provided table
data = [
    {'Beverage Type': 'Coffee', 'Monday': '30%', 'Tuesday': '35%', 'Wednesday': '40%', 'Thursday': '38%', 'Friday': '45%', 'Saturday': '25%', 'Sunday': '20%'},
    {'Beverage Type': 'Tea', 'Monday': '20%', 'Tuesday': '18%', 'Wednesday': '15%', 'Thursday': '16%', 'Friday': '10%', 'Saturday': '20%', 'Sunday': '25%'},
    {'Beverage Type': 'Juices', 'Monday': '10%', 'Tuesday': '12%', 'Wednesday': '10%', 'Thursday': '11%', 'Friday': '5%', 'Saturday': '15%', 'Sunday': '20%'},
    {'Beverage Type': 'Smoothies', 'Monday': '15%', 'Tuesday': '10%', 'Wednesday': '12%', 'Thursday': '12%', 'Friday': '10%', 'Saturday': '15%', 'Sunday': '15%'},
    {'Beverage Type': 'Soda', 'Monday': '10%', 'Tuesday': '10%', 'Wednesday': '8%', 'Thursday': '9%', 'Friday': '15%', 'Saturday': '10%', 'Sunday': '10%'},
    {'Beverage Type': 'Hot Chocolate', 'Monday': '5%', 'Tuesday': '5%', 'Wednesday': '5%', 'Thursday': '5%', 'Friday': '5%', 'Saturday': '5%', 'Sunday': '5%'},
    {'Beverage Type': 'Water', 'Monday': '5%', 'Tuesday': '5%', 'Wednesday': '5%', 'Thursday': '5%', 'Friday': '5%', 'Saturday': '5%', 'Sunday': '2%'},
    {'Beverage Type': 'Specialty Drinks', 'Monday': '5%', 'Tuesday': '5%', 'Wednesday': '5%', 'Thursday': '4%', 'Friday': '5%', 'Saturday': '5%', 'Sunday': '3%'}
]

# Extract weekday names and beverage types
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
beverage_types = [x['Beverage Type'] for x in data]

# Initialize the bottom array for stacking
bottoms = np.zeros(len(weekdays))

# Colors for each beverage type
colors = plt.cm.get_cmap('tab20', len(data))

# Start plotting
plt.figure(figsize=(12, 8))

# Loop over each beverage type and stack them
for idx, beverage in enumerate(data):
    percentages = [float(beverage[day].strip('%')) for day in weekdays]
    plt.bar(weekdays, percentages, bottom=bottoms, color=colors(idx), edgecolor='white', label=beverage['Beverage Type'])
    bottoms += np.array(percentages)  # Update the bottoms for the next stack

# Add some text for labels, title and custom x-axis tick labels, etc.
plt.xticks(weekdays)
plt.xlabel('Weekday')
plt.ylabel('Percentage')
plt.title('Beverage Sales Percentage by Weekday')
plt.legend()

# Customize the y-axis to show percentages
plt.yticks(np.arange(0, 101, 10), [f'{i}%' for i in range(0, 101, 10)])

# Show values on the bars
for i in range(len(weekdays)):
    total_percentage = 0
    for idx, beverage in enumerate(data):
        percent = float(beverage[weekdays[i]].strip('%'))
        height = total_percentage + percent / 2
        plt.text(i, height, f'{percent}%', ha='center', va='center', color='black')
        total_percentage += percent

# Show the plot
plt.tight_layout()
plt.show()