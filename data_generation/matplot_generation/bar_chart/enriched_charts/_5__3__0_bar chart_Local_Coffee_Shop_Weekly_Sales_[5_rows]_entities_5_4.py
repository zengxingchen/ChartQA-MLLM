
import matplotlib.pyplot as plt

# Data
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
calories = [1800, 2200, 1700, 2100, 2500, 2700, 2300]

# Color scheme using specific color codes
colors = ['#FF4500', '#32CD32', '#FFD700', '#1E90FF', '#FF69B4', '#8A2BE2', '#00CED1']

# Create horizontal bar chart
plt.figure(figsize=(12, 8))
bars = plt.barh(days, calories, color=colors, height=0.5)

# Adjusting the y-axis limits to start from 1500 instead of 0
plt.xlim(1500, max(calories) * 1.1)

# Changing the layout and labels
plt.xlabel('Calories', fontsize=12)
plt.title('Weekly Calorie Intake', fontsize=16)
plt.gca().invert_yaxis()  # Invert y-axis to have Monday on top

# Adding value labels on top of each bar
for i, v in enumerate(calories):
    plt.text(v + 50, i, str(v), color='black', va='center', fontsize=11)

# Show the final result
plt.tight_layout()
plt.show()