
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
average_sleep_hours = [7.5, 7.3, 7.0, 6.8, 7.2, 7.6, 7.8, 7.7, 7.4, 6.9, 6.7, 7.1]

# Create horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 8))  # Change width and height of the chart
bars = ax.barh(months, average_sleep_hours, height=0.5, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#aec7e8', '#ffbb78'])

# Customizing the plot
ax.set_title('Average Monthly Hours of Sleep', fontsize=20)  # Change topic and headline
ax.set_xlabel('Average Sleep Hours', fontsize=14)
ax.set_ylabel('Month', fontsize=14)

# Set y-axis limits to start from 4
ax.set_xlim(4, 8)

# Set bar labels to show the sleep hours values
for bar in bars:
    width = bar.get_width()
    label_x_pos = width if width > 4 else width + 0.1  # Adjust label position based on value
    ax.text(label_x_pos, bar.get_y() + bar.get_height()/2, f'{width} hrs', ha='left', va='center')

# Show the plot
plt.tight_layout()
plt.show()