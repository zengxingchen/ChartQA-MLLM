
import matplotlib.pyplot as plt

data = [
    {'Day': 'Monday', 'Cardio Sessions': 50, 'Strength Training': 60, 'Yoga Sessions': 45, 'HIIT Sessions': 30, 'Pilates Sessions': 40},
    {'Day': 'Tuesday', 'Cardio Sessions': 55, 'Strength Training': 58, 'Yoga Sessions': 48, 'HIIT Sessions': 33, 'Pilates Sessions': 42},
    {'Day': 'Wednesday', 'Cardio Sessions': 53, 'Strength Training': 65, 'Yoga Sessions': 47, 'HIIT Sessions': 35, 'Pilates Sessions': 44},
    {'Day': 'Thursday', 'Cardio Sessions': 57, 'Strength Training': 70, 'Yoga Sessions': 50, 'HIIT Sessions': 40, 'Pilates Sessions': 45},
    {'Day': 'Friday', 'Cardio Sessions': 60, 'Strength Training': 75, 'Yoga Sessions': 55, 'HIIT Sessions': 45, 'Pilates Sessions': 50},
    {'Day': 'Saturday', 'Cardio Sessions': 65, 'Strength Training': 80, 'Yoga Sessions': 60, 'HIIT Sessions': 50, 'Pilates Sessions': 55},
    {'Day': 'Sunday', 'Cardio Sessions': 62, 'Strength Training': 78, 'Yoga Sessions': 58, 'HIIT Sessions': 48, 'Pilates Sessions': 52}
]

days = [item['Day'] for item in data]
cardio_sessions = [item['Cardio Sessions'] for item in data]
strength_training = [item['Strength Training'] for item in data]
yoga_sessions = [item['Yoga Sessions'] for item in data]
hiit_sessions = [item['HIIT Sessions'] for item in data]
pilates_sessions = [item['Pilates Sessions'] for item in data]

plt.figure(figsize=(16, 12))
plt.plot(days, cardio_sessions, label='Cardio Sessions', linestyle='-', marker='o', color='#1b9e77')
plt.plot(days, strength_training, label='Strength Training', linestyle='--', marker='s', color='#d95f02')
plt.plot(days, yoga_sessions, label='Yoga Sessions', linestyle='-.', marker='^', color='#7570b3')
plt.plot(days, hiit_sessions, label='HIIT Sessions', linestyle=':', marker='D', color='#e7298a')
plt.plot(days, pilates_sessions, label='Pilates Sessions', linestyle='-', marker='*', color='#66a61e')

plt.title('Weekly Workout Sessions', pad=20)
plt.xlabel('Day of the Week')
plt.ylabel('Number of Sessions')
plt.legend(loc='upper left')

plt.grid(True, linestyle='--', linewidth=0.5, color='gray')

for i, txt in enumerate(hiit_sessions):
    plt.annotate(txt, (days[i], hiit_sessions[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.tight_layout()
plt.show()