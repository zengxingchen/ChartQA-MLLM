
import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['Student1', 'Student2', 'Student3', 'Student4', 'Student5', 'Student6', 'Student7', 'Student8', 
          'Student9', 'Student10', 'Student11', 'Student12', 'Student13', 'Student14', 'Student15', 
          'Student16', 'Student17', 'Student18', 'Student19', 'Student20']
online_learning = [30, 25, 20, 35, 25, 20, 30, 25, 20, 35, 25, 20, 30, 25, 20, 35, 25, 20, 30, 25]
classroom_learning = [20, 25, 30, 20, 20, 25, 20, 30, 25, 20, 20, 25, 20, 30, 25, 20, 20, 25, 20, 30]
self_study = [25, 20, 25, 15, 30, 30, 20, 20, 30, 20, 30, 25, 20, 25, 30, 20, 30, 25, 20, 25]
group_study = [15, 20, 15, 20, 15, 15, 20, 15, 15, 15, 15, 20, 20, 10, 15, 15, 15, 20, 20, 10]
workshops = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

data = np.array([online_learning, classroom_learning, self_study, group_study, workshops])
data_cum = data.cumsum(axis=0)

# Colors
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2']

fig, ax = plt.subplots(figsize=(12, 8))

# Plot
for i, (colname, color) in enumerate(zip(['Online Learning', 'Classroom Learning', 'Self-study', 'Group Study', 'Workshops'], colors)):
    heights = data[i]
    starts = data_cum[i] - heights
    ax.bar(labels, heights, bottom=starts, width=0.8, label=colname, color=color)

# Decoration
ax.set_title('Preferred Learning Methods Among Students', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1))
plt.ylabel('Percentage')
plt.xlabel('Students')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()