
import matplotlib.pyplot as plt

# Data
countries = ['United States', 'China', 'Japan', 'Germany', 'India',
             'United Kingdom', 'France', 'Italy', 'Brazil', 'Canada',
             'Russia', 'South Korea', 'Spain', 'Australia', 'Mexico',
             'Indonesia', 'Netherlands', 'Saudi Arabia', 'Turkey', 'Switzerland']
gdp = [21.43, 14.34, 5.08, 3.86, 2.87,
       2.83, 2.72, 2.00, 1.84, 1.74,
       1.70, 1.63, 1.40, 1.39, 1.27,
       1.12, 0.91, 0.79, 0.76, 0.70]

# Create horizontal bar chart
plt.figure(figsize=(14, 8))  # Change width and height of the chart
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
          '#aec7e8', '#ffbb78', '#98df8a', '#ff9896', '#c5b0d5',
          '#c49c94', '#f7b6d2', '#c7c7c7', '#dbdb8d', '#9edae5']

plt.barh(countries, gdp, color=colors, height=0.6)  # Change direction of chart and bar width

# Customizing the plot
plt.xlabel('GDP (in trillions USD)')
plt.title('Top 20 Countries by GDP in 2020', pad=20)
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.xlim(0.5, 22)  # Set y-axis limits to truncate the chart

plt.tight_layout()
plt.show()