
import matplotlib.pyplot as plt

# Data provided
data = [
    {'Week': '2023-02-01 to 2023-02-07', 'Refrigerator': 75, 'Heating/Cooling': 150, 'Washer/Dryer': 30, 'Lights': 45, 'Electronics': 50},
    {'Week': '2023-02-08 to 2023-02-14', 'Refrigerator': 80, 'Heating/Cooling': 165, 'Washer/Dryer': 25, 'Lights': 40, 'Electronics': 60},
    {'Week': '2023-02-15 to 2023-02-21', 'Refrigerator': 70, 'Heating/Cooling': 140, 'Washer/Dryer': 35, 'Lights': 50, 'Electronics': 55},
    {'Week': '2023-02-22 to 2023-02-28', 'Refrigerator': 85, 'Heating/Cooling': 130, 'Washer/Dryer': 40, 'Lights': 60, 'Electronics': 65},
    {'Week': '2023-03-01 to 2023-03-07', 'Refrigerator': 90, 'Heating/Cooling': 180, 'Washer/Dryer': 32, 'Lights': 42, 'Electronics': 70},
    {'Week': '2023-03-08 to 2023-03-14', 'Refrigerator': 88, 'Heating/Cooling': 175, 'Washer/Dryer': 29, 'Lights': 47, 'Electronics': 66},
    {'Week': '2023-03-15 to 2023-03-21', 'Refrigerator': 74, 'Heating/Cooling': 160, 'Washer/Dryer': 34, 'Lights': 55, 'Electronics': 54},
    {'Week': '2023-03-22 to 2023-03-28', 'Refrigerator': 78, 'Heating/Cooling': 155, 'Washer/Dryer': 31, 'Lights': 51, 'Electronics': 63}
]

# Extracting weeks for x-axis labels
weeks = [entry['Week'] for entry in data]

# Extracting data for each category
refrigerator = [entry['Refrigerator'] for entry in data]
heating_cooling = [entry['Heating/Cooling'] for entry in data]
washer_dryer = [entry['Washer/Dryer'] for entry in data]
lights = [entry['Lights'] for entry in data]
electronics = [entry['Electronics'] for entry in data]

# Number of weeks
num_weeks = len(weeks)

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(10, 8))

# Colors and hatch patterns for each category
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
hatch_patterns = ['/', '\\', '|', '-', '+']

# Plotting stacks
ax.bar(weeks, refrigerator, color=colors[0], edgecolor='white', hatch=hatch_patterns[0], label='Refrigerator')
ax.bar(weeks, heating_cooling, bottom=refrigerator, color=colors[1], edgecolor='white', hatch=hatch_patterns[1], label='Heating/Cooling')
ax.bar(weeks, washer_dryer, bottom=[i+j for i,j in zip(refrigerator, heating_cooling)], color=colors[2], edgecolor='white', hatch=hatch_patterns[2], label='Washer/Dryer')
ax.bar(weeks, lights, bottom=[i+j+k for i,j,k in zip(refrigerator, heating_cooling, washer_dryer)], color=colors[3], edgecolor='white', hatch=hatch_patterns[3], label='Lights')
ax.bar(weeks, electronics, bottom=[i+j+k+l for i,j,k,l in zip(refrigerator, heating_cooling, washer_dryer, lights)], color=colors[4], edgecolor='white', hatch=hatch_patterns[4], label='Electronics')

# Adding labels and title
ax.set_xlabel('Weeks', fontsize=14)
ax.set_ylabel('Usage (units)', fontsize=14)
ax.set_title('Weekly Household Energy Usage by Category', fontsize=16)

# Adding legend
ax.legend(title='Categories', bbox_to_anchor=(1.05, 1), loc='upper left')

# Improve layout
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()                    # Adjust layout to fit everything without overlapping

# Display the plot
plt.show()