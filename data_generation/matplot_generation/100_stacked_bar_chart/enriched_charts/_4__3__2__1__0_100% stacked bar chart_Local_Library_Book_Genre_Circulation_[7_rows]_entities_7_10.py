
import matplotlib.pyplot as plt
import numpy as np

# Data
age_groups = ["10-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80+"]
reading = [20, 25, 30, 35, 40, 45, 50, 55]
writing = [25, 30, 25, 20, 15, 10, 5, 0]
analyzing = [30, 20, 25, 30, 35, 40, 45, 40]
creativity = [25, 25, 20, 15, 10, 5, 0, 5]

# Plot
fig, ax = plt.subplots(figsize=(10, 14))

width = 0.8  # width of bars
age_index = np.arange(len(age_groups))

# Stacked bar chart
p1 = ax.bar(age_index, reading, width, color='#FF6347', label='Reading')
p2 = ax.bar(age_index, writing, width, bottom=reading, color='#4682B4', label='Writing')
p3 = ax.bar(age_index, analyzing, width, bottom=np.array(reading) + np.array(writing), color='#32CD32', label='Analyzing')
p4 = ax.bar(age_index, creativity, width, bottom=np.array(reading) + np.array(writing) + np.array(analyzing), color='#FFD700', label='Creativity')

# Labels and title
ax.set_ylabel('Percentage')
ax.set_title('Skills Utilized by Age Group in Literature & Writing')
ax.set_xticks(age_index)
ax.set_xticklabels(age_groups)
ax.legend(loc='upper left')

# Display
plt.show()