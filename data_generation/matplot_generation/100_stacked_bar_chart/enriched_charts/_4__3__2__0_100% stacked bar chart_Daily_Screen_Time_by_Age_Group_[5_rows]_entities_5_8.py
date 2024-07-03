
import matplotlib.pyplot as plt
import numpy as np

# Data
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
math = [8, 7, 6, 7, 6, 5, 4]
science = [6, 6, 5, 5, 6, 4, 4]
english = [5, 6, 7, 6, 5, 4, 3]
history = [4, 4, 4, 5, 5, 3, 2]
arts = [3, 3, 2, 2, 3, 4, 5]
physical_education = [2, 2, 2, 2, 2, 4, 5]
other = [1, 2, 2, 3, 3, 3, 4]

# Normalize data to sum to 100%
data = np.array([math, science, english, history, arts, physical_education, other])
data_percentage = data / data.sum(axis=0) * 100

# Colors
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#FFC300', '#DAF7A6', '#581845']

# Plot
fig, ax = plt.subplots(figsize=(10, 8))
bar_width = 0.5
indices = np.arange(len(days))

bottoms = np.zeros(len(days))
for i in range(len(data)):
    ax.bar(indices, data_percentage[i], bottom=bottoms, width=bar_width, color=colors[i])
    bottoms += data_percentage[i]

# Labels and title
ax.set_ylabel('Percentage')
ax.set_title('Weekly Study Time Distribution', pad=20)
ax.set_xticks(indices)
ax.set_xticklabels(days)
ax.legend(['Math', 'Science', 'English', 'History', 'Arts', 'Physical Education', 'Other'], bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()