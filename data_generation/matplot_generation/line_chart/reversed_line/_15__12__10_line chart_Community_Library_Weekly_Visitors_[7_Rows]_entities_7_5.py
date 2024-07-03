
import matplotlib.pyplot as plt

data = [
    {'Month': '2023-01', 'Awareness': 700},
    {'Month': '2023-02', 'Awareness': 680},
    {'Month': '2023-03', 'Awareness': 710},
    {'Month': '2023-04', 'Awareness': 690},
    {'Month': '2023-05', 'Awareness': 750},
    {'Month': '2023-06', 'Awareness': 740},
    {'Month': '2023-07', 'Awareness': 720},
    {'Month': '2023-08', 'Awareness': 760},
    {'Month': '2023-09', 'Awareness': 780},
    {'Month': '2023-10', 'Awareness': 770},
    {'Month': '2023-11', 'Awareness': 800},
    {'Month': '2023-12', 'Awareness': 790}
]

months = [entry['Month'] for entry in data]
awareness = [entry['Awareness'] for entry in data]

plt.figure(figsize=(12, 6))
line, = plt.plot(months, awareness, color='#1E90FF', linestyle='-', linewidth=2, marker='s', markerfacecolor='#FF4500', markeredgewidth=2, markersize=8)

max_awareness = max(awareness)
max_month = months[awareness.index(max_awareness)]
plt.annotate(f'Peak\n{max_awareness}', xy=(max_month, max_awareness), xytext=(max_month, max_awareness + 15),
             arrowprops=dict(facecolor='green', shrink=0.05),
             horizontalalignment='center')

min_awareness = min(awareness)
min_month = months[awareness.index(min_awareness)]
plt.annotate(f'Low\n{min_awareness}', xy=(min_month, min_awareness), xytext=(min_month, min_awareness - 20),
             arrowprops=dict(facecolor='purple', shrink=0.05),
             horizontalalignment='center')

plt.gca().invert_yaxis()
plt.title('Monthly Awareness Levels in 2023', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Awareness (in units)', fontsize=12)
plt.grid(True, which='major', linestyle='--', linewidth=0.5, color='grey')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()