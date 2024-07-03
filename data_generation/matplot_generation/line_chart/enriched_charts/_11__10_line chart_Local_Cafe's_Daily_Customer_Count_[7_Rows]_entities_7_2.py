
import matplotlib.pyplot as plt

# Data for the new chart
data = [
    {'Day': 'Monday', 'Stress Level': 45},
    {'Day': 'Tuesday', 'Stress Level': 60},
    {'Day': 'Wednesday', 'Stress Level': 50},
    {'Day': 'Thursday', 'Stress Level': 70},
    {'Day': 'Friday', 'Stress Level': 80},
    {'Day': 'Saturday', 'Stress Level': 55},
    {'Day': 'Sunday', 'Stress Level': 65}
]

# Extracting the days and stress levels into separate lists
days = [entry['Day'] for entry in data]
stress_levels = [entry['Stress Level'] for entry in data]

# Creating the line chart
plt.figure(figsize=(14, 7))  # Set the size of the figure

# Plot the data
plt.plot(days, stress_levels, color='#ff5733', linestyle='-', marker='s', linewidth=2, markersize=8, label="Stress Level per Day")

# Add titles and labels
plt.title('Daily Stress Levels Measured in a Week', fontsize=18, loc='center')
plt.xlabel('Day of the Week', fontsize=14)
plt.ylabel('Stress Level', fontsize=14)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

# Include grid lines
plt.grid(True, linestyle='--', linewidth=0.5, color='grey')

# Add text annotations for the data points
for i, level in enumerate(stress_levels):
    plt.text(days[i], level + 3, str(level), ha='center', color='black')

# Highlight the max and min stress levels
max_level = max(stress_levels)
min_level = min(stress_levels)
plt.axhline(max_level, color='#2ca02c', linestyle='--', linewidth=1)
plt.axhline(min_level, color='#d62728', linestyle='--', linewidth=1)

# Add a legend
plt.legend(loc='upper right')

# Show the plot
plt.tight_layout()  # Adjust the plot to ensure everything fits without overlapping
plt.show()