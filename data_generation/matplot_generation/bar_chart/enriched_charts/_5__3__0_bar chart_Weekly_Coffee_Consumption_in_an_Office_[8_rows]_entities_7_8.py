
import matplotlib.pyplot as plt

# Data for plotting
weeks = ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", 
         "Week 7", "Week 8", "Week 9", "Week 10", "Week 11", "Week 12",
         "Week 13", "Week 14", "Week 15", "Week 16", "Week 17", "Week 18",
         "Week 19", "Week 20"]
stress_levels = [45, 55, 48, 50, 60, 52, 58, 53, 57, 50, 59, 54, 56, 57, 51, 61, 55, 58, 53, 59]

fig, ax = plt.subplots(figsize=(14, 8))

# Create a horizontal bar chart with custom colors and bar widths
bars = ax.barh(weeks, stress_levels, height=0.7,
               color=['#003f5c', '#374c80', '#7a5195', '#bc5090', '#ef5675', '#ff764a',
                      '#ffa600', '#003f5c', '#374c80', '#7a5195', '#bc5090', '#ef5675',
                      '#ff764a', '#ffa600', '#003f5c', '#374c80', '#7a5195', '#bc5090',
                      '#ef5675', '#ff764a'])

# Set the chart title and labels
ax.set_title('Weekly Stress Levels of Students', fontsize=20, pad=30)
ax.set_xlabel('Stress Level', fontsize=14)
ax.set_ylabel('Week', fontsize=14)

# Customize the ticks on both axes
ax.xaxis.set_tick_params(labelsize=12)
ax.yaxis.set_tick_params(labelsize=12)

# Set y-axis limits to start from a specific value
ax.set_xlim(40, 65)

# Add value labels to each bar
for bar in bars:
    width = bar.get_width()
    label_x_pos = width + 0.5  # Some padding to the right
    ax.text(label_x_pos, bar.get_y() + bar.get_height()/2, f'{width} points',
            va='center', ha='center', fontsize=12)

plt.tight_layout()
plt.show()