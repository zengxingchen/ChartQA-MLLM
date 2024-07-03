
import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['USA', 'Canada', 'UK', 'Australia', 'Germany', 'Brazil', 'Japan']
football = [35, 20, 40, 30, 25, 45, 25]
basketball = [30, 35, 20, 25, 30, 20, 25]
baseball = [25, 30, 25, 20, 30, 20, 30]
swimming = [10, 15, 15, 25, 15, 15, 20]

# Plotting
width = 0.5  # width of the bars
ind = np.arange(len(labels))  # the x locations for the groups

fig, ax = plt.subplots(figsize=(10, 6))

p1 = ax.barh(ind, football, width, color='#FF5733', label='Football')
p2 = ax.barh(ind, basketball, width, left=np.array(football), color='#33FF57', label='Basketball')
p3 = ax.barh(ind, baseball, width, left=np.array(football) + np.array(basketball), color='#3357FF', label='Baseball')
p4 = ax.barh(ind, swimming, width, left=np.array(football) + np.array(basketball) + np.array(baseball), color='#FF33A1', label='Swimming')

# Add labels
ax.set_xlabel('Percentage')
ax.set_title('Participation in Different Sports by Country')
ax.set_yticks(ind)
ax.set_yticklabels(labels)
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1))

# Display the plot
plt.tight_layout()
plt.show()