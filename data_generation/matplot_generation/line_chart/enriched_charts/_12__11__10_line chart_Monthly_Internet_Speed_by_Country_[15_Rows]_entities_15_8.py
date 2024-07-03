
import matplotlib.pyplot as plt

chart_data = [
    {'Month': 'January', 'Page Views': 1200, 'Unique Visitors': 400, 'Bounce Rate': 70, 'Session Duration': 2.5},
    {'Month': 'February', 'Page Views': 1300, 'Unique Visitors': 450, 'Bounce Rate': 65, 'Session Duration': 2.8},
    {'Month': 'March', 'Page Views': 1100, 'Unique Visitors': 420, 'Bounce Rate': 68, 'Session Duration': 2.6},
    {'Month': 'April', 'Page Views': 1400, 'Unique Visitors': 480, 'Bounce Rate': 60, 'Session Duration': 3.0},
    {'Month': 'May', 'Page Views': 1500, 'Unique Visitors': 500, 'Bounce Rate': 55, 'Session Duration': 3.1},
    {'Month': 'June', 'Page Views': 1600, 'Unique Visitors': 550, 'Bounce Rate': 50, 'Session Duration': 3.3},
    {'Month': 'July', 'Page Views': 1700, 'Unique Visitors': 600, 'Bounce Rate': 45, 'Session Duration': 3.5},
    {'Month': 'August', 'Page Views': 1800, 'Unique Visitors': 650, 'Bounce Rate': 40, 'Session Duration': 3.7},
    {'Month': 'September', 'Page Views': 1900, 'Unique Visitors': 700, 'Bounce Rate': 35, 'Session Duration': 3.9},
    {'Month': 'October', 'Page Views': 2000, 'Unique Visitors': 750, 'Bounce Rate': 30, 'Session Duration': 4.0},
    {'Month': 'November', 'Page Views': 2100, 'Unique Visitors': 800, 'Bounce Rate': 28, 'Session Duration': 4.2},
    {'Month': 'December', 'Page Views': 2200, 'Unique Visitors': 850, 'Bounce Rate': 25, 'Session Duration': 4.4}
]

months = [entry['Month'] for entry in chart_data]
page_views = [entry['Page Views'] for entry in chart_data]
unique_visitors = [entry['Unique Visitors'] for entry in chart_data]
bounce_rate = [entry['Bounce Rate'] for entry in chart_data]
session_duration = [entry['Session Duration'] for entry in chart_data]

plt.figure(figsize=(16, 8))

plt.plot(months, page_views, label='Page Views', marker='o', linestyle='-', color='#4B0082')
plt.plot(months, unique_visitors, label='Unique Visitors', marker='s', linestyle='--', color='#FFD700')
plt.plot(months, bounce_rate, label='Bounce Rate', marker='^', linestyle='-.', color='#DC143C')
plt.plot(months, session_duration, label='Session Duration', marker='d', linestyle=':', color='#008080')

plt.title('Monthly Website Analytics', fontsize=20, pad=20)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Metrics', fontsize=14)
plt.xticks(rotation=45, fontsize=12)

for i, txt in enumerate(page_views):
    plt.annotate(txt, (months[i], page_views[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.legend(loc='upper right', fontsize=12)

plt.tight_layout()
plt.show()