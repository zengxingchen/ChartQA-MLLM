
import matplotlib.pyplot as plt

# Data
time_of_day = ['Morning', 'Afternoon', 'Evening', 'Night']
cardio = [1.2, 1.5, 1.8, 1.0]
strength = [0.8, 1.0, 1.2, 0.7]
flexibility = [0.6, 0.7, 0.9, 0.5]
balance = [0.4, 0.3, 0.6, 0.2]

# Offsets for stacked bars
bottom_offset_cardio = [0, 0, 0, 0]
bottom_offset_strength = [a+b for a, b in zip(bottom_offset_cardio, cardio)]
bottom_offset_flexibility = [a+b for a, b in zip(bottom_offset_strength, strength)]
bottom_offset_balance = [a+b for a, b in zip(bottom_offset_flexibility, flexibility)]

# Create horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Stacked bars
ax.barh(time_of_day, cardio, height=0.6, left=bottom_offset_cardio, color='#FF4500')  # OrangeRed
ax.barh(time_of_day, strength, height=0.6, left=bottom_offset_strength, color='#32CD32')  # LimeGreen
ax.barh(time_of_day, flexibility, height=0.6, left=bottom_offset_flexibility, color='#1E90FF')  # DodgerBlue
ax.barh(time_of_day, balance, height=0.6, left=bottom_offset_balance, color='#FFD700')  # Gold

# Add some text for labels, title, and custom y-axis tick labels, etc.
ax.set_xlabel('Hours')
ax.set_title('Fitness Activity by Time of Day', pad=20)
ax.set_yticks(range(len(time_of_day)))
ax.set_yticklabels(time_of_day)
ax.set_ylabel('Time of Day')

# Display the legend
ax.legend(['Cardio', 'Strength', 'Flexibility', 'Balance'], loc='upper right')

# Add numerical labels
for i, (c, s, f, b) in enumerate(zip(cardio, strength, flexibility, balance)):
    ax.text(c / 2, i, f'{c}', va='center', ha='center', color='white', fontweight='bold')
    ax.text(c + s / 2, i, f'{s}', va='center', ha='center', color='white', fontweight='bold')
    ax.text(c + s + f / 2, i, f'{f}', va='center', ha='center', color='white', fontweight='bold')
    ax.text(c + s + f + b / 2, i, f'{b}', va='center', ha='center', color='white', fontweight='bold')

# Display the plot
plt.tight_layout()
plt.show()