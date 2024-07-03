
import matplotlib.pyplot as plt

# Data from your provided chart
data = [{'Day': 'Monday', 'Customer Count': 87},
        {'Day': 'Tuesday', 'Customer Count': 92},
        {'Day': 'Wednesday', 'Customer Count': 78},
        {'Day': 'Thursday', 'Customer Count': 83},
        {'Day': 'Friday', 'Customer Count': 109},
        {'Day': 'Saturday', 'Customer Count': 142},
        {'Day': 'Sunday', 'Customer Count': 131}]

# Extracting the days and customer counts into separate lists
days = [entry['Day'] for entry in data]
customer_counts = [entry['Customer Count'] for entry in data]

# Creating the line chart
plt.figure(figsize=(10, 5)) # Set the size of the figure

# Plot the data
plt.plot(days, customer_counts, color='blue', linestyle='-', marker='o', linewidth=2, markersize=8, label="Customer Count per Day")

# Add titles and labels
plt.title('Customer Count Per Day', fontsize=18)
plt.xlabel('Day of the Week', fontsize=14)
plt.ylabel('Customer Count', fontsize=14)
plt.xticks(rotation=45) # Rotate x-axis labels for better readability

# Include grid lines
plt.grid(True, linestyle='--', linewidth=0.5, color='grey')

# Add more diversified visual encoding such as text annotations for the data points
for i, count in enumerate(customer_counts):
    plt.text(days[i], count + 3, str(count), ha='center', color='black')

# Highlight the max and min customer counts
max_count = max(customer_counts)
min_count = min(customer_counts)
plt.axhline(max_count, color='green', linestyle='--', linewidth=1)
plt.axhline(min_count, color='red', linestyle='--', linewidth=1)

# Add a legend
plt.legend()

# Show the plot
plt.tight_layout() # Adjust the plot to ensure everything fits without overlapping
plt.show()