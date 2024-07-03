
import matplotlib.pyplot as plt

# Original data
data = [
    {'Month': 'January', 'Swimming': '10%', 'Yoga': '20%', 'Soccer': '15%', 'Basketball': '25%', 'Dance': '10%', 'Gym Workouts': '10%', 'Cycling': '5%', 'Running': '5%'},
    {'Month': 'February', 'Swimming': '8%', 'Yoga': '22%', 'Soccer': '12%', 'Basketball': '26%', 'Dance': '11%', 'Gym Workouts': '11%', 'Cycling': '5%', 'Running': '5%'},
    # ... other monthly data ...
    {'Month': 'August', 'Swimming': '5%', 'Yoga': '10%', 'Soccer': '35%', 'Basketball': '10%', 'Dance': '10%', 'Gym Workouts': '15%', 'Cycling': '10%', 'Running': '5%'}
]

# Extracting activity names
activities = list(data[0].keys())[1:]

# Convert the percentages to float values
for entry in data:
    for activity in activities:
        entry[activity] = float(entry[activity].strip('%')) / 100

# Extract months and initialize lists to store the data for plotting
months = [entry['Month'] for entry in data]
activity_data = {activity: [] for activity in activities}

# Populate the lists with data
for activity in activities:
    for entry in data:
        activity_data[activity].append(entry[activity])

# Create stacked bars
bottoms = [0] * len(data)  # Initialize the bottom positions for the first set of bars
for activity in activities:
    plt.bar(months, activity_data[activity], bottom=bottoms, label=activity)
    # Update the bottoms to be ready for stacking the next set of bars
    bottoms = [sum(x) for x in zip(bottoms, activity_data[activity])]

plt.title('Monthly Activities Participation - 100% Stacked Bar Chart')
plt.xlabel('Month')
plt.ylabel('Percentage')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))  # Place the legend outside the chart
plt.ylim(0, 1)  # Set y-axis to show percentage as fractions

# Prepare x-axis with evenly spaced month names
plt.xticks(range(len(months)), months, rotation=45)

# Show grid lines for better readability
plt.grid(axis='y')

# Show plot
plt.tight_layout()
plt.show()