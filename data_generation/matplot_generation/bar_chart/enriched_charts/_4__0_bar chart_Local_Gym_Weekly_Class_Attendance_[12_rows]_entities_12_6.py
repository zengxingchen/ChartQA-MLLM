
import matplotlib.pyplot as plt

# Data
countries = ['United States', 'China', 'Japan', 'Germany', 'India',
             'United Kingdom', 'France', 'Italy', 'Brazil', 'Canada',
             'Russia', 'South Korea', 'Spain', 'Australia', 'Mexico']
life_expectancy = [78.5, 76.7, 84.5, 81.2, 69.7,
                   81.3, 82.4, 83.2, 75.7, 82.3,
                   72.6, 83.3, 83.4, 82.9, 75.0]

# Create bar chart
plt.figure(figsize=(12, 6))  # Change width and height of the chart
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FF8C33',
          '#8C33FF', '#FF3380', '#33FFC5', '#FF5733', '#33D4FF',
          '#33FF57', '#FF33E8', '#E833FF', '#FFBD33', '#33FF90']

plt.bar(countries, life_expectancy, color=colors, width=0.6)  # Change direction of chart and bar width

# Customizing the plot
plt.ylabel('Life Expectancy in Years')
plt.title('Life Expectancy by Country (2020)')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Set y-axis limits to start from 65 to truncate the lower part
plt.ylim(65, 85)

plt.tight_layout()
plt.show()