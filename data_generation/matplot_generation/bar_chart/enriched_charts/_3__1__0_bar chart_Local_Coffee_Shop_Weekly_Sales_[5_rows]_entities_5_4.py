import matplotlib.pyplot as plt

# Data
activities = ['Reading', 'Writing', 'Studying', 'Exercise', 'Relaxing', 'Cooking',
              'Traveling', 'Hobbies', 'Watching TV', 'Socializing', 'Volunteering', 'Sleeping',
              'Gardening', 'Gaming', 'Music Practice', 'Shopping']
hours_spent = [50, 45, 60, 30, 40, 25, 20, 35, 55, 48, 28, 56, 22, 33, 27, 38]

# Color scheme using color codes
colors = ['#FF5733', '#C70039', '#900C3F', '#571845', '#27AE60', '#2980B9',
          '#8E44AD', '#3498DB', '#2ECC71', '#F1C40F', '#E67E22', '#E74C3C',
          '#16A085', '#F39C12', '#D35400', '#7D3C98']

# Create horizontal bar chart
plt.figure(figsize=(12, 10))
bars = plt.barh(activities, hours_spent, color=colors, height=0.6)

# Adjusting the width and height of bars
for bar in bars:
    bar.set_height(0.5)

# Changing the layout and labels
plt.xlabel('Hours Spent', fontsize=12)
plt.title('Weekly Activity Distribution', fontsize=16)
plt.xlim(0, max(hours_spent) * 1.1)  # Set x-axis limit higher to accommodate labels

# Adding value labels on top of each bar
for i, v in enumerate(hours_spent):
    plt.text(v + 1, i, str(v), color='black', va='center', fontsize=11)

# Show the final result
plt.tight_layout()
plt.show()