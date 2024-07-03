
import matplotlib.pyplot as plt

# Provided data
data = [
    {'Week': '2023-W09', 'Visitors': 150},
    {'Week': '2023-W10', 'Visitors': 200},
    {'Week': '2023-W11', 'Visitors': 180},
    {'Week': '2023-W12', 'Visitors': 220},
    {'Week': '2023-W13', 'Visitors': 210},
    {'Week': '2023-W14', 'Visitors': 300},
    {'Week': '2023-W15', 'Visitors': 250}
]

# Extracting weeks and visitor counts
weeks = [entry['Week'] for entry in data]
visitors = [entry['Visitors'] for entry in data]

# Creating the line chart
plt.figure(figsize=(10, 5))
line, = plt.plot(weeks, visitors, color='navy', linestyle='-', linewidth=2, marker='o', markerfacecolor='red', markeredgewidth=2, markersize=8)

# Highlighting the highest visitor count
max_visitors = max(visitors)
max_week = weeks[visitors.index(max_visitors)]
plt.annotate(f'Peak\n{max_visitors}', xy=(max_week, max_visitors), xytext=(max_week, max_visitors + 15),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='center')

# Aesthetic settings for the chart
plt.title('Weekly Visitors for 2023 Weeks 09 to 15', fontsize=14, fontweight='bold')
plt.xlabel('Week', fontsize=12)
plt.ylabel('Number of Visitors', fontsize=12)
plt.grid(True, which='major', linestyle='--', linewidth=0.5, color='grey')
plt.xticks(rotation=45)
plt.tight_layout()

# Show the chart
plt.show()