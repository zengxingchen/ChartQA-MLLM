
import matplotlib.pyplot as plt

# Data
countries = ['United States', 'China', 'Japan', 'Germany', 'India',
             'United Kingdom', 'France', 'Italy', 'Brazil', 'Canada',
             'Russia', 'South Korea', 'Spain', 'Australia', 'Mexico']
gdp = [21.43, 14.34, 5.08, 3.84, 2.87,
       2.83, 2.72, 2.00, 1.84, 1.74,
       1.70, 1.63, 1.40, 1.38, 1.27]

# Create bar chart
plt.figure(figsize=(10, 8))  # Change width and height of the chart
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
          '#1a55FF', '#2a5f0e', '#6a5230', '#4b6728', '#b967cd']

plt.barh(countries, gdp, color=colors, height=0.5)  # Change direction of chart and bar height

# Customizing the plot
plt.xlabel('GDP in Trillion USD')
plt.title('GDP by country in trillions of USD (2020)')
plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()