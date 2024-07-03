
import matplotlib.pyplot as plt
import pandas as pd

# Given data
data = [
    {'Day': 'Monday', 'Visitor Count': 50, 'Hour': 10},
    {'Day': 'Monday', 'Visitor Count': 75, 'Hour': 12},
    {'Day': 'Monday', 'Visitor Count': 60, 'Hour': 14},
    {'Day': 'Monday', 'Visitor Count': 30, 'Hour': 16},
    {'Day': 'Tuesday', 'Visitor Count': 40, 'Hour': 10},
    {'Day': 'Tuesday', 'Visitor Count': 70, 'Hour': 12},
    {'Day': 'Tuesday', 'Visitor Count': 55, 'Hour': 14},
    {'Day': 'Tuesday', 'Visitor Count': 25, 'Hour': 16},
    {'Day': 'Wednesday', 'Visitor Count': 60, 'Hour': 10},
    {'Day': 'Wednesday', 'Visitor Count': 90, 'Hour': 12},
    {'Day': 'Wednesday', 'Visitor Count': 80, 'Hour': 14},
    {'Day': 'Wednesday', 'Visitor Count': 45, 'Hour': 16},
    {'Day': 'Thursday', 'Visitor Count': 35, 'Hour': 10},
    {'Day': 'Thursday', 'Visitor Count': 80, 'Hour': 12},
    {'Day': 'Thursday', 'Visitor Count': 65, 'Hour': 14}
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Unique days, for coloring in the scatter plot
days = df['Day'].unique()
colors = {'Monday': 'red', 'Tuesday': 'green', 'Wednesday': 'blue', 'Thursday': 'purple'}

# Create a scatter plot
plt.figure(figsize=(10, 6))
for day in days:
    day_data = df[df['Day'] == day]
    plt.scatter(
        day_data['Hour'], 
        day_data['Visitor Count'],
        s=day_data['Visitor Count'],  # Size based on visitor count
        c=colors[day],               # Color for each day
        label=day,
        alpha=0.6,                   # Translucency of markers
        edgecolors='w'               # Edge color for markers
    )

# Customize the plot
plt.title('Visitor Count by Hour and Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Visitor Count')
plt.xticks(range(10, 17, 2))          # Set x-ticks to match the given hours
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(title='Day of the Week')

# Display the plot
plt.show()