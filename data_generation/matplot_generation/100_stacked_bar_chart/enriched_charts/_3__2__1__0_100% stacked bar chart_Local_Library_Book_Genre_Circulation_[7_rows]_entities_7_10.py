
import matplotlib.pyplot as plt
import numpy as np

# Data
age_groups = ["10-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80+"]
anxiety = [35, 45, 40, 30, 25, 20, 15, 10]
depression = [25, 30, 35, 40, 35, 30, 25, 20]
ptsd = [20, 15, 15, 20, 25, 30, 35, 40]
other = [20, 10, 10, 10, 15, 20, 25, 30]

# Plot
fig, ax = plt.subplots(figsize=(14, 8))

width = 0.6  # width of bars
age_index = np.arange(len(age_groups))

# Stacked bar chart
p1 = ax.barh(age_index, anxiety, width, color='#FF9999', label='Anxiety')
p2 = ax.barh(age_index, depression, width, left=anxiety, color='#66B3FF', label='Depression')
p3 = ax.barh(age_index, ptsd, width, left=np.array(anxiety)+np.array(depression), color='#99FF99', label='PTSD')
p4 = ax.barh(age_index, other, width, left=np.array(anxiety)+np.array(depression)+np.array(ptsd), color='#FFD700', label='Other')

# Labels and title
ax.set_xlabel('Percentage')
ax.set_title('Mental Health Issues Reported by Age Group')
ax.set_yticks(age_index)
ax.set_yticklabels(age_groups)
ax.legend(loc='upper right')

# Display
plt.show()