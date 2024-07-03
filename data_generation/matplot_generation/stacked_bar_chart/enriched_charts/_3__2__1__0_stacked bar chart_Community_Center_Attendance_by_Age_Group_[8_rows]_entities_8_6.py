
import matplotlib.pyplot as plt

events = ['Music Festival', 'Theater Show', 'Art Exhibition', 'Film Screening', 'Dance Performance', 'Concert', 'Opera', 'Stand-up Comedy', 'Circus', 'Magic Show']
attendance = [15000, 12000, 8000, 10000, 9000, 20000, 7000, 6000, 11000, 5000]
revenue = [75000, 65000, 30000, 40000, 35000, 100000, 50000, 25000, 45000, 20000]
duration = [4, 3, 2, 2.5, 3, 5, 3.5, 2, 3.5, 1.5]
rating = [4.5, 4.2, 4.0, 4.3, 4.1, 4.7, 4.4, 3.9, 4.2, 3.8]

fig, ax = plt.subplots(figsize=(12, 8))  # Set width and height of the chart
bars1 = ax.barh(events, attendance, label='Attendance', color='#FF5733', edgecolor='white', height=0.5)
bars2 = ax.barh(events, revenue, label='Revenue', color='#33FF57', edgecolor='white', height=0.5, left=attendance)
bars3 = ax.barh(events, duration, label='Duration (hrs)', color='#3357FF', edgecolor='white', height=0.5, left=[i+j for i, j in zip(attendance, revenue)])
bars4 = ax.barh(events, rating, label='Rating', color='#FF33A1', edgecolor='white', height=0.5, left=[i+j+k for i, j, k in zip(attendance, revenue, duration)])

ax.set_ylabel('Events')
ax.set_xlabel('Metrics')
ax.set_title('Event Metrics for Various Entertainment & Leisure Events', pad=20)
ax.legend(loc='upper right')

for bar in bars1:
    width = bar.get_width()
    plt.text(width + 500, bar.get_y() + bar.get_height()/2, width, ha='center', va='bottom')
for bar, width in zip(bars2, revenue):
    plt.text(bar.get_x() + bar.get_width() + width/2, bar.get_y() + bar.get_height()/2, width, ha='center', va='bottom')
for bar, width in zip(bars3, duration):
    plt.text(bar.get_x() + bar.get_width() + width/2, bar.get_y() + bar.get_height()/2, width, ha='center', va='bottom')
for bar, width in zip(bars4, rating):
    plt.text(bar.get_x() + bar.get_width() + width/2, bar.get_y() + bar.get_height()/2, width, ha='center', va='bottom')

plt.show()