
import matplotlib.pyplot as plt

# Data
countries = [
    'Bangladesh', 'Pakistan', 'India', 'Mongolia', 'Afghanistan', 
    'Indonesia', 'Vietnam', 'Thailand', 'China', 'Nepal', 
    'Sri Lanka', 'Myanmar', 'Iran', 'Philippines', 'Egypt', 
    'Uzbekistan', 'Kazakhstan', 'Turkey', 'South Korea', 'Russia'
]
pollution_levels = [
    83.0, 70.0, 51.9, 48.5, 46.7, 
    44.0, 34.1, 24.5, 23.6, 23.4, 
    22.8, 22.0, 20.5, 20.3, 19.8, 
    18.9, 18.3, 16.9, 16.5, 16.2
]
colors = [
    '#ff6666', '#ffcc99', '#99cc99', '#66b2ff', '#ff66b2',
    '#b266ff', '#ccff66', '#66ffcc', '#ff9966', '#ff6699',
    '#6699ff', '#99ff66', '#ffcc66', '#66ff99', '#cc66ff',
    '#ff9966', '#ff66b2', '#66b2ff', '#99cc99', '#ffcc99'
]

# Figure size
plt.figure(figsize=(12, 6))

# Vertical bar chart
plt.bar(countries, pollution_levels, color=colors, width=0.6)

# Labeling
plt.ylabel('Pollution Level (PM2.5, µg/m³)')
plt.title('Top 20 Countries by Air Pollution Levels in 2024')

# Rotate x-axis labels for readability
plt.xticks(rotation=90)

# Adjust layout to ensure title and labels fit
plt.tight_layout()

# Show plot
plt.show()