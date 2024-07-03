
import matplotlib.pyplot as plt
import numpy as np

# Provided data
parks_data = [
    {'Park Name': 'Riverside Park', 'Weekday Visitors': 250, 'Average Visit Duration (minutes)': 30, 'Weekend Visitors': 800, 'Satisfaction Rating (1-5 scale)': 4.7, 'Green Space (acres)': 22},
    {'Park Name': 'Maple Grove Park', 'Weekday Visitors': 150, 'Average Visit Duration (minutes)': 25, 'Weekend Visitors': 500, 'Satisfaction Rating (1-5 scale)': 4.3, 'Green Space (acres)': 15},
    {'Park Name': 'Central Park', 'Weekday Visitors': 600, 'Average Visit Duration (minutes)': 45, 'Weekend Visitors': 2500, 'Satisfaction Rating (1-5 scale)': 4.9, 'Green Space (acres)': 50},
    {'Park Name': 'Harborview Park', 'Weekday Visitors': 100, 'Average Visit Duration (minutes)': 60, 'Weekend Visitors': 300, 'Satisfaction Rating (1-5 scale)': 4.5, 'Green Space (acres)': 8},
    {'Park Name': 'Sunnydale Park', 'Weekday Visitors': 75, 'Average Visit Duration (minutes)': 20, 'Weekend Visitors': 250, 'Satisfaction Rating (1-5 scale)': 4.1, 'Green Space (acres)': 10},
    {'Park Name': 'Liberty Park', 'Weekday Visitors': 300, 'Average Visit Duration (minutes)': 40, 'Weekend Visitors': 950, 'Satisfaction Rating (1-5 scale)': 4.8, 'Green Space (acres)': 30},
    {'Park Name': 'West End Park', 'Weekday Visitors': 50, 'Average Visit Duration (minutes)': 15, 'Weekend Visitors': 200, 'Satisfaction Rating (1-5 scale)': 3.9, 'Green Space (acres)': 5},
    {'Park Name': 'Pine Hill Park', 'Weekday Visitors': 80, 'Average Visit Duration (minutes)': 35, 'Weekend Visitors': 400, 'Satisfaction Rating (1-5 scale)': 4.2, 'Green Space (acres)': 18},
    {'Park Name': 'Oakwood Park', 'Weekday Visitors': 200, 'Average Visit Duration (minutes)': 50, 'Weekend Visitors': 700, 'Satisfaction Rating (1-5 scale)': 4.6, 'Green Space (acres)': 25},
    {'Park Name': 'Meadowland Park', 'Weekday Visitors': 120, 'Average Visit Duration (minutes)': 40, 'Weekend Visitors': 450, 'Satisfaction Rating (1-5 scale)': 4.4, 'Green Space (acres)': 12},
    {'Park Name': 'Lakefront Park', 'Weekday Visitors': 350, 'Average Visit Duration (minutes)': 55, 'Weekend Visitors': 1100, 'Satisfaction Rating (1-5 scale)': 4.8, 'Green Space (acres)': 34}
]

# Extract data for plotting
park_names = [park['Park Name'] for park in parks_data]
visit_durations = [park['Average Visit Duration (minutes)'] for park in parks_data]
weekend_visitors = [park['Weekend Visitors'] for park in parks_data]
satisfaction_ratings = [park['Satisfaction Rating (1-5 scale)'] for park in parks_data]
green_space = [park['Green Space (acres)'] for park in parks_data]

# Map satisfaction ratings to colors
satisfaction_colors = plt.cm.viridis((np.array(satisfaction_ratings) - min(satisfaction_ratings)) / (max(satisfaction_ratings) - min(satisfaction_ratings)))

# Plot bubble chart
plt.figure(figsize=(14, 8))
bubble = plt.scatter(visit_durations, park_names, s=np.sqrt(weekend_visitors)*10, c=satisfaction_colors, alpha=0.6, edgecolors='w', linewidth=1)

# Add labels for each bubble
for i, park_name in enumerate(park_names):
    plt.text(visit_durations[i], park_names[i], park_name, ha='center', va='center', size=8)

# Add color bar
cbar = plt.colorbar(bubble)
cbar.set_label('Satisfaction Rating (1-5 scale)')

# Set the title of the chart
plt.title('Park Bubble Chart')

# Set x and y axes labels
plt.xlabel('Average Visit Duration (minutes)')
plt.ylabel('Park Name')

# Improve layout
plt.tight_layout()

# Show the plot
plt.show()