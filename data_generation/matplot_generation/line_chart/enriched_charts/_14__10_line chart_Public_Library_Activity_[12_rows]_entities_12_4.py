
import matplotlib.pyplot as plt

data = [
    {'Month': 'January', 'Cardio Workouts': 300, 'Strength Training': 280, 'Yoga Sessions': 250, 'HIIT Sessions': 270},
    {'Month': 'February', 'Cardio Workouts': 310, 'Strength Training': 290, 'Yoga Sessions': 240, 'HIIT Sessions': 260},
    {'Month': 'March', 'Cardio Workouts': 320, 'Strength Training': 270, 'Yoga Sessions': 230, 'HIIT Sessions': 250},
    {'Month': 'April', 'Cardio Workouts': 330, 'Strength Training': 260, 'Yoga Sessions': 220, 'HIIT Sessions': 240},
    {'Month': 'May', 'Cardio Workouts': 340, 'Strength Training': 250, 'Yoga Sessions': 210, 'HIIT Sessions': 230},
    {'Month': 'June', 'Cardio Workouts': 350, 'Strength Training': 240, 'Yoga Sessions': 200, 'HIIT Sessions': 220},
    {'Month': 'July', 'Cardio Workouts': 360, 'Strength Training': 230, 'Yoga Sessions': 190, 'HIIT Sessions': 210},
    {'Month': 'August', 'Cardio Workouts': 370, 'Strength Training': 220, 'Yoga Sessions': 180, 'HIIT Sessions': 200},
    {'Month': 'September', 'Cardio Workouts': 380, 'Strength Training': 210, 'Yoga Sessions': 170, 'HIIT Sessions': 190},
    {'Month': 'October', 'Cardio Workouts': 390, 'Strength Training': 200, 'Yoga Sessions': 160, 'HIIT Sessions': 180},
    {'Month': 'November', 'Cardio Workouts': 400, 'Strength Training': 190, 'Yoga Sessions': 150, 'HIIT Sessions': 170},
    {'Month': 'December', 'Cardio Workouts': 410, 'Strength Training': 180, 'Yoga Sessions': 140, 'HIIT Sessions': 160}
]

months = [entry['Month'] for entry in data]
cardio_workouts = [entry['Cardio Workouts'] for entry in data]
strength_training = [entry['Strength Training'] for entry in data]
yoga_sessions = [entry['Yoga Sessions'] for entry in data]
hiit_sessions = [entry['HIIT Sessions'] for entry in data]

plt.figure(figsize=(14, 8))

plt.plot(months, cardio_workouts, label='Cardio Workouts', color='#1f77b4', linestyle='-', marker='o')
plt.plot(months, strength_training, label='Strength Training', color='#ff7f0e', linestyle='--', marker='s')
plt.plot(months, yoga_sessions, label='Yoga Sessions', color='#2ca02c', linestyle='-.', marker='^')
plt.plot(months, hiit_sessions, label='HIIT Sessions', color='#d62728', linestyle=':', marker='x')

plt.title('Monthly Fitness Activities in 2023', fontsize=18, pad=20)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Sessions', fontsize=14)

plt.legend(loc='upper left')
plt.grid(True)

plt.gca().invert_yaxis()

plt.xticks(rotation=45)
plt.yticks(range(0, 450, 50))

for i, txt in enumerate(cardio_workouts):
    plt.annotate(txt, (months[i], cardio_workouts[i]), textcoords="offset points", xytext=(0,5), ha='center')
for i, txt in enumerate(strength_training):
    plt.annotate(txt, (months[i], strength_training[i]), textcoords="offset points", xytext=(0,5), ha='center')
for i, txt in enumerate(yoga_sessions):
    plt.annotate(txt, (months[i], yoga_sessions[i]), textcoords="offset points", xytext=(0,5), ha='center')
for i, txt in enumerate(hiit_sessions):
    plt.annotate(txt, (months[i], hiit_sessions[i]), textcoords="offset points", xytext=(0,5), ha='center')

plt.tight_layout()
plt.show()