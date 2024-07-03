
import matplotlib.pyplot as plt

# Data for the bar chart
countries = [
    'Canada', 'Russia', 'Germany', 'United Kingdom', 'France', 'Spain', 
    'Italy', 'Greece', 'Turkey', 'Australia', 'Brazil', 'India', 
    'China', 'Japan', 'South Korea', 'Mexico', 'South Africa', 
    'Argentina', 'Nigeria', 'Egypt'
]

average_life_expectancy = [
    82.3, 72.6, 81.1, 81.2, 82.7, 83.4, 83.3, 82.1, 78.5, 82.9, 76.3, 69.4, 
    76.9, 84.6, 83.0, 75.4, 63.5, 76.5, 54.3, 71.7
]

# Modify the color scheme
colors = [
    '#FF6347', '#4682B4', '#8A2BE2', '#DEB887', '#5F9EA0', '#7FFF00', 
    '#D2691E', '#FF7F50', '#6495ED', '#DC143C', '#00FFFF', '#00008B', 
    '#B8860B', '#A9A9A9', '#006400', '#8B008B', '#FF8C00', '#8B0000', 
    '#2F4F4F', '#00CED1'
]

# Set the figure size for better clarity or visual appeal
plt.figure(figsize=(14, 8))

# Change the direction of the chart from horizontal to vertical and adjust the width
plt.barh(countries, average_life_expectancy, color=colors, height=0.6)

# Add labels and title to the chart
plt.xlabel('Average Life Expectancy (Years)')
plt.title('Average Life Expectancy by Country', pad=20)

# Set the y-axis limits
plt.xlim(50, 90)

# Display the chart
plt.show()