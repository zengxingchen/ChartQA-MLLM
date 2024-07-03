
import matplotlib.pyplot as plt

# Data for the new chart
data = [
    {'Day': 'Monday', 'Productivity Level': 85},
    {'Day': 'Tuesday', 'Productivity Level': 80},
    {'Day': 'Wednesday', 'Productivity Level': 75},
    {'Day': 'Thursday', 'Productivity Level': 78},
    {'Day': 'Friday', 'Productivity Level': 72},
    {'Day': 'Saturday', 'Productivity Level': 68},
    {'Day': 'Sunday', 'Productivity Level': 70}
]

# Extracting the days and productivity levels into separate lists
days = [entry['Day'] for entry in data]
productivity_levels = [entry['Productivity Level'] for entry in data]

# Creating the line chart
plt.figure(figsize=(12, 6))  # Set the size of the figure

# Plot the data
plt.plot(days, productivity_levels, color='#1f77b4', linestyle='-', marker='o', linewidth=2, markersize=8, label="Productivity Level per Day")

# Add titles and labels
plt.title('Weekly Productivity Levels', fontsize=18, loc='left')
plt.xlabel('Day of the Week', fontsize=14)
plt.ylabel('Productivity Level', fontsize=14)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

# Include grid lines
plt.grid(True, linestyle='--', linewidth=0.5, color='grey')

# Add text annotations for the data points
for i, level in enumerate(productivity_levels):
    plt.text(days[i], level - 3, str(level), ha='center', color='black')

# Highlight the max and min productivity levels
max_level = max(productivity_levels)
min_level = min(productivity_levels)
plt.axhline(max_level, color='#2ca02c', linestyle='--', linewidth=1)
plt.axhline(min_level, color='#d62728', linestyle='--', linewidth=1)

# Add a legend
plt.legend(loc='upper right')

# Adjust y-axis to be inverted
plt.gca().invert_yaxis()

# Show the plot
plt.tight_layout()  # Adjust the plot to ensure everything fits without overlapping
plt.show()