
import matplotlib.pyplot as plt

# Data
fruits = ['Bananas', 'Apples', 'Oranges', 'Grapes', 'Strawberries', 
          'Watermelons', 'Pineapples', 'Mangoes', 'Blueberries', 'Peaches', 
          'Kiwis', 'Cherries', 'Pears', 'Plums', 'Papayas']
consumption = [12.4, 10.2, 8.6, 5.4, 4.2,
               3.8, 3.5, 2.9, 2.4, 2.1,
               1.9, 1.7, 1.5, 1.2, 1.0]

# Colors
colors = ['#FF6347', '#FFA07A', '#FFD700', '#ADFF2F', '#7FFF00',
          '#32CD32', '#20B2AA', '#00CED1', '#1E90FF', '#4169E1',
          '#8A2BE2', '#9932CC', '#DA70D6', '#FF1493', '#FF69B4']

# Pie chart
fig, ax = plt.subplots(figsize=(10, 7))  # Width, Height of the chart
ax.pie(consumption, labels=fruits, colors=colors, autopct='%1.1f%%', startangle=140)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('Average Fruit Consumption per Person per Year (kg)', pad=20)
plt.show()