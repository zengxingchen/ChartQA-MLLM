
import matplotlib.pyplot as plt

# Data for the stacked area chart
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
exercise = [30, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
work = [50, 60, 65, 70, 80, 90, 95, 100, 105, 110, 115, 120]
leisure = [40, 30, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(12, 7)) # Modify figure size
ax.stackplot(months, exercise, work, leisure, colors=['#1f77b4', '#ff7f0e', '#2ca02c'])

# Customize the chart with a title and labels
ax.set_title('Monthly Time Allocation (in Hours)', fontsize=16, fontweight='bold', loc='left')
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Hours', fontsize=14)

# Assign annotation/text label on the chart.
for i in range(len(months)):
    ax.text(i, exercise[i] + work[i] + leisure[i], f"{exercise[i] + work[i] + leisure[i]}", ha='center', va='bottom', fontsize=10)

# Add a legend
ax.legend(['Exercise', 'Work', 'Leisure'], loc='upper left', fontsize=12)

# Show the figure
plt.tight_layout()
plt.show()