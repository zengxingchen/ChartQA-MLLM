
import matplotlib.pyplot as plt

# Data
countries = ['France', 'Spain', 'USA', 'China', 'Italy',
             'Turkey', 'Mexico', 'Germany', 'Thailand', 'UK',
             'Japan', 'Australia', 'Canada', 'Russia', 'South Korea']
tourists = [89.4, 83.7, 79.3, 65.7, 64.5,
            51.2, 45.0, 39.6, 38.2, 36.3,
            31.9, 28.5, 25.1, 24.4, 23.3]

# Create bar chart
plt.figure(figsize=(14, 8))  # Change width and height of the chart
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
          '#aec7e8', '#ffbb78', '#98df8a', '#ff9896', '#c5b0d5']

plt.barh(countries, tourists, color=colors, height=0.5)  # Horizontal bar chart with changed bar height

# Customizing the plot
plt.xlabel('Annual Tourists (in millions)')
plt.title('Top Tourist Destinations by Annual Visitors (2023)', pad=30)
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.xlim(20, 100)  # Set y-axis limits to truncate

plt.tight_layout()
plt.show()