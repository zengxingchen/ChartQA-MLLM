
import matplotlib.pyplot as plt

# Data
activities = ['Reading', 'Writing', 'Studying', 'Exercise', 'Relaxing', 'Cooking',
              'Traveling', 'Hobbies', 'Watching Movies', 'Socializing', 'Volunteering', 'Sleeping', 'Gaming', 'Meditation']
hours_spent = [45, 50, 55, 35, 30, 40, 25, 32, 50, 42, 38, 60, 48, 20]

# Color scheme using specific color codes
colors = ['#FF5733', '#C70039', '#900C3F', '#571845', '#27AE60', '#2980B9',
          '#8E44AD', '#3498DB', '#2ECC71', '#F1C40F', '#E67E22', '#E74C3C',
          '#8A2BE2', '#7FFF00']

# Create horizontal bar chart
plt.figure(figsize=(12, 10))
bars = plt.barh(activities, hours_spent, color=colors, height=0.5)

# Adjusting the width of bars (if vertical, but here height for horizontal bars)
for bar in bars:
    bar.set_height(0.4)

# Changing the layout and labels
plt.xlabel('Hours Spent', fontsize=12)
plt.title('Weekly Activity Distribution in Leisure & Entertainment', fontsize=16, pad=20)
plt.xlim(min(hours_spent) - 5, max(hours_spent) * 1.1)  # Set x-axis limit higher to accommodate labels

# Adding value labels at the end of each bar
for i, v in enumerate(hours_spent):
    plt.text(v + 1, i, str(v), color='black', va='center', fontsize=11)

# Show the final result
plt.tight_layout()
plt.show()