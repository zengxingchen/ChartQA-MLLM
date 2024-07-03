
import matplotlib.pyplot as plt

# Data for plotting
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
calories_burned = [400, 450, 500, 350, 600, 700, 650]

fig, ax = plt.subplots(figsize=(10, 6))

# Create a vertical bar chart with custom colors and bar widths
bars = ax.bar(days, calories_burned, width=0.5, color=['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0'])

# Set the chart title and labels
ax.set_title('Daily Calories Burned', fontsize=18)
ax.set_xlabel('Day of the Week', fontsize=14)
ax.set_ylabel('Calories Burned', fontsize=14)

# Customize the ticks on both axes
ax.xaxis.set_tick_params(labelsize=12)
ax.yaxis.set_tick_params(labelsize=12)

# Set y-axis limits to truncate the chart, starting at 300
ax.set_ylim(300, 750)

# Add value labels to each bar
for bar in bars:
    height = bar.get_height()
    label_y_pos = height + 10  # Some padding to the top
    ax.text(bar.get_x() + bar.get_width()/2, label_y_pos, f'{height} Cal',
            va='bottom', ha='center', fontsize=12)

plt.tight_layout()
plt.show()