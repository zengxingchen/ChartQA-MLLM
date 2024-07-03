
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Car', 'Bus', 'Bicycle', 'Walking', 'Train']
times = ['Morning', 'Afternoon', 'Evening', 'Night']
data = np.array([
    [20, 30, 15, 25, 10],  # Morning
    [25, 20, 20, 25, 10],  # Afternoon
    [30, 15, 20, 25, 10],  # Evening
    [35, 20, 15, 20, 10]   # Night
])

# Calculate the cumulative sum for each bar
cumulative_data = np.cumsum(data, axis=1)

# Colors for each category
colors = ['#FFA07A', '#20B2AA', '#778899', '#FF6347', '#4682B4']

# Plotting
fig, ax = plt.subplots(figsize=(10, 8))

for i in range(len(categories)):
    if i == 0:
        ax.bar(times, data[:, i], color=colors[i], edgecolor='white', width=0.6)
    else:
        ax.bar(times, data[:, i], bottom=cumulative_data[:, i-1], color=colors[i], edgecolor='white', width=0.6)

# Title and labels
ax.set_title('Percentage of Different Transportation Methods Used During the Day', fontsize=14, pad=20)
ax.set_ylabel('Percentage', fontsize=12)
ax.set_xlabel('Time of Day', fontsize=12)

# Legend
ax.legend(categories, loc='upper right', bbox_to_anchor=(1.2, 1))

# Display the chart
plt.tight_layout()
plt.show()