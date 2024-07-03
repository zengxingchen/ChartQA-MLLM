
import matplotlib.pyplot as plt

# Provided data
data = [{'Day': 'Monday', ' Cups of Coffee Consumed': 34},
        {'Day': 'Tuesday', ' Cups of Coffee Consumed': 30},
        {'Day': 'Wednesday', ' Cups of Coffee Consumed': 45},
        {'Day': 'Thursday', ' Cups of Coffee Consumed': 41},
        {'Day': 'Friday', ' Cups of Coffee Consumed': 50},
        {'Day': 'Monday', ' Cups of Coffee Consumed': 38},
        {'Day': 'Tuesday', ' Cups of Coffee Consumed': 31},
        {'Day': 'Wednesday', ' Cups of Coffee Consumed': 47},
        {'Day': 'Thursday', ' Cups of Coffee Consumed': 43},
        {'Day': 'Friday', ' Cups of Coffee Consumed': 52},
        {'Day': 'Monday', ' Cups of Coffee Consumed': 29},
        {'Day': 'Tuesday', ' Cups of Coffee Consumed': 33},
        {'Day': 'Wednesday', ' Cups of Coffee Consumed': 42},
        {'Day': 'Thursday', ' Cups of Coffee Consumed': 40},
        {'Day': 'Friday', ' Cups of Coffee Consumed': 51}]

# Group and sum the data by day
from collections import defaultdict

coffee_consumed_per_day = defaultdict(int)
for entry in data:
    coffee_consumed_per_day[entry['Day']] += entry[' Cups of Coffee Consumed']

# Convert the grouped data into a list sorted by weekdays
weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
sorted_data = [coffee_consumed_per_day[day] for day in weekday_order]

# Plotting the histogram
plt.figure(figsize=(10, 6)) # Set the size of the plot
plt.bar(weekday_order, sorted_data, color='skyblue') # Create a bar chart

# Customize the plot with diversified visual encodings
plt.title("Total Cups of Coffee Consumed Per Day", fontsize=16) # Add a title
plt.xlabel("Day of the Week", fontsize=14) # X-axis label
plt.ylabel("Cups of Coffee Consumed", fontsize=14) # Y-axis label
plt.xticks(fontsize=12, rotation=45) # Customizing the x-axis tick labels
plt.yticks(fontsize=12) # Customizing the y-axis tick labels

# Add data labels on each bar
for i, value in enumerate(sorted_data):
    plt.text(i, value + 2, str(value), ha='center', fontsize=10)

# Optionally, you can save the figure to a file
# plt.savefig('coffee_histogram.png', bbox_inches='tight')

# Show the plot
plt.show()