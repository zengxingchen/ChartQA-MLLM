import matplotlib.pyplot as plt
import numpy as np

# Data
age_groups = ['18-25', '26-35', '36-45', '46-55', '56-65', '66+']
cardio = [35, 30, 25, 20, 15, 10]
strength_training = [25, 30, 35, 30, 25, 20]
flexibility = [25, 20, 25, 30, 35, 40]
balance = [15, 20, 15, 20, 25, 30]

# Define bar width and positions
bar_width = 0.7
r = np.arange(len(age_groups))

# Create the percentage stacked bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plot each type of workout
p1 = plt.barh(r, cardio, color='#1f77b4', edgecolor='grey', height=bar_width)
p2 = plt.barh(r, strength_training, left=cardio, color='#ff7f0e', edgecolor='grey', height=bar_width)
p3 = plt.barh(r, flexibility, left=np.add(cardio, strength_training), color='#2ca02c', edgecolor='grey', height=bar_width)
p4 = plt.barh(r, balance, left=np.add(cardio, np.add(strength_training, flexibility)), color='#d62728', edgecolor='grey', height=bar_width)

# Add labels
plt.ylabel('Age Group')
plt.xlabel('Percentage')
plt.title('Percentage Distribution of Workouts by Age Group')
plt.yticks(r, age_groups)
plt.xticks(np.arange(0, 101, 10))

# Add legend
plt.legend((p1[0], p2[0], p3[0], p4[0]), ('Cardio', 'Strength Training', 'Flexibility', 'Balance'), loc='upper right')

# Show plot
plt.show()