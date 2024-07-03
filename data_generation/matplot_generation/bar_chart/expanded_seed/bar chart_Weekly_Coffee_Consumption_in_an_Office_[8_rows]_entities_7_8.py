
import matplotlib.pyplot as plt

# Here's the data provided in a list of dictionaries
data = [
    {'Day': 'Monday', 'Number of Coffee Cups': 95},
    {'Day': 'Tuesday', 'Number of Coffee Cups': 105},
    {'Day': 'Wednesday', 'Number of Coffee Cups': 110},
    {'Day': 'Thursday', 'Number of Coffee Cups': 90},
    {'Day': 'Friday', 'Number of Coffee Cups': 120},
    {'Day': 'Saturday', 'Number of Coffee Cups': 45},
    {'Day': 'Sunday', 'Number of Coffee Cups': 30}
]

# Extracting days and corresponding coffee cups into separate lists
days = [entry['Day'] for entry in data]
coffee_cups = [entry['Number of Coffee Cups'] for entry in data]

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6)) # You can adjust the figure size as needed

# Generate a bar chart
ax.bar(days, coffee_cups, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2'])

# Adding labels and title
ax.set_xlabel('Day of the Week', fontsize=12)
ax.set_ylabel('Number of Coffee Cups Consumed', fontsize=12)
ax.set_title('Coffee Consumption by Day', fontsize=16)

# Adding value labels on each bar
for i in range(len(coffee_cups)):
    ax.text(i, coffee_cups[i] + 3, str(coffee_cups[i]), ha='center', va='bottom')

# Optional: Rotate the x-axis labels for better readability
plt.xticks(rotation=45)

# Optional: Add a grid for easier reading of values
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()  # Adjusts the plot to ensure everything fits without overlapping
plt.show()