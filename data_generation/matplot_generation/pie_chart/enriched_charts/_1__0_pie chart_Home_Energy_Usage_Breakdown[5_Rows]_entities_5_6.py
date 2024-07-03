
import matplotlib.pyplot as plt

# Data
destinations = ['France', 'Spain', 'United States', 'China', 'Italy', 
                'Turkey', 'Mexico', 'Germany', 'Thailand', 'United Kingdom', 
                'Japan', 'Austria', 'Greece', 'Russia', 'Canada']
visitors = [89.4, 83.7, 79.3, 65.7, 64.5,
            51.2, 45.0, 39.6, 39.2, 37.7,
            31.2, 30.8, 30.1, 24.5, 22.1]

# Colors
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#FF8F33',
          '#8FFF33', '#33FFF0', '#FF3333', '#8C33FF', '#FFD433',
          '#33D4FF', '#8CFF33', '#FF3386', '#33FF8F', '#FF8F57']

# Pie chart
fig, ax = plt.subplots(figsize=(10, 7))  # Width, Height of the chart
ax.pie(visitors, labels=destinations, colors=colors, autopct='%1.1f%%', startangle=140)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('Top Travel Destinations by Visitor Numbers (Millions)', pad=20)
plt.show()