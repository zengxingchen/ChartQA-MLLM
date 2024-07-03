
import matplotlib.pyplot as plt

# Data for plotting
destinations = ['France', 'Spain', 'USA', 'China', 'Italy', 'Turkey', 'Mexico', 'Germany', 'Thailand', 'UK']
visitor_counts = [89, 83, 79, 65, 62, 51, 45, 39, 38, 37]
average_expenses = [1200, 1150, 1350, 900, 1100, 800, 850, 1050, 700, 1300]
satisfaction_ratings = [8.5, 8.3, 8.2, 7.8, 8.0, 7.5, 7.9, 8.1, 7.7, 8.4]

# Create a figure with specified width and height
fig, ax = plt.subplots(figsize=(14, 10))

# Bubble sizes (scaled)
sizes = [visitors * 10 for visitors in visitor_counts]

# Bubble colors with specific hex color codes
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#A633FF', '#FF8833', '#33FFD5', '#FFD733', '#FF5733', '#33FF57']

# Plot each data point
for (destination, visitors, expense, rating, size, color) in zip(destinations, visitor_counts, average_expenses, satisfaction_ratings, sizes, colors):
    ax.scatter(visitors, expense, s=size, label=destination, alpha=0.6, edgecolors='w', color=color)

# Titles and labels
plt.title('Top Travel Destinations by Visitor Count, Expense, and Satisfaction')
plt.xlabel('Visitor Count (millions)')
plt.ylabel('Average Expense (USD)')

# Legend
handles, labels = ax.get_legend_handles_labels()
hl = sorted(zip(handles, labels), key=lambda x: x[1])
handles2, labels2 = zip(*hl)
ax.legend(handles2, labels2, loc="upper left", title="Destinations")

# Show plot
plt.show()