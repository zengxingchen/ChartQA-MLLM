
import matplotlib.pyplot as plt

# Data for the stacked area chart
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
cardio = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]
strength = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
flexibility = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(14, 9))  # Modify figure size
ax.stackplot(months, cardio, strength, flexibility, colors=['#4b8bbe', '#d16a16', '#6a9d2a'])

# Customize the chart with a title and labels
ax.set_title('Monthly Workout Duration (in hours)', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Duration (hours)', fontsize=14)

# Assign annotation/text label on the chart.
for i in range(len(months)):
    total = cardio[i] + strength[i] + flexibility[i]
    ax.text(i, total + 5, f"{total}", ha='center', va='bottom')

# Show the figure
plt.tight_layout()
plt.show()