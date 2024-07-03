
import matplotlib.pyplot as plt
import numpy as np

# Data in the order of the CSV table provided above
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
sleeping = [8, 7, 8, 7, 6, 9, 9]
eating = [2, 3, 2, 2, 3, 3, 3]
work = [8, 7, 7, 8, 8, 4, 3]
leisure = [4, 5, 4, 5, 4, 6, 6]
exercise = [2, 2, 3, 2, 3, 2, 3]

# Calculate the bottom positions for each stack segment
sleeping_bottom = np.zeros(len(days))
eating_bottom = np.array(sleeping)
work_bottom = eating_bottom + np.array(eating)
leisure_bottom = work_bottom + np.array(work)

# Normalize data to sum up to 100%
total = [sleep + eat + wrk + lei + ex for sleep, eat, wrk, lei, ex in zip(sleeping, eating, work, leisure, exercise)]
sleeping = np.array(sleeping) / total * 100
eating = np.array(eating) / total * 100
work = np.array(work) / total * 100
leisure = np.array(leisure) / total * 100
exercise = np.array(exercise) / total * 100

fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.6

# Plotting
bars1 = ax.barh(days, sleeping, height=bar_width, color='#FFD700', edgecolor='white', label='Sleeping')
bars2 = ax.barh(days, eating, height=bar_width, left=sleeping_bottom, color='#228B22', edgecolor='white', label='Eating')
bars3 = ax.barh(days, work, height=bar_width, left=work_bottom, color='#6495ED', edgecolor='white', label='Work')
bars4 = ax.barh(days, leisure, height=bar_width, left=leisure_bottom, color='#FF4500', edgecolor='white', label='Leisure')
bars5 = ax.barh(days, exercise, height=bar_width, left=leisure_bottom + leisure, color='#6A5ACD', edgecolor='white', label='Exercise')

# Customizing the plot
ax.set_xlabel('Percentage of Day Spent on Activity')
ax.set_title('Weekly Activity Distribution')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=5)

# Display the chart
plt.tight_layout()
plt.show()