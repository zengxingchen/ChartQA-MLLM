
import matplotlib.pyplot as plt

data = [
    {'Day': 'Monday', 'Philosophy Lectures': 10, 'Ethics Workshops': 15, 'Reading Sessions': 20, 'Debates': 25, 'Group Discussions': 30},
    {'Day': 'Tuesday', 'Philosophy Lectures': 12, 'Ethics Workshops': 14, 'Reading Sessions': 19, 'Debates': 22, 'Group Discussions': 28},
    {'Day': 'Wednesday', 'Philosophy Lectures': 14, 'Ethics Workshops': 13, 'Reading Sessions': 18, 'Debates': 20, 'Group Discussions': 26},
    {'Day': 'Thursday', 'Philosophy Lectures': 16, 'Ethics Workshops': 12, 'Reading Sessions': 17, 'Debates': 18, 'Group Discussions': 24},
    {'Day': 'Friday', 'Philosophy Lectures': 18, 'Ethics Workshops': 11, 'Reading Sessions': 16, 'Debates': 16, 'Group Discussions': 22},
    {'Day': 'Saturday', 'Philosophy Lectures': 20, 'Ethics Workshops': 10, 'Reading Sessions': 15, 'Debates': 14, 'Group Discussions': 20},
    {'Day': 'Sunday', 'Philosophy Lectures': 22, 'Ethics Workshops': 9, 'Reading Sessions': 14, 'Debates': 12, 'Group Discussions': 18}
]

days = [item['Day'] for item in data]
philosophy_lectures = [item['Philosophy Lectures'] for item in data]
ethics_workshops = [item['Ethics Workshops'] for item in data]
reading_sessions = [item['Reading Sessions'] for item in data]
debates = [item['Debates'] for item in data]
group_discussions = [item['Group Discussions'] for item in data]

plt.figure(figsize=(14, 10))
plt.plot(days, philosophy_lectures, label='Philosophy Lectures', linestyle='-', marker='o', color='#3498db')
plt.plot(days, ethics_workshops, label='Ethics Workshops', linestyle='--', marker='s', color='#e74c3c')
plt.plot(days, reading_sessions, label='Reading Sessions', linestyle='-.', marker='^', color='#9b59b6')
plt.plot(days, debates, label='Debates', linestyle=':', marker='D', color='#f1c40f')
plt.plot(days, group_discussions, label='Group Discussions', linestyle='-', marker='*', color='#2ecc71')

plt.title('Weekly Philosophy & Ethics Activities', pad=20)
plt.xlabel('Day of the Week')
plt.ylabel('Number of Sessions')
plt.legend(loc='upper left')

plt.grid(True, linestyle='--', linewidth=0.5, color='gray')
plt.gca().invert_yaxis()

for i, txt in enumerate(debates):
    plt.annotate(txt, (days[i], debates[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.tight_layout()
plt.show()