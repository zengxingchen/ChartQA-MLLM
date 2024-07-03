
import matplotlib.pyplot as plt

# Provided data
data = [
    {'Week': '2023-W09', 'Visitors': 350},
    {'Week': '2023-W10', 'Visitors': 400},
    {'Week': '2023-W11', 'Visitors': 380},
    {'Week': '2023-W12', 'Visitors': 450},
    {'Week': '2023-W13', 'Visitors': 430},
    {'Week': '2023-W14', 'Visitors': 320},
    {'Week': '2023-W15', 'Visitors': 370},
    {'Week': '2023-W16', 'Visitors': 420},
    {'Week': '2023-W17', 'Visitors': 390},
    {'Week': '2023-W18', 'Visitors': 460},
    {'Week': '2023-W19', 'Visitors': 440},
    {'Week': '2023-W20', 'Visitors': 410}
]

# Extracting weeks and visitor counts
weeks = [entry['Week'] for entry in data]
visitors = [entry['Visitors'] for entry in data]

# Creating the line chart
plt.figure(figsize=(12, 6))
line, = plt.plot(weeks, visitors, color='#1f77b4', linestyle='-', linewidth=2, marker='o', markerfacecolor='#ff7f0e', markeredgewidth=2, markersize=8)

# Highlighting the highest visitor count
max_visitors = max(visitors)
max_week = weeks[visitors.index(max_visitors)]
plt.annotate(f'Peak\n{max_visitors}', xy=(max_week, max_visitors), xytext=(max_week, max_visitors + 15),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='center')

# Highlighting the lowest visitor count
min_visitors = min(visitors)
min_week = weeks[visitors.index(min_visitors)]
plt.annotate(f'Low\n{min_visitors}', xy=(min_week, min_visitors), xytext=(min_week, min_visitors - 20),
             arrowprops=dict(facecolor='red', shrink=0.05),
             horizontalalignment='center')

# Aesthetic settings for the chart
plt.title('Weekly Visitor Trends in 2023', fontsize=16, fontweight='bold')
plt.xlabel('Week', fontsize=12)
plt.ylabel('Number of Visitors', fontsize=12)
plt.grid(True, which='major', linestyle='--', linewidth=0.5, color='grey')
plt.xticks(rotation=45)
plt.tight_layout()

# Show the chart
plt.show()