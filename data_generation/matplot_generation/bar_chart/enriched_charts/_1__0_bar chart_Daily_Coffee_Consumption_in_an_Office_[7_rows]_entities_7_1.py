
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
membership_counts = [120, 115, 140, 160, 180, 200, 220, 210, 190, 170, 150, 130]

# Color codes for each bar
colors = ['#FF5733', '#FF8D33', '#FFC433', '#EFFF33', '#B0FF33', '#6AFF33', '#33FF57', '#33FFDA', '#33D2FF', '#3385FF', '#6B33FF', '#D433FF']

# Bar width
bar_width = 0.5

# Create vertical bar chart
plt.figure(figsize=(12, 6))
bar_container = plt.bar(months, membership_counts, color=colors, width=bar_width)

# Add data labels
for bar in bar_container:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 5, f'{height}', ha='center', va='bottom')
    
# Title and labels
plt.title('Average Monthly Gym Membership Count')
plt.xlabel('Month')
plt.ylabel('Membership Count')

# Customize the grid
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show plot
plt.show()