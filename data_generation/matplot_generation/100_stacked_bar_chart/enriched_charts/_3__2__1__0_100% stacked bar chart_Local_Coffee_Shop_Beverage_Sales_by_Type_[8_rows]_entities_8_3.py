
import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
exercise = [20, 15, 30, 25, 10]
diet = [25, 30, 20, 15, 10]
sleep = [30, 25, 20, 15, 10]
mental_health = [15, 20, 15, 30, 20]
social_interaction = [10, 10, 15, 15, 50]

data = np.array([exercise, diet, sleep, mental_health, social_interaction])
data_cum = data.cumsum(axis=0)

# Colors
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

fig, ax = plt.subplots(figsize=(10, 6))

# Plot
for i, (colname, color) in enumerate(zip(['Exercise', 'Diet', 'Sleep', 'Mental Health', 'Social Interaction'], colors)):
    widths = data[i]
    starts = data_cum[i] - widths
    ax.barh(labels, widths, left=starts, height=0.5, label=colname, color=color)

# Decoration
ax.set_title('Contribution to Overall Health by Different Activities', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1))
plt.xlabel('Percentage')
plt.ylabel('Individuals')
plt.show()