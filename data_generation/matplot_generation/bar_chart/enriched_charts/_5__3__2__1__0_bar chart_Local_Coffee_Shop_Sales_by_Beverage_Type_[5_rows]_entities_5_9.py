
import matplotlib.pyplot as plt

# Data
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
soccer = [1.5, 2.0, 2.5, 1.0, 1.5, 3.0, 2.5]
basketball = [2.0, 1.5, 2.0, 1.0, 2.5, 2.5, 1.5]
swimming = [1.0, 1.5, 1.0, 2.0, 1.0, 1.5, 2.0]
cycling = [0.5, 1.0, 1.5, 2.0, 2.0, 2.5, 3.0]

# Create figure and axis objects
fig, ax = plt.subplots(figsize=(14, 10))

# Plotting the bar chart
bar_height = 0.2
ax.barh(days, soccer, color='#1f77b4', height=bar_height, label='Soccer')
ax.barh([d + bar_height for d in range(len(days))], basketball, color='#ff7f0e', height=bar_height, label='Basketball')
ax.barh([d + 2 * bar_height for d in range(len(days))], swimming, color='#2ca02c', height=bar_height, label='Swimming')
ax.barh([d + 3 * bar_height for d in range(len(days))], cycling, color='#d62728', height=bar_height, label='Cycling')

# Customizing the plot (labels, title, etc.)
ax.set_ylabel('Days')
ax.set_xlabel('Hours')
ax.set_title('Weekly Hours Spent on Various Sports Activities', pad=20)
ax.set_xlim([0, 4])
ax.legend(loc='lower right', bbox_to_anchor=(1, 0))

# Adjust layout
plt.tight_layout()
plt.show()