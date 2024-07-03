
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
calories_running = [300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410]
calories_swimming = [250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360]
calories_cycling = [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310]

# Color codes for each activity
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Plot stacked vertical bar chart
plt.figure(figsize=(12, 10))  # Width and height of the chart in inches
bar_width = 0.5  # Width of the bars

plt.bar(months, calories_running, color=colors[0], edgecolor='white', width=bar_width, label='Running')
plt.bar(months, calories_swimming, bottom=calories_running, color=colors[1], edgecolor='white', width=bar_width, label='Swimming')
plt.bar(months, calories_cycling, bottom=[i+j for i, j in zip(calories_running, calories_swimming)], color=colors[2], edgecolor='white', width=bar_width, label='Cycling')

# Add labels and title
plt.ylabel('Calories')
plt.xlabel('Month')
plt.title('Monthly Caloric Burn from Different Activities')
plt.legend(loc='upper left')

# Add numerical labels
for i, (run, swim, cycle) in enumerate(zip(calories_running, calories_swimming, calories_cycling)):
    plt.text(i, run / 2, str(run), ha='center', va='center', color='white', fontweight='bold')
    plt.text(i, run + swim / 2, str(swim), ha='center', va='center', color='white', fontweight='bold')
    plt.text(i, run + swim + cycle / 2, str(cycle), ha='center', va='center', color='white', fontweight='bold')

# Display the final result
plt.show()