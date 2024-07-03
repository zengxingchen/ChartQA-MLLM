
import matplotlib.pyplot as plt
import numpy as np

# Data
subjects = ['Math', 'Science', 'English', 'History', 'Geography']
data = [
    [20, 25, 15, 25, 15],  # Class 1
    [22, 23, 18, 20, 17],  # Class 2
    [18, 30, 20, 20, 12],  # Class 3
    [25, 20, 15, 25, 15],  # Class 4
    [15, 20, 30, 20, 15],  # Class 5
    [20, 25, 20, 20, 15],  # Class 6
    [18, 20, 25, 22, 15],  # Class 7
    [20, 30, 20, 15, 15],  # Class 8
    [22, 22, 20, 18, 18],  # Class 9
    [20, 25, 25, 20, 10]   # Class 10
]

data = np.array(data)
data_cum = data.cumsum(axis=1)
class_labels = ['Class 1', 'Class 2', 'Class 3', 'Class 4', 'Class 5', 'Class 6', 'Class 7', 'Class 8', 'Class 9', 'Class 10']
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FFD700']
fig, ax = plt.subplots(figsize=(10, 7))

# Plot
for i, (colname, color) in enumerate(zip(subjects, colors)):
    widths = data[:, i]
    starts = data_cum[:, i] - widths
    ax.barh(class_labels, widths, left=starts, height=0.8, label=colname, color=color)

# Formatting
ax.set_xlabel('Percentage')
ax.set_ylabel('Classes')
ax.set_title('Class Performance in Different Subjects')
ax.legend(loc='lower right', bbox_to_anchor=(1.1, 0))

plt.tight_layout()
plt.show()