
import matplotlib.pyplot as plt
import numpy as np

categories = ['Online Courses', 'Textbooks', 'Extracurricular', 'Tutoring', 'Other']
values1 = [20, 30, 10, 15, 25]
values2 = [30, 20, 20, 10, 20]
values3 = [25, 10, 30, 20, 15]
values4 = [15, 25, 20, 30, 10]
values5 = [10, 15, 20, 25, 30]

width = 0.6  # Width of the bars

fig, ax = plt.subplots(figsize=(12, 7))  # Change the width and height of the chart

# Plotting horizontal stacked bar chart
ax.barh(categories, values1, color='#ff9999', edgecolor='grey', height=width)
ax.barh(categories, values2, left=np.array(values1), color='#66b3ff', edgecolor='grey', height=width)
ax.barh(categories, values3, left=np.array(values1)+np.array(values2), color='#99ff99', edgecolor='grey', height=width)
ax.barh(categories, values4, left=np.array(values1)+np.array(values2)+np.array(values3), color='#ffcc99', edgecolor='grey', height=width)
ax.barh(categories, values5, left=np.array(values1)+np.array(values2)+np.array(values3)+np.array(values4), color='#c2c2f0', edgecolor='grey', height=width)

# Adding labels
ax.set_xlabel('Percentage (%)')
ax.set_ylabel('Education Resources')
ax.set_title('Distribution of Educational Resources')

# Moving legend to a different position
plt.legend(['Online Courses', 'Textbooks', 'Extracurricular', 'Tutoring', 'Other'], loc='upper right', bbox_to_anchor=(1.15, 1))

plt.tight_layout()
plt.show()