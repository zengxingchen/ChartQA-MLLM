
import matplotlib.pyplot as plt
import numpy as np

# Data
activities = ['Reading', 'Writing', 'Listening', 'Speaking', 'Grammar', 'Vocabulary']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
data = np.array([
    [1.5, 2, 1.8, 2.1, 1.7, 1.9, 2.2],  # Reading
    [2, 2.5, 2.2, 2.8, 2.3, 2.6, 2.9],  # Writing
    [3, 3.5, 3.2, 3.7, 3.3, 3.4, 3.8],  # Listening
    [1, 1.5, 1.3, 1.7, 1.4, 1.6, 1.8],  # Speaking
    [2, 2.5, 2.2, 2.7, 2.3, 2.6, 2.9],  # Grammar
    [2.5, 3, 2.8, 3.5, 2.9, 3.2, 3.7]   # Vocabulary
])

# Colors
colors = ['#3498DB', '#E74C3C', '#2ECC71', '#F39C12', '#9B59B6', '#34495E']

# Stacked bar chart
fig, ax = plt.subplots(figsize=(8, 10))
width = 0.8  # Width of the bars

# Plotting each row of the data
cumulative_data = np.zeros(len(days))
for i, row in enumerate(data):
    ax.bar(days, row, bottom=cumulative_data, color=colors[i], width=width)
    cumulative_data += row

# Customizing the plot
ax.set_ylabel('Hours')
ax.set_xlabel('Days of the Week')
ax.set_title('Weekly Language Learning Activity Distribution', pad=20)
ax.legend(activities, loc='upper right', bbox_to_anchor=(1.2, 1))

# Display the plot
plt.tight_layout()
plt.show()