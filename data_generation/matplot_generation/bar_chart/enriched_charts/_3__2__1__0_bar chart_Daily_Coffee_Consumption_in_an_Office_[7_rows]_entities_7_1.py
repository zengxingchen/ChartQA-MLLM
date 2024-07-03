
import matplotlib.pyplot as plt

# Data
categories = ['Reading', 'Exercising', 'Working', 'Sleeping', 'Cooking', 'Meditation', 'Watching TV', 'Gaming', 'Socializing', 'Shopping']
values = [35, 50, 70, 80, 20, 25, 45, 60, 30, 15]

# Color codes for each bar
colors = ['#FF5733', '#33FFDA', '#3385FF', '#6B33FF', '#FF33B0', '#FF339A', '#FF3364', '#FF3344', '#FF3366', '#FF3380']

# Bar width
bar_width = 0.5

# Create vertical bar chart
plt.figure(figsize=(15, 10))
bar_container = plt.bar(categories, values, color=colors, width=bar_width)

# Add data labels
for bar in bar_container:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 1, f'{height}', ha='center', va='bottom')

# Title and labels
plt.title('Daily Activities Time Allocation (Minutes)', pad=20)
plt.xlabel('Activities')
plt.ylabel('Time (Minutes)')

# Customize the grid
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show plot
plt.show()