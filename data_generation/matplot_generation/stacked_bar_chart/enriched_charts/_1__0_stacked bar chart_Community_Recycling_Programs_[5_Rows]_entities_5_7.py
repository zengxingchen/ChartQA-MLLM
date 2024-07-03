
import matplotlib.pyplot as plt

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021']
apples = [14000, 16000, 19000, 22000, 25000, 29000, 32000]
oranges = [17000, 19000, 21000, 23000, 26000, 30000, 34000]
bananas = [20000, 23000, 25000, 27000, 30000, 34000, 38000]

# Bottom data for stacking
oranges_bottom = [i + j for i, j in zip(apples, oranges)]
apples_bottom = apples

# Figure and Axes
fig, ax = plt.subplots(figsize=(12, 8))  # Change width and height of the chart

# Stacked Bars
ax.bar(years, apples, color='#ff9999', edgecolor='white', width=0.5)  # Apples with pink color
ax.bar(years, oranges, bottom=apples_bottom, color='#66b3ff', edgecolor='white', width=0.5)  # Oranges with light blue color
ax.bar(years, bananas, bottom=oranges_bottom, color='#99ff99', edgecolor='white', width=0.5)  # Bananas with light green color

# Labels and Title
ax.set_ylabel('Number of Fruits Sold')
ax.set_xlabel('Year')
ax.set_title('Fruit Sales by Type from 2015 to 2021', pad=20)

# Display the plot
plt.show()