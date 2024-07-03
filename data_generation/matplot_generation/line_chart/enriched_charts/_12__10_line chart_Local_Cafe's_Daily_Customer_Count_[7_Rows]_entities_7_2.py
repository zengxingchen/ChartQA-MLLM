
import matplotlib.pyplot as plt

# Data for the new chart
data = [
    {'Day': 'Monday', 'Income': 120},
    {'Day': 'Tuesday', 'Income': 105},
    {'Day': 'Wednesday', 'Income': 135},
    {'Day': 'Thursday', 'Income': 90},
    {'Day': 'Friday', 'Income': 150},
    {'Day': 'Saturday', 'Income': 180},
    {'Day': 'Sunday', 'Income': 160}
]

# Extracting the days and income into separate lists
days = [entry['Day'] for entry in data]
income = [entry['Income'] for entry in data]

# Creating the line chart
plt.figure(figsize=(14, 8))  # Set the size of the figure

# Plot the data
plt.plot(days, income, color='#FF5733', linestyle='-', marker='s', linewidth=2, markersize=8, label="Daily Income")

# Add titles and labels
plt.title('Daily Income in Business Ventures', fontsize=18, loc='center')
plt.xlabel('Day of the Week', fontsize=14)
plt.ylabel('Income ($)', fontsize=14)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

# Include grid lines
plt.grid(True, linestyle='--', linewidth=0.5, color='grey')

# Add more diversified visual encoding such as text annotations for the data points
for i, count in enumerate(income):
    plt.text(days[i], count + 3, str(count), ha='center', color='black')

# Highlight the max and min income
max_income = max(income)
min_income = min(income)
plt.axhline(max_income, color='#2ca02c', linestyle='--', linewidth=1)
plt.axhline(min_income, color='#d62728', linestyle='--', linewidth=1)

# Add a legend
plt.legend(loc='upper left')

# Show the plot
plt.tight_layout()  # Adjust the plot to ensure everything fits without overlapping
plt.show()