
import matplotlib.pyplot as plt

# Data
destinations = ['Paris', 'Bangkok', 'London', 'Dubai', 'Singapore', 'New York',
                'Istanbul', 'Kuala Lumpur', 'Tokyo', 'Rome', 'Barcelona', 
                'Los Angeles', 'Hong Kong', 'Amsterdam', 'Madrid']
visitors = [19.1, 22.8, 21.7, 16.5, 14.7, 13.5, 15.2, 13.8, 12.1, 10.6, 11.4, 9.5, 8.9, 8.7, 7.8]

# Color scheme using color codes
colors = ['#FF6347', '#FFD700', '#8A2BE2', '#00CED1', '#1E90FF', '#32CD32',
          '#FF1493', '#7FFF00', '#FF69B4', '#87CEEB', '#FF4500', '#8B0000',
          '#40E0D0', '#BA55D3', '#4682B4']

# Create vertical bar chart
plt.figure(figsize=(14, 8))
bars = plt.bar(destinations, visitors, color=colors, width=0.6)

# Adjusting the height and width of bars
for bar in bars:
    bar.set_width(0.5)

# Changing the layout and labels
plt.ylabel('Visitors (millions)', fontsize=12)
plt.title('Top Destinations Visited in 2023', fontsize=16)
plt.ylim(0, max(visitors) * 1.1)  # Set y-axis limit higher to accommodate labels

# Adding value labels on top of each bar
for i, v in enumerate(visitors):
    plt.text(i, v + 0.5, str(v), color='black', ha='center', fontsize=11)

# Show the final result
plt.tight_layout()
plt.show()