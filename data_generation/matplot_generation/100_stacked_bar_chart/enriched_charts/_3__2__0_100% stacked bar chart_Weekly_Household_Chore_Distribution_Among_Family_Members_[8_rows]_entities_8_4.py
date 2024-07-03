
import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
cardio = [40, 35, 30, 25, 20, 15]
strength = [35, 30, 30, 30, 25, 20]
flexibility = [15, 20, 25, 30, 35, 40]
balance = [10, 15, 15, 15, 20, 25]

# Bar widths and indices
width = 0.6
ind = np.arange(len(labels))

# Plot
fig, ax = plt.subplots(figsize=(10, 7))

# Stacked bar chart
p1 = ax.barh(ind, cardio, width, color='#1f77b4')
p2 = ax.barh(ind, strength, width, left=cardio, color='#ff7f0e')
p3 = ax.barh(ind, flexibility, width, left=np.array(cardio) + np.array(strength), color='#2ca02c')
p4 = ax.barh(ind, balance, width, left=np.array(cardio) + np.array(strength) + np.array(flexibility), color='#d62728')

# Labels and title
ax.set_xlabel('Percentage')
ax.set_title('Exercise Habits by Age Group')
ax.set_yticks(ind)
ax.set_yticklabels(labels)
ax.legend((p1[0], p2[0], p3[0], p4[0]), ('Cardio', 'Strength', 'Flexibility', 'Balance'), loc='lower right')

# Adjust layout
plt.tight_layout()
plt.show()