
import matplotlib.pyplot as plt
import numpy as np

# Data for the chart
labels = ['2000', '2005', '2010', '2015', '2020', '2025', '2030', '2035', '2040', '2045']
reading = np.array([78, 80, 82, 85, 88, 90, 92, 94, 96, 98])
writing = np.array([82, 84, 86, 88, 90, 92, 94, 96, 98, 100])
math = np.array([85, 87, 90, 92, 94, 96, 98, 100, 102, 104])
science = np.array([80, 82, 85, 87, 90, 92, 94, 96, 98, 100])
art = np.array([75, 77, 80, 82, 85, 87, 90, 92, 94, 96])

# Calculating percentage for stacked bar chart
total = reading + writing + math + science + art
reading_perc = reading / total * 100
writing_perc = writing / total * 100
math_perc = math / total * 100
science_perc = science / total * 100
art_perc = art / total * 100

# Plotting the data
fig, ax = plt.subplots(figsize=(10, 14))

bar_width = 0.7

bar1 = ax.bar(labels, reading_perc, color='#FF9999', edgecolor='white', width=bar_width)
bar2 = ax.bar(labels, writing_perc, bottom=reading_perc, color='#66B3FF', edgecolor='white', width=bar_width)
bar3 = ax.bar(labels, math_perc, bottom=reading_perc + writing_perc, color='#99FF99', edgecolor='white', width=bar_width)
bar4 = ax.bar(labels, science_perc, bottom=reading_perc + writing_perc + math_perc, color='#FFCC99', edgecolor='white', width=bar_width)
bar5 = ax.bar(labels, art_perc, bottom=reading_perc + writing_perc + math_perc + science_perc, color='#FFD700', edgecolor='white', width=bar_width)

# Adding labels and title
ax.set_ylabel('Percentage')
ax.set_title('Student Proficiency in Different Subjects (2000-2045)', pad=20)

# Adding legend
ax.legend((bar1, bar2, bar3, bar4, bar5), ('Reading', 'Writing', 'Math', 'Science', 'Art'), loc='upper left')

# Display the plot
plt.tight_layout()
plt.show()