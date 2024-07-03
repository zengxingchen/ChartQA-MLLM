
import matplotlib.pyplot as plt

# Data for the new chart
data = [
    {'Day': 'Monday', 'Technology Count': 56},
    {'Day': 'Tuesday', 'Technology Count': 73},
    {'Day': 'Wednesday', 'Technology Count': 68},
    {'Day': 'Thursday', 'Technology Count': 85},
    {'Day': 'Friday', 'Technology Count': 95},
    {'Day': 'Saturday', 'Technology Count': 78},
    {'Day': 'Sunday', 'Technology Count': 65}
]

# Extracting the days and technology counts into separate lists
days = [entry['Day'] for entry in data]
technology_counts = [entry['Technology Count'] for entry in data]

# Creating the line chart
plt.figure(figsize=(12, 6))  # Set the size of the figure

# Plot the data
plt.plot(days, technology_counts, color='#1f77b4', linestyle='-', marker='o', linewidth=2, markersize=8, label="Technology Count per Day")

# Add titles and labels
plt.title('Technology Count Per Day in Future Technologies', fontsize=18, loc='center')
plt.xlabel('Day of the Week', fontsize=14)
plt.ylabel('Technology Count', fontsize=14)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

# Include grid lines
plt.grid(True, linestyle='--', linewidth=0.5, color='grey')

# Add more diversified visual encoding such as text annotations for the data points
for i, count in enumerate(technology_counts):
    plt.text(days[i], count + 3, str(count), ha='center', color='black')

# Highlight the max and min technology counts
max_count = max(technology_counts)
min_count = min(technology_counts)
plt.axhline(max_count, color='#2ca02c', linestyle='--', linewidth=1)
plt.axhline(min_count, color='#d62728', linestyle='--', linewidth=1)

# Add a legend
plt.legend(loc='upper left')

# Show the plot
plt.tight_layout()  # Adjust the plot to ensure everything fits without overlapping
plt.show()