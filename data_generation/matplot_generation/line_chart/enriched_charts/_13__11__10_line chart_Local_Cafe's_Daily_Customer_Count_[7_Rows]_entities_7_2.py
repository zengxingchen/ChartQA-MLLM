
import matplotlib.pyplot as plt

# Data for the new chart
data = [
    {'Day': 'Monday', 'Exercise Duration (minutes)': 30},
    {'Day': 'Tuesday', 'Exercise Duration (minutes)': 45},
    {'Day': 'Wednesday', 'Exercise Duration (minutes)': 50},
    {'Day': 'Thursday', 'Exercise Duration (minutes)': 40},
    {'Day': 'Friday', 'Exercise Duration (minutes)': 60},
    {'Day': 'Saturday', 'Exercise Duration (minutes)': 20},
    {'Day': 'Sunday', 'Exercise Duration (minutes)': 25}
]

# Extracting the days and exercise durations into separate lists
days = [entry['Day'] for entry in data]
exercise_durations = [entry['Exercise Duration (minutes)'] for entry in data]

# Creating the line chart
plt.figure(figsize=(12, 6))  # Set the size of the figure

# Plot the data
plt.plot(days, exercise_durations, color='#1f77b4', linestyle='-', marker='o', linewidth=2, markersize=8, label="Exercise Duration per Day")

# Add titles and labels
plt.title('Weekly Exercise Duration', fontsize=18, loc='center')
plt.xlabel('Day of the Week', fontsize=14)
plt.ylabel('Exercise Duration (minutes)', fontsize=14)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

# Include grid lines
plt.grid(True, linestyle='--', linewidth=0.5, color='grey')

# Add text annotations for the data points
for i, duration in enumerate(exercise_durations):
    plt.text(days[i], duration + 2, str(duration), ha='center', color='black')

# Highlight the max and min exercise durations
max_duration = max(exercise_durations)
min_duration = min(exercise_durations)
plt.axhline(max_duration, color='#2ca02c', linestyle='--', linewidth=1)
plt.axhline(min_duration, color='#d62728', linestyle='--', linewidth=1)

# Add a legend
plt.legend(loc='upper left')

# Show the plot
plt.tight_layout()  # Adjust the plot to ensure everything fits without overlapping
plt.show()