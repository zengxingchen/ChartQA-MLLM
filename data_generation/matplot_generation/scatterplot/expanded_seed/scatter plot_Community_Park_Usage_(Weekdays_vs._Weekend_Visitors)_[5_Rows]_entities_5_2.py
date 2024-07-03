
import matplotlib.pyplot as plt

# The provided chart table data
data = [
    {'Day': 'Monday', 'Weekday Visitors (count)': 120, 'Weekend Visitors (count)': 0},
    {'Day': 'Tuesday', 'Weekday Visitors (count)': 87, 'Weekend Visitors (count)': 0},
    {'Day': 'Wednesday', 'Weekday Visitors (count)': 103, 'Weekend Visitors (count)': 0},
    {'Day': 'Saturday', 'Weekday Visitors (count)': 0, 'Weekend Visitors (count)': 240},
    {'Day': 'Sunday', 'Weekday Visitors (count)': 0, 'Weekend Visitors (count)': 312}
]

# Prepare the data for plotting
days = [entry['Day'] for entry in data]
weekday_counts = [entry['Weekday Visitors (count)'] for entry in data]
weekend_counts = [entry['Weekend Visitors (count)'] for entry in data]

# Create a scatter plot using the matplotlib
plt.figure(figsize=(10, 6))

# Scatter plot for weekday visitors
for i, day in enumerate(days):
    if weekday_counts[i] > 0:  # Plot only if there's a weekday count
        plt.scatter(day, weekday_counts[i], color='blue', label='Weekday Visitors' if i == 0 else "")

# Scatter plot for weekend visitors
for i, day in enumerate(days):
    if weekend_counts[i] > 0:  # Plot only if there's a weekend count
        plt.scatter(day, weekend_counts[i], color='red', label='Weekend Visitors' if i == 3 else "")

# Adding Titles and Labels
plt.title('Visitor Counts by Day')
plt.xlabel('Day of Week')
plt.ylabel('Number of Visitors')

# Add grid for better readability
plt.grid(True)

# Adding a legend, but only if there's at least one entry for weekday and weekend
if any(weekday_counts):
    plt.legend(loc='upper left')

# Show the plot with all the visitor data points
plt.show()