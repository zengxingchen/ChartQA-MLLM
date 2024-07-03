
import matplotlib.pyplot as plt

# Data
activities = ['Reading', 'Writing', 'Studying', 'Exercise', 'Relaxing', 'Cooking',
              'Traveling', 'Hobbies', 'Watching TV', 'Socializing', 'Volunteering', 'Sleeping',
              'Gardening', 'Gaming', 'Music Practice', 'Shopping']
hours_spent = [75, 62, 80, 55, 68, 45, 40, 60, 70, 65, 50, 90, 48, 53, 58, 63]

# Color scheme using color codes
colors = ['#FF6347', '#8B0000', '#FF4500', '#2E8B57', '#4682B4', '#D2691E',
          '#6A5ACD', '#DB7093', '#7FFF00', '#FF69B4', '#1E90FF', '#B22222',
          '#4B0082', '#FF8C00', '#FFD700', '#2F4F4F']

# Create vertical bar chart
plt.figure(figsize=(14, 8))
bars = plt.bar(activities, hours_spent, color=colors, width=0.5)

# Adjusting the width of bars
for bar in bars:
    bar.set_width(0.4)

# Changing the layout and labels
plt.ylabel('Frequency', fontsize=12)
plt.title('Weekly Activity Frequency', fontsize=16)
plt.ylim(min(hours_spent) - 5, max(hours_spent) + 10)  # Set y-axis limit to start from a specific value

# Adding value labels on top of each bar
for i, v in enumerate(hours_spent):
    plt.text(i, v + 1, str(v), color='black', ha='center', fontsize=11)

# Show the final result
plt.tight_layout()
plt.show()