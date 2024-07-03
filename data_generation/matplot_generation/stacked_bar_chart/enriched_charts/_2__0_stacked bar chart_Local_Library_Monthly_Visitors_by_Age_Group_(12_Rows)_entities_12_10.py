
import matplotlib.pyplot as plt

# Data
categories = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
work_hours = [7.0, 8.0, 6.5, 7.5, 6.0, 2.0, 3.0]
leisure_hours = [4.0, 3.5, 5.0, 4.0, 5.5, 9.0, 8.5]
sleep_hours = [8.0, 7.5, 8.0, 7.5, 8.5, 9.0, 9.0]

# Offsets for stacked bars
left_offset_work = [0] * len(work_hours)
left_offset_leisure = [a + b for a, b in zip(left_offset_work, work_hours)]
left_offset_sleep = [a + b for a, b in zip(left_offset_leisure, leisure_hours)]

# Create vertical bar chart
fig, ax = plt.subplots(figsize=(10, 6))

# Stacked bars
ax.bar(categories, work_hours, width=0.5, bottom=left_offset_work, color='#FF5733')  # Red
ax.bar(categories, leisure_hours, width=0.5, bottom=left_offset_leisure, color='#33FF57')  # Green
ax.bar(categories, sleep_hours, width=0.5, bottom=left_offset_sleep, color='#3357FF')  # Blue

# Add some text for labels, title, and custom y-axis tick labels, etc.
ax.set_ylabel('Hours')
ax.set_title('Weekly Time Distribution for Activities')
ax.legend(['Work', 'Leisure', 'Sleep'], loc='upper left')

# Numerical labels for each bar segment
for i in range(len(categories)):
    ax.text(i, work_hours[i] / 2, str(work_hours[i]), ha='center', va='center', color='black')
    ax.text(i, left_offset_leisure[i] + leisure_hours[i] / 2, str(leisure_hours[i]), ha='center', va='center', color='black')
    ax.text(i, left_offset_sleep[i] + sleep_hours[i] / 2, str(sleep_hours[i]), ha='center', va='center', color='black')

plt.tight_layout()
plt.show()