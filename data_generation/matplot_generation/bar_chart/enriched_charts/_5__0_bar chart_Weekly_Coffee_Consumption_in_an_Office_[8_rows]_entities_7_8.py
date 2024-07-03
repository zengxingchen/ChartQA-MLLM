
import matplotlib.pyplot as plt

# Data for plotting
activities = ["Running", "Swimming", "Cycling", "Yoga", "Hiking", "Dancing", 
              "Gym Workout", "Basketball", "Tennis", "Boxing", "Soccer", "Golf"]
calories_burned = [25, 40, 35, 30, 45, 38, 50, 42, 37, 33, 44, 31]

fig, ax = plt.subplots(figsize=(10, 12))

# Create a vertical bar chart with custom colors and bar widths
bars = ax.bar(activities, calories_burned, width=0.5,
              color=['#ff5733', '#33ff57', '#3357ff', '#ff33a1', '#33ffd7', '#d733ff',
                     '#ff8833', '#33ff88', '#8833ff', '#ff3333', '#33ffff', '#ff8c33'])

# Set the chart title and labels
ax.set_title('Calories Burned in Different Activities (kcal)', fontsize=18)
ax.set_ylabel('Calories Burned (kcal)', fontsize=14)
ax.set_xlabel('Activity', fontsize=14)

# Customize the ticks on both axes
ax.yaxis.set_tick_params(labelsize=12)
ax.xaxis.set_tick_params(labelsize=12, rotation=45)

# Set y-axis limits to truncate the chart
ax.set_ylim(20, 55)

# Add value labels to each bar
for bar in bars:
    height = bar.get_height()
    label_y_pos = height + 0.5  # Some padding above the bar
    ax.text(bar.get_x() + bar.get_width()/2, label_y_pos, f'{height} kcal',
            va='bottom', ha='center', fontsize=12)

plt.tight_layout()
plt.show()