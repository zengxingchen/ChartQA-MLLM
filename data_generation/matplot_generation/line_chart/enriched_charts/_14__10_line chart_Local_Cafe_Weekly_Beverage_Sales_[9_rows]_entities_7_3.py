
import matplotlib.pyplot as plt

# Table data provided
data = [
    {'Day': 'Monday', 'Running': 45, 'Yoga': 35, 'StrengthTraining': 50, 'Cycling': 60, 'Swimming': 40},
    {'Day': 'Tuesday', 'Running': 50, 'Yoga': 40, 'StrengthTraining': 55, 'Cycling': 65, 'Swimming': 45},
    {'Day': 'Wednesday', 'Running': 40, 'Yoga': 45, 'StrengthTraining': 60, 'Cycling': 70, 'Swimming': 50},
    {'Day': 'Thursday', 'Running': 60, 'Yoga': 50, 'StrengthTraining': 65, 'Cycling': 75, 'Swimming': 55},
    {'Day': 'Friday', 'Running': 70, 'Yoga': 55, 'StrengthTraining': 70, 'Cycling': 80, 'Swimming': 60},
    {'Day': 'Saturday', 'Running': 80, 'Yoga': 60, 'StrengthTraining': 75, 'Cycling': 90, 'Swimming': 65},
    {'Day': 'Sunday', 'Running': 85, 'Yoga': 65, 'StrengthTraining': 80, 'Cycling': 100, 'Swimming': 70}
]

# Extracting data for plotting
days = [item['Day'] for item in data]
running = [item['Running'] for item in data]
yoga = [item['Yoga'] for item in data]
strength_training = [item['StrengthTraining'] for item in data]
cycling = [item['Cycling'] for item in data]
swimming = [item['Swimming'] for item in data]

# Creating a line chart with a different line style and marker for each exercise type
plt.figure(figsize=(14, 9))
plt.plot(days, running, label='Running', linestyle='-', marker='o', color='#1f77b4')
plt.plot(days, yoga, label='Yoga', linestyle='--', marker='s', color='#ff7f0e')
plt.plot(days, strength_training, label='Strength Training', linestyle='-.', marker='^', color='#2ca02c')
plt.plot(days, cycling, label='Cycling', linestyle=':', marker='D', color='#d62728')
plt.plot(days, swimming, label='Swimming', linestyle='-', marker='*', color='#9467bd')

# Adding relevant titles and labels
plt.title('Weekly Exercise Routine', pad=30)
plt.xlabel('Day of the Week')
plt.ylabel('Minutes of Exercise')
plt.legend(loc='upper left')

# Customizing the grid
plt.grid(True, linestyle='--', linewidth=0.5, color='gray')

# Adding annotations
for i, txt in enumerate(cycling):
    plt.annotate(txt, (days[i], cycling[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Inverting y-axis
plt.gca().invert_yaxis()

# Displaying the chart
plt.tight_layout()
plt.show()