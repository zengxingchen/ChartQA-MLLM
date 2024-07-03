
import matplotlib.pyplot as plt

# Data
categories = ['Weekday', 'Saturday', 'Sunday']
work_hours = [8.5, 2.5, 3.0]
leisure_hours = [4.0, 8.0, 9.0]
sleep_hours = [7.5, 8.0, 8.5]

# Offsets for stacked bars
left_offset_work = [0, 0, 0]
left_offset_leisure = [a+b for a, b in zip(left_offset_work, work_hours)]
left_offset_sleep = [a+b for a, b in zip(left_offset_leisure, leisure_hours)]

# Create horizontal bar chart
fig, ax = plt.subplots(figsize=(8, 4))  # Changed chart size

# Stacked bars
ax.barh(categories, work_hours, height=0.6, left=left_offset_work, color='#FFD700')  # Gold
ax.barh(categories, leisure_hours, height=0.6, left=left_offset_leisure, color='#7EC850')  # Green
ax.barh(categories, sleep_hours, height=0.6, left=left_offset_sleep, color='#6495ED')  # Cornflower Blue

# Add some text for labels, title, and custom x-axis tick labels, etc.
ax.set_xlabel('Hours')
ax.set_title('Average Daily Time Spent on Activities')
ax.set_yticks(range(len(categories)))
ax.set_yticklabels(categories)
ax.invert_yaxis()  # Labels read top-to-bottom

# Display the legend
ax.legend(['Work', 'Leisure', 'Sleep'], loc='upper right')

# Display the plot
plt.tight_layout()

plt.show()