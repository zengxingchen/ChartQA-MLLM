
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
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'
]

# Figure size
plt.figure(figsize=(10, 14))

# Horizontal bar chart
plt.barh(countries, pollution_levels, color=colors, height=0.5)

# Labeling
plt.xlabel('Pollution Level (PM2.5, µg/m³)')
plt.title('Top 20 Countries by Air Pollution Levels in 2024')

# Set y-axis limit to truncate the chart
plt.xlim(15, 85)

# Adjust layout to ensure title and labels fit
plt.tight_layout()

# Show plot
plt.show()