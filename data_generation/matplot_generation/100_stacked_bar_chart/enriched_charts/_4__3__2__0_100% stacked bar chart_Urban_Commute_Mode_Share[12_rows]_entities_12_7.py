
import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60+']
football = [10, 20, 30, 25, 15, 10, 5]
basketball = [5, 10, 20, 30, 25, 5, 5]
baseball = [2, 8, 15, 20, 25, 10, 5]
swimming = [3, 12, 10, 15, 20, 10, 5]

# Plotting
width = 0.4  # width of the bars
ind = np.arange(len(labels))  # the x locations for the groups

fig, ax = plt.subplots(figsize=(12, 8))

p1 = ax.bar(ind, football, width, color='#1f77b4', label='Football')
p2 = ax.bar(ind, basketball, width, bottom=np.array(football), color='#ff7f0e', label='Basketball')
p3 = ax.bar(ind, baseball, width, bottom=np.array(football) + np.array(basketball), color='#2ca02c', label='Baseball')
p4 = ax.bar(ind, swimming, width, bottom=np.array(football) + np.array(basketball) + np.array(baseball), color='#d62728', label='Swimming')

# Add labels
ax.set_ylabel('Participation Percentage')
ax.set_title('Participation in Different Sports by Age Group', pad=20)
ax.set_xticks(ind)
ax.set_xticklabels(labels)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Display the plot
plt.tight_layout()
plt.show()