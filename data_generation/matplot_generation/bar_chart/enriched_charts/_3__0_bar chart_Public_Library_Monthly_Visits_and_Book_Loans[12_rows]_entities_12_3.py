
import matplotlib.pyplot as plt

# Data from the table above
countries = ["Japan", "Switzerland", "Singapore", "Australia", "Spain", 
             "Italy", "Iceland", "Israel", "Sweden", "France", 
             "Canada", "Norway", "Netherlands", "New Zealand", "South Korea"]
life_expectancies = [84.6, 83.4, 83.1, 82.8, 82.7, 82.5, 82.4, 82.2, 82.1, 82.0,
                     81.9, 81.8, 81.7, 81.6, 81.3]

# Setting colors for each bar
colors = ['#FF5733', '#33FF57', '#3357FF', '#57FF33', '#FF3357', 
          '#A1D6E2', '#1995AD', '#BCBABE', '#766F64', '#8BB8B8',
          '#3B9C9C', '#5D4C46', '#778C85', '#D1B499', '#A2885F']

# Increase the width and height of the chart
plt.figure(figsize=(10, 15))

# Create vertical bar chart and modify the bar width
plt.bar(countries, life_expectancies, color=colors, width=0.5)

# Customizing the chart with titles and labels
plt.ylabel('Life Expectancy (Years)')
plt.title('Life Expectancy in Various Countries')

# Display the bar chart
plt.show()