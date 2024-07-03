
import matplotlib.pyplot as plt
import numpy as np

categories = ['Age Group 10-19', 'Age Group 20-29', 'Age Group 30-39', 'Age Group 40-49', 'Age Group 50-59', 'Age Group 60+']
values1 = [15, 20, 30, 25, 10, 20]
values2 = [25, 15, 20, 30, 10, 15]
values3 = [20, 25, 10, 15, 30, 20]
values4 = [10, 30, 15, 20, 25, 30]
values5 = [30, 10, 25, 10, 25, 15]

width = 0.4  # Width of the bars

fig, ax = plt.subplots(figsize=(10, 8))  # Change the width and height of the chart

# Plotting vertical stacked bar chart
ax.bar(categories, values1, color='#1f77b4', edgecolor='grey', width=width)
ax.bar(categories, values2, bottom=np.array(values1), color='#ff7f0e', edgecolor='grey', width=width)
ax.bar(categories, values3, bottom=np.array(values1)+np.array(values2), color='#2ca02c', edgecolor='grey', width=width)
ax.bar(categories, values4, bottom=np.array(values1)+np.array(values2)+np.array(values3), color='#d62728', edgecolor='grey', width=width)
ax.bar(categories, values5, bottom=np.array(values1)+np.array(values2)+np.array(values3)+np.array(values4), color='#9467bd', edgecolor='grey', width=width)

# Adding labels
ax.set_ylabel('Percentage (%)')
ax.set_xlabel('Age Groups')
ax.set_title('Participation in Sports Activities by Age Group')

# Moving legend to a different position
plt.legend(['Running', 'Swimming', 'Cycling', 'Weightlifting', 'Yoga'], loc='upper right', bbox_to_anchor=(1.25, 1))

plt.tight_layout()
plt.show()