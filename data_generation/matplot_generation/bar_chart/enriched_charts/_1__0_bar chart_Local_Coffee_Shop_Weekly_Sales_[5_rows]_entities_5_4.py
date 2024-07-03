
import matplotlib.pyplot as plt

# Data
activities = ['Reading', 'Writing', 'Studying', 'Exercise', 'Relaxing', 'Cooking',
              'Traveling', 'Hobbies', 'Watching TV', 'Socializing', 'Volunteering', 'Sleeping']
hours_spent = [50, 45, 60, 30, 40, 25, 20, 35, 55, 48, 28, 56]

# Color scheme using color codes
colors = ['#FF5733', '#C70039', '#900C3F', '#571845', '#27AE60', '#2980B9',
          '#8E44AD', '#3498DB', '#2ECC71', '#F1C40F', '#E67E22', '#E74C3C']

# Create vertical bar chart
plt.figure(figsize=(10, 12))
bars = plt.bar(activities, hours_spent, color=colors, width=0.7)

# Adjusting the width and height of bars
for bar in bars:
    bar.set_width(0.6)

# Changing the layout and labels
plt.ylabel('Hours Spent', fontsize=12)
plt.title('Weekly Activity Distribution', fontsize=16)
plt.ylim(0, max(hours_spent) * 1.1)  # Set y-axis limit higher to accommodate labels

# Adding value labels on top of each bar
for i, v in enumerate(hours_spent):
    plt.text(i, v + 1, str(v), color='black', ha='center', fontsize=11)

# Show the final result
plt.tight_layout()
plt.show()