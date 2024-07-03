
import matplotlib.pyplot as plt

# Data
categories = ['Running', 'Cycling', 'Swimming', 'Yoga', 'Weightlifting', 'Pilates', 'Hiking', 'Boxing', 'Rowing', 'Dance']
values = [75, 90, 60, 40, 55, 45, 80, 50, 70, 65]

# Color codes for each bar
colors = ['#FF5733', '#33FFDA', '#3385FF', '#6B33FF', '#FF33B0', '#FF339A', '#FF3364', '#FF3344', '#FF3366', '#FF3380']

# Bar width
bar_width = 0.4

# Create horizontal bar chart
plt.figure(figsize=(18, 12))
bar_container = plt.barh(categories, values, color=colors, height=bar_width)

# Add data labels
for bar in bar_container:
    width = bar.get_width()
    plt.text(width + 1, bar.get_y() + bar.get_height()/2, f'{width}', ha='center', va='bottom')

# Title and labels
plt.title('Time Spent on Sports Activities (Minutes)', pad=20)
plt.xlabel('Time (Minutes)')
plt.ylabel('Activities')

# Customize the grid
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Set y-axis limits for truncated effect
plt.xlim(30, 100)

# Show plot
plt.show()