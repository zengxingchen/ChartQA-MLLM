
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Painting', 'Sculpture', 'Photography', 'Digital Art', 'Graphic Design', 'Fashion Design', 'Calligraphy']
cardio = [20, 15, 10, 25, 30, 35, 40]
strength_training = [25, 30, 35, 20, 15, 10, 25]
flexibility = [30, 25, 20, 30, 25, 20, 20]
balance = [25, 30, 35, 25, 30, 35, 15]

# Define bar width and positions
bar_width = 0.6
r = np.arange(len(categories))

# Create the percentage stacked bar chart
fig, ax = plt.subplots(figsize=(10, 12))

# Plot each type of workout
p1 = plt.bar(r, cardio, color='#FF5733', edgecolor='grey', width=bar_width)
p2 = plt.bar(r, strength_training, bottom=cardio, color='#33FF57', edgecolor='grey', width=bar_width)
p3 = plt.bar(r, flexibility, bottom=np.add(cardio, strength_training), color='#3357FF', edgecolor='grey', width=bar_width)
p4 = plt.bar(r, balance, bottom=np.add(cardio, np.add(strength_training, flexibility)), color='#FF33A1', edgecolor='grey', width=bar_width)

# Add labels
plt.xlabel('Art Category')
plt.ylabel('Percentage')
plt.title('Percentage Distribution of Skills in Various Art Categories')
plt.xticks(r, categories, rotation=45)
plt.yticks(np.arange(0, 101, 10))

# Add legend
plt.legend((p1[0], p2[0], p3[0], p4[0]), ('Cardio', 'Strength Training', 'Flexibility', 'Balance'), loc='upper left')

# Show plot
plt.tight_layout()
plt.show()