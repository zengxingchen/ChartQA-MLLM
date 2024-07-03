
import matplotlib.pyplot as plt

# Data for the chart
fruits = ['Apples', 'Oranges', 'Bananas', 'Grapes', 'Strawberries', 
          'Blueberries', 'Peaches', 'Mangoes', 'Pineapples', 'Kiwis', 
          'Cherries', 'Pomegranates', 'Watermelons', 'Papayas', 'Plums']
consumption = [50, 35, 45, 30, 25, 20, 15, 40, 32, 18, 22, 28, 27, 19, 26]

# Setting colors for each bar
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#FFBF00', '#92A8D1', 
          '#955251', '#B565A7', '#009B77', '#DD4124', '#D65076',
          '#45B8AC', '#EFC050', '#5B5EA6', '#9B2335', '#E15D44']

# Increase the width and height of the chart
plt.figure(figsize=(10, 12))

# Change the direction of the chart to vertical and modify the bar width
plt.bar(fruits, consumption, color=colors, width=0.7)

# Customizing the chart with titles and labels
plt.ylabel('Fruit Consumption (kg per person per year)')
plt.title('Annual Fruit Consumption in Various Countries')
plt.grid(color='gray', linestyle='--', linewidth=0.5)

# Display the bar chart
plt.show()