
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Math', 'Science', 'History', 'Art', 'Sports', 'Language', 'Music', 'Computer Science', 'Physics', 'Chemistry']
part_a = np.array([20, 35, 45, 30, 25, 40, 35, 50, 30, 25])
part_b = np.array([25, 40, 30, 35, 45, 25, 30, 25, 45, 35])
part_c = np.array([55, 25, 25, 35, 30, 35, 35, 25, 25, 40])

# Calculate percentages
total = part_a + part_b + part_c
part_a_perc = part_a / total * 100
part_b_perc = part_b / total * 100
part_c_perc = part_c / total * 100

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.7

bars1 = ax.bar(categories, part_a_perc, color='#1f77b4', edgecolor='white', width=bar_width, label='Part A')
bars2 = ax.bar(categories, part_b_perc, bottom=part_a_perc, color='#ff7f0e', edgecolor='white', width=bar_width, label='Part B')
bars3 = ax.bar(categories, part_c_perc, bottom=part_a_perc + part_b_perc, color='#2ca02c', edgecolor='white', width=bar_width, label='Part C')

# Add labels
ax.set_ylabel('Percentage')
ax.set_title('Subject Distribution in Academic Performance')
ax.legend(loc='upper left')

# Show plot
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()