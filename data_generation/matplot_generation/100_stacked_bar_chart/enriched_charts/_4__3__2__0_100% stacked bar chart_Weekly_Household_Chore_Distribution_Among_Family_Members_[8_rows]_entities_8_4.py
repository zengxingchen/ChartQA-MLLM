
import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
vegetables = [25, 20, 15, 20, 25, 30]
fruits = [20, 25, 20, 25, 25, 25]
grains = [30, 30, 40, 30, 25, 20]
protein = [25, 25, 25, 25, 25, 25]

# Bar widths and indices
width = 0.6
ind = np.arange(len(labels))

# Plot
fig, ax = plt.subplots(figsize=(12, 8))

# Stacked bar chart
p1 = ax.bar(ind, vegetables, width, color='#1f77b4')
p2 = ax.bar(ind, fruits, width, bottom=vegetables, color='#ff7f0e')
p3 = ax.bar(ind, grains, width, bottom=np.array(vegetables) + np.array(fruits), color='#2ca02c')
p4 = ax.bar(ind, protein, width, bottom=np.array(vegetables) + np.array(fruits) + np.array(grains), color='#d62728')

# Labels and title
ax.set_ylabel('Percentage')
ax.set_title('Food Consumption by Age Group')
ax.set_xticks(ind)
ax.set_xticklabels(labels)
ax.legend((p1[0], p2[0], p3[0], p4[0]), ('Vegetables', 'Fruits', 'Grains', 'Protein'), loc='upper left')

# Adjust layout
plt.tight_layout()
plt.show()