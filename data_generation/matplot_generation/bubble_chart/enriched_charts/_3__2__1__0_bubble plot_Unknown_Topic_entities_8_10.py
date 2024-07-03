
import matplotlib.pyplot as plt

# Data for plotting
destinations = ['Modern Art Museum', 'Art Workshop', 'Street Art Tour', 'Photography Exhibit', 'Art Fair', 'Gallery Hopping', 'Sculpture Garden', 'Cultural Exhibition', 'Film Festival', 'Theatre Performance']
visitor_counts = [60, 25, 40, 55, 30, 45, 35, 50, 20, 22]
average_expenses = [1350, 700, 300, 1200, 500, 1000, 800, 1100, 2000, 1600]
satisfaction_ratings = [9.2, 8.7, 8.5, 9.1, 8.8, 8.6, 9.0, 8.9, 8.2, 8.4]

# Create a figure with specified width and height
fig, ax = plt.subplots(figsize=(14, 10))

# Bubble sizes (scaled)
sizes = [visitors * 10 for visitors in visitor_counts]

# Bubble colors with specific hex color codes
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFC1', '#FF8F33', '#A133FF', '#FFC133', '#33FFF5', '#F533FF']

# Plot each data point
for (destination, visitors, expense, rating, size, color) in zip(destinations, visitor_counts, average_expenses, satisfaction_ratings, sizes, colors):
    ax.scatter(visitors, expense, s=size, label=destination, alpha=0.6, edgecolors='w', color=color)

# Titles and labels
plt.title('Popular Art Destinations by Visitor Count, Expense, and Satisfaction', pad=20)
plt.xlabel('Visitor Count (thousands)')
plt.ylabel('Average Cost (USD)')

# Legend
handles, labels = ax.get_legend_handles_labels()
hl = sorted(zip(handles, labels), key=lambda x: x[1])
handles2, labels2 = zip(*hl)
ax.legend(handles2, labels2, loc="upper left", title="Destinations")

# Show plot
plt.show()