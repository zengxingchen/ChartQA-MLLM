
import matplotlib.pyplot as plt

# Data for plotting
weeks = ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", 
         "Week 7", "Week 8", "Week 9", "Week 10", "Week 11", "Week 12",
         "Week 13", "Week 14", "Week 15", "Week 16", "Week 17", "Week 18",
         "Week 19", "Week 20"]
study_hours = [6, 8, 5, 7, 9, 6.5, 8.5, 7.2, 8.1, 5.8, 9.3, 6.9, 7.8, 8.2, 6.7, 9.5, 7.5, 8.3, 7.6, 8.4]

fig, ax = plt.subplots(figsize=(10, 12))

# Create a vertical bar chart with custom colors and bar widths
bars = ax.bar(weeks, study_hours, width=0.6,
              color=['#003f5c', '#2f4b7c', '#665191', '#a05195', '#d45087', '#f95d6a',
                     '#ff7c43', '#ffa600', '#488f31', '#6ba292', '#75bba7', '#ace8d3',
                     '#003f5c', '#2f4b7c', '#665191', '#a05195', '#d45087', '#f95d6a',
                     '#ff7c43', '#ffa600'])

# Set the chart title and labels
ax.set_title('Average Weekly Study Hours by Students', fontsize=18, pad=20)
ax.set_ylabel('Study Hours', fontsize=14)
ax.set_xlabel('Week', fontsize=14)

# Customize the ticks on both axes
ax.xaxis.set_tick_params(labelsize=12, rotation=45)
ax.yaxis.set_tick_params(labelsize=12)

# Add value labels to each bar
for bar in bars:
    height = bar.get_height()
    label_y_pos = height + 0.3  # Some padding to the top
    ax.text(bar.get_x() + bar.get_width()/2, label_y_pos, f'{height} hours',
            va='center', ha='center', fontsize=12)

plt.tight_layout()
plt.show()