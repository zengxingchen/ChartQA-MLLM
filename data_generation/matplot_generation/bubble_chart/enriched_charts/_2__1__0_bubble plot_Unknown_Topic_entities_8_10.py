
import matplotlib.pyplot as plt

# Data for plotting
destinations = ['Yoga Retreat', 'Spa Resort', 'Meditation Center', 'Nature Trail', 'Mountain Hiking', 'Beach Resort', 'City Tour', 'Historical Sites', 'Adventure Park', 'Cultural Festival']
visitor_counts = [40, 30, 25, 45, 35, 50, 55, 20, 22, 28]
average_expenses = [1500, 1400, 1000, 800, 950, 1300, 1200, 1100, 1250, 900]
satisfaction_ratings = [9.1, 8.7, 8.5, 8.2, 8.8, 9.0, 8.9, 8.3, 8.4, 8.6]

# Create a figure with specified width and height
fig, ax = plt.subplots(figsize=(16, 12))

# Bubble sizes (scaled)
sizes = [visitors * 10 for visitors in visitor_counts]

# Bubble colors with specific hex color codes
colors = ['#4CAF50', '#FFC107', '#2196F3', '#FF5722', '#9C27B0', '#03A9F4', '#FF9800', '#8BC34A', '#E91E63', '#CDDC39']

# Plot each data point
for (destination, visitors, expense, rating, size, color) in zip(destinations, visitor_counts, average_expenses, satisfaction_ratings, sizes, colors):
    ax.scatter(visitors, expense, s=size, label=destination, alpha=0.6, edgecolors='w', color=color)

# Titles and labels
plt.title('Top Wellness Destinations by Visitor Count, Expense, and Satisfaction', pad=20)
plt.xlabel('Visitor Count (millions)')
plt.ylabel('Average Expense (USD)')

# Legend
handles, labels = ax.get_legend_handles_labels()
hl = sorted(zip(handles, labels), key=lambda x: x[1])
handles2, labels2 = zip(*hl)
ax.legend(handles2, labels2, loc="upper right", title="Destinations")

# Show plot
plt.show()