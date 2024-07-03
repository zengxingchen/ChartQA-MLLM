
import matplotlib.pyplot as plt

# Data for the new chart
data = [
    {'Day': 'Monday', 'Reading Count': 150},
    {'Day': 'Tuesday', 'Reading Count': 130},
    {'Day': 'Wednesday', 'Reading Count': 110},
    {'Day': 'Thursday', 'Reading Count': 115},
    {'Day': 'Friday', 'Reading Count': 95},
    {'Day': 'Saturday', 'Reading Count': 85},
    {'Day': 'Sunday', 'Reading Count': 75}
]

# Extracting the days and reading counts into separate lists
days = [entry['Day'] for entry in data]
reading_counts = [entry['Reading Count'] for entry in data]

# Creating the line chart
plt.figure(figsize=(10, 5))  # Set the size of the figure

# Plot the data
plt.plot(days, reading_counts, color='#FF6347', linestyle='-', marker='o', linewidth=2, markersize=8, label="Reading Count per Day")

# Add titles and labels
plt.title('Reading Count Per Day in Literature & Writing', fontsize=18, loc='right')
plt.xlabel('Day of the Week', fontsize=14)
plt.ylabel('Reading Count', fontsize=14)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

# Include grid lines
plt.grid(True, linestyle='--', linewidth=0.5, color='grey')

# Add text annotations for the data points
for i, count in enumerate(reading_counts):
    plt.text(days[i], count + 3, str(count), ha='center', color='black')

# Highlight the max and min reading counts
max_count = max(reading_counts)
min_count = min(reading_counts)
plt.axhline(max_count, color='#2ca02c', linestyle='--', linewidth=1)
plt.axhline(min_count, color='#d62728', linestyle='--', linewidth=1)

# Invert the y-axis
plt.gca().invert_yaxis()

# Add a legend
plt.legend(loc='upper left')

# Show the plot
plt.tight_layout()  # Adjust the plot to ensure everything fits without overlapping
plt.show()