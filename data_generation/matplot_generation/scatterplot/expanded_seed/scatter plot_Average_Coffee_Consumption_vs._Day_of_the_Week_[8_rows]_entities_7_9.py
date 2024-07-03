
import matplotlib.pyplot as plt

# Given table data
data = [
    {'Day': 'Monday', 'Average Cups of Coffee Consumed': 3.8},
    {'Day': 'Tuesday', 'Average Cups of Coffee Consumed': 3.5},
    {'Day': 'Wednesday', 'Average Cups of Coffee Consumed': 3.6},
    {'Day': 'Thursday', 'Average Cups of Coffee Consumed': 3.7},
    {'Day': 'Friday', 'Average Cups of Coffee Consumed': 4.2},
    {'Day': 'Saturday', 'Average Cups of Coffee Consumed': 2.8},
    {'Day': 'Sunday', 'Average Cups of Coffee Consumed': 2.4}
]

# Extracting days and average cups of coffee consumed
days = [entry['Day'] for entry in data]
avg_cups = [entry['Average Cups of Coffee Consumed'] for entry in data]

# Mapping days of the week to numerical values for the x-axis
day_to_num = {day: idx for idx, day in enumerate(days)}

# Plotting the scatter plot
plt.figure(figsize=(10, 6))
for day, cups in zip(days, avg_cups):
    plt.scatter(
        day_to_num[day], cups,  # X and Y coordinates
        s=cups * 50,  # Marker size based on coffee consumption
        alpha=0.5,  # Transparency
        cmap='viridis',  # Color map for diversity
        label=f'{day}: {cups} cups'  # Label for the legend
    )

# Customizing the x-axis to show the days of the week
plt.xticks(range(len(days)), days)

# Adding labels and title
plt.xlabel('Day of the Week')
plt.ylabel('Average Cups of Coffee Consumed')
plt.title('Average Cups Of Coffee Consumed Per Day')

# Enabling the legend
plt.legend()

# Displaying the plot
plt.grid(True)
plt.show()