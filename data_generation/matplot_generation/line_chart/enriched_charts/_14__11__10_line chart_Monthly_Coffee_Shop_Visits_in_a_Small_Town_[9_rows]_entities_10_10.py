
import matplotlib.pyplot as plt

data = [
    {'Month': 'January', 'Reading': 30, 'Painting': 40, 'Writing': 50, 'Sculpting': 60, 'Dancing': 70},
    {'Month': 'February', 'Reading': 35, 'Painting': 45, 'Writing': 55, 'Sculpting': 65, 'Dancing': 75},
    {'Month': 'March', 'Reading': 40, 'Painting': 50, 'Writing': 60, 'Sculpting': 70, 'Dancing': 80},
    {'Month': 'April', 'Reading': 45, 'Painting': 55, 'Writing': 65, 'Sculpting': 75, 'Dancing': 85},
    {'Month': 'May', 'Reading': 50, 'Painting': 60, 'Writing': 70, 'Sculpting': 80, 'Dancing': 90},
    {'Month': 'June', 'Reading': 55, 'Painting': 65, 'Writing': 75, 'Sculpting': 85, 'Dancing': 95},
    {'Month': 'July', 'Reading': 60, 'Painting': 70, 'Writing': 80, 'Sculpting': 90, 'Dancing': 100},
    {'Month': 'August', 'Reading': 65, 'Painting': 75, 'Writing': 85, 'Sculpting': 95, 'Dancing': 105},
    {'Month': 'September', 'Reading': 70, 'Painting': 80, 'Writing': 90, 'Sculpting': 100, 'Dancing': 110},
    {'Month': 'October', 'Reading': 75, 'Painting': 85, 'Writing': 95, 'Sculpting': 105, 'Dancing': 115},
    {'Month': 'November', 'Reading': 70, 'Painting': 80, 'Writing': 90, 'Sculpting': 100, 'Dancing': 110},
    {'Month': 'December', 'Reading': 65, 'Painting': 75, 'Writing': 85, 'Sculpting': 95, 'Dancing': 105}
]

months = [entry['Month'] for entry in data]

plt.figure(figsize=(14, 10))
activities = list(data[0].keys())[1:]

line_styles = ['-', '--', '-.', ':']
markers = ['o', '^', 's', 'D', 'x']
colors = ['#ff6347', '#4682b4', '#32cd32', '#800080', '#ffd700']

for i, activity in enumerate(activities):
    values = [entry[activity] for entry in data]
    plt.plot(months, values, label=activity, linestyle=line_styles[i % len(line_styles)], marker=markers[i % len(markers)], color=colors[i % len(colors)])
    plt.text(months[-1], values[-1], f'{values[-1]}', fontsize=10, color=colors[i % len(colors)])

plt.title('Monthly Creative Activities Participation', pad=20)
plt.xlabel('Month')
plt.ylabel('Participation (in thousands)')
plt.grid(True)
plt.legend(title='Activities', loc='upper left', bbox_to_anchor=(1, 1))
plt.gca().invert_yaxis()
plt.show()