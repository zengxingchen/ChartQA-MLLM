
import matplotlib.pyplot as plt

# Data
categories = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
cardio = [1.5, 2.0, 1.8, 2.2, 1.6, 2.5, 1.7]
strength = [1.0, 1.2, 1.5, 1.3, 1.1, 1.8, 1.4]
flexibility = [0.5, 0.8, 0.6, 0.9, 0.7, 1.0, 0.8]
balance = [0.2, 0.3, 0.4, 0.5, 0.2, 0.6, 0.3]

# Offsets for stacked bars
bottom_offset_cardio = [0] * len(categories)
bottom_offset_strength = [a + b for a, b in zip(bottom_offset_cardio, cardio)]
bottom_offset_flexibility = [a + b for a, b in zip(bottom_offset_strength, strength)]
bottom_offset_balance = [a + b for a, b in zip(bottom_offset_flexibility, flexibility)]

# Create vertical bar chart
fig, ax = plt.subplots(figsize=(10, 12))

# Stacked bars
ax.bar(categories, cardio, width=0.5, bottom=bottom_offset_cardio, color='#FF6347')  # Tomato
ax.bar(categories, strength, width=0.5, bottom=bottom_offset_strength, color='#4682B4')  # SteelBlue
ax.bar(categories, flexibility, width=0.5, bottom=bottom_offset_flexibility, color='#8FBC8F')  # DarkSeaGreen
ax.bar(categories, balance, width=0.5, bottom=bottom_offset_balance, color='#FFD700')  # Gold

# Add some text for labels, title, and custom y-axis tick labels, etc.
ax.set_ylabel('Hours')
ax.set_title('Average Weekly Exercise Hours by Activity', pad=20)
ax.set_xticks(range(len(categories)))
ax.set_xticklabels(categories)
ax.set_xlabel('Days of the Week')

# Display the legend
ax.legend(['Cardio', 'Strength', 'Flexibility', 'Balance'], loc='upper right')

# Add numerical labels to each bar
for i in range(len(categories)):
    ax.text(i, cardio[i] / 2, str(cardio[i]), va='center', ha='center', color='black')
    ax.text(i, cardio[i] + strength[i] / 2, str(strength[i]), va='center', ha='center', color='black')
    ax.text(i, cardio[i] + strength[i] + flexibility[i] / 2, str(flexibility[i]), va='center', ha='center', color='black')
    ax.text(i, cardio[i] + strength[i] + flexibility[i] + balance[i] / 2, str(balance[i]), va='center', ha='center', color='black')

# Display the plot
plt.tight_layout()
plt.show()