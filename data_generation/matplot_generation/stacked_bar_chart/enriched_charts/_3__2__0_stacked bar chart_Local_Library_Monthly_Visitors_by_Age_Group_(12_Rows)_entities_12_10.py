
import matplotlib.pyplot as plt

# Data
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
cardio_hours = [1.5, 2.0, 1.0, 1.5, 1.0, 2.5, 2.0]
strength_hours = [0.5, 0.5, 1.0, 1.0, 0.5, 1.5, 1.0]
flexibility_hours = [0.5, 0.5, 0.5, 0.5, 1.0, 1.0, 0.5]

# Offsets for stacked bars
left_offset_cardio = [0] * len(cardio_hours)
left_offset_strength = [a + b for a, b in zip(left_offset_cardio, cardio_hours)]
left_offset_flexibility = [a + b for a, b in zip(left_offset_strength, strength_hours)]

# Create horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Stacked bars
ax.barh(days, cardio_hours, height=0.4, left=left_offset_cardio, color='#1f77b4')  # Blue
ax.barh(days, strength_hours, height=0.4, left=left_offset_strength, color='#ff7f0e')  # Orange
ax.barh(days, flexibility_hours, height=0.4, left=left_offset_flexibility, color='#2ca02c')  # Green

# Add some text for labels, title, and custom y-axis tick labels, etc.
ax.set_xlabel('Hours')
ax.set_title('Weekly Exercise Routine')
ax.legend(['Cardio', 'Strength', 'Flexibility'], loc='lower right')

# Numerical labels for each bar segment
for i in range(len(days)):
    ax.text(cardio_hours[i] / 2, i, str(cardio_hours[i]), ha='center', va='center', color='black')
    ax.text(left_offset_strength[i] + strength_hours[i] / 2, i, str(strength_hours[i]), ha='center', va='center', color='black')
    ax.text(left_offset_flexibility[i] + flexibility_hours[i] / 2, i, str(flexibility_hours[i]), ha='center', va='center', color='black')

plt.tight_layout()
plt.show()