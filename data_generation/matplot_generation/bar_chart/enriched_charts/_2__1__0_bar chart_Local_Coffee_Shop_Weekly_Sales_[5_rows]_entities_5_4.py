
import matplotlib.pyplot as plt

# Data
sports = ['Basketball', 'Football', 'Swimming', 'Tennis', 'Cycling', 'Running',
          'Yoga', 'Gym', 'Hiking', 'Badminton', 'Boxing', 'Dancing', 'Skating', 'Martial Arts', 'Rock Climbing']
hours_spent = [38, 45, 30, 35, 42, 28, 25, 40, 37, 33, 22, 39, 27, 20, 26]

# Color scheme using color codes
colors = ['#1E90FF', '#32CD32', '#FFD700', '#FF4500', '#8A2BE2', '#00CED1',
          '#FF1493', '#7FFF00', '#FF69B4', '#87CEEB', '#FF6347', '#8B0000', '#40E0D0', '#BA55D3', '#4682B4']

# Create horizontal bar chart
plt.figure(figsize=(12, 10))
bars = plt.barh(sports, hours_spent, color=colors, height=0.7)

# Adjusting the height and width of bars
for bar in bars:
    bar.set_height(0.6)

# Changing the layout and labels
plt.xlabel('Hours Spent', fontsize=12)
plt.title('Weekly Sports Activity Distribution', fontsize=16)
plt.xlim(0, max(hours_spent) * 1.1)  # Set x-axis limit higher to accommodate labels

# Adding value labels on top of each bar
for i, v in enumerate(hours_spent):
    plt.text(v + 1, i, str(v), color='black', va='center', fontsize=11)

# Show the final result
plt.tight_layout()
plt.show()