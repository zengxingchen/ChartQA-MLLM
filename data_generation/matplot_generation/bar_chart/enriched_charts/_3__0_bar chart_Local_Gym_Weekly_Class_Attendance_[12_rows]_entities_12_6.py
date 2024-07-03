
import matplotlib.pyplot as plt

# Data
countries = ['Japan', 'Switzerland', 'Singapore', 'Italy', 'Spain', 
             'Australia', 'Iceland', 'Israel', 'Sweden', 'France', 
             'South Korea', 'Norway', 'Luxembourg', 'Finland', 
             'Canada', 'Netherlands', 'New Zealand', 'Ireland', 
             'Belgium', 'Austria']
life_expectancy = [84.63, 84.25, 84.07, 83.52, 83.50, 
                   83.44, 83.34, 83.25, 83.21, 82.97, 
                   82.75, 82.75, 82.31, 82.28, 
                   82.24, 82.15, 82.05, 82.00, 
                   81.83, 81.74]

# Create bar chart
plt.figure(figsize=(12, 10))  # Change width and height of the chart
colors = ['#003f5c', '#2f4b7c', '#665191', '#a05195', '#d45087', 
          '#f95d6a', '#ff7c43', '#ffa600', '#58508d', '#bc5090', 
          '#ff6361', '#003f5c', '#665191', '#f95d6a', 
          '#2f4b7c', '#ff7c43', '#a05195', '#bc5090', 
          '#d45087', '#ffa600']

plt.bar(countries, life_expectancy, color=colors, width=0.6)  # Change direction of chart and bar width

# Customizing the plot
plt.ylabel('Life Expectancy in Years')
plt.title('Life Expectancy by Country (2020)')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()