
import matplotlib.pyplot as plt

# Data from the table above
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 
          'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose', 
          'Austin', 'Jacksonville', 'Fort Worth', 'Columbus', 'Charlotte']
temperatures = [24, 20, 22, 28, 33, 25, 29, 21, 30, 23, 31, 27, 29, 23, 26]

# Setting colors for each bar
colors = ['#FF5733', '#33FF57', '#3357FF', '#57FF33', '#FF3357', 
          '#A1D6E2', '#1995AD', '#BCBABE', '#766F64', '#8BB8B8',
          '#3B9C9C', '#5D4C46', '#778C85', '#D1B499', '#A2885F']

# Increase the width and height of the chart
plt.figure(figsize=(12, 8))

# Change the direction of the chart to horizontal and modify the bar height
plt.barh(cities, temperatures, color=colors, height=0.6)

# Customizing the chart with titles and labels
plt.xlabel('Average Temperature (°C)')
plt.title('Average Temperatures in June Across Various U.S. Cities')
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

# Display the bar chart
plt.show()