
import matplotlib.pyplot as plt
import numpy as np

# Data
activities = ['Sleeping', 'Working', 'Exercise', 'Leisure', 'Eating', 'Others']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
data = np.array([
    [8, 7.5, 8, 8, 7.5, 9, 9],         # Sleeping
    [8, 8.5, 8, 8, 8.5, 4, 0],         # Working
    [1, 1, 1.5, 1, 1, 1.5, 2],         # Exercise
    [4, 4, 3.5, 4, 4, 5, 6],           # Leisure
    [2, 2, 2, 2, 2, 2, 2],             # Eating
    [1, 1, 1, 1, 1, 2.5, 5]            # Others
])

# Colors
colors = ['#FF6347', '#FFD700', '#ADFF2F', '#87CEEB', '#EE82EE', '#FFA500']

# Stacked bar chart
fig, ax = plt.subplots(figsize=(10, 6))
width = 0.5  # Width of the bars

# Plotting each row of the data
cumulative_data = np.zeros(len(days))
for i, row in enumerate(data):
    ax.barh(days, row, left=cumulative_data, color=colors[i], height=width)
    cumulative_data += row

# Customizing the plot
ax.set_xlabel('Hours')
ax.set_ylabel('Days of the Week')
ax.set_title('Daily Activity Distribution')
ax.legend(activities, loc='upper left', bbox_to_anchor=(1, 1))

# Display the plot
plt.tight_layout()
plt.show()