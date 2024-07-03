
import matplotlib.pyplot as plt

# Data from the provided table
data = [
    {'Day': 'Monday', 'Total Sales ($)': 1575},
    {'Day': 'Tuesday', 'Total Sales ($)': 1832},
    {'Day': 'Wednesday', 'Total Sales ($)': 1710},
    {'Day': 'Thursday', 'Total Sales ($)': 1625},
    {'Day': 'Friday', 'Total Sales ($)': 2045}
]

# Extracting the 'Day' and 'Total Sales ($)' information from the data
days = [item['Day'] for item in data]
sales = [item['Total Sales ($)'] for item in data]

# Plotting the area chart
plt.figure(figsize=(10, 6))  # setting the figure size
plt.fill_between(days, sales, color='skyblue', alpha=0.4)  # fill area under the line
plt.plot(days, sales, color='Slateblue', alpha=0.6, marker='o')  # line chart settings

# Additional visual encodings for aesthetically enhancing the plot
plt.title('Total Sales by Day', fontsize=18)  # setting the title of the plot
plt.xlabel('Day of the Week', fontsize=14)  # setting the x-axis label
plt.ylabel('Total Sales ($)', fontsize=14)  # setting the y-axis label
plt.grid(True, which='both', linestyle='--', linewidth=0.5)  # adding grid lines
plt.xticks(fontsize=12)  # setting font size for x-axis tick labels
plt.yticks(fontsize=12)  # setting font size for y-axis tick labels

# Highlighting each data point on the plot
for i in range(len(days)):
    plt.text(days[i], sales[i] + 50, f"${sales[i]}", ha='center', va='bottom', fontsize=10, color='black')

# Show the plot
plt.tight_layout()  # this ensures the plot is not cut off when saved or viewed
plt.show()