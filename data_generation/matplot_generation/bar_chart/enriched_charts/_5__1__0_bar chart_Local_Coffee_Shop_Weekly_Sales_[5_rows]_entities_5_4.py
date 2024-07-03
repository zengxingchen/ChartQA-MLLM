
import matplotlib.pyplot as plt

# Data
activities = ['Soccer', 'Basketball', 'Tennis', 'Swimming', 'Cycling', 'Running', 
              'Yoga', 'Hiking', 'Gym Workout', 'Boxing', 'Martial Arts', 'Dancing']
hours_spent = [70, 65, 55, 80, 60, 75, 50, 85, 90, 45, 65, 70]

# Color scheme using color codes
colors = ['#1F618D', '#2874A6', '#2E86C1', '#3498DB', '#5DADE2', '#76D7C4',
          '#52BE80', '#27AE60', '#229954', '#1E8449', '#196F3D', '#145A32']

# Create horizontal bar chart
plt.figure(figsize=(12, 8))
bars = plt.barh(activities, hours_spent, color=colors, height=0.6)

# Adjusting the width and height of bars
for bar in bars:
    bar.set_height(0.5)

# Changing the layout and labels
plt.xlabel('Hours Spent', fontsize=12)
plt.title('Weekly Sports Activity Distribution', fontsize=16, pad=20)
plt.xlim(min(hours_spent) * 0.9, max(hours_spent) * 1.1)  # Set x-axis limit higher to accommodate labels

# Adding value labels on the side of each bar
for i, v in enumerate(hours_spent):
    plt.text(v + 1, i, str(v), color='black', va='center', fontsize=11)

# Show the final result
plt.tight_layout()
plt.show()