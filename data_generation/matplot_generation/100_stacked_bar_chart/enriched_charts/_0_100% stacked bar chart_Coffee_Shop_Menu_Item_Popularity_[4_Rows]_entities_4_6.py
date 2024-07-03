
import matplotlib.pyplot as plt
import numpy as np

# Given data table in a CSV-like string format
data = """
Day,Coffee,Tea,Soft Drink,Water
Monday,30,20,25,25
Tuesday,35,15,15,35
Wednesday,40,20,10,30
Thursday,60,10,15,15
Friday,50,12,18,20
Saturday,45,25,15,15
Sunday,55,15,10,20
"""

# Parsing data from the CSV-like string into lists
days, coffee, tea, soft_drink, water = [], [], [], [], []
for i, line in enumerate(data.strip().split('\n')):
    if i > 0:
        parts = line.split(',')
        days.append(parts[0])
        coffee.append(int(parts[1]))
        tea.append(int(parts[2]))
        soft_drink.append(int(parts[3]))
        water.append(int(parts[4]))

# Converting lists to numpy arrays
coffee = np.array(coffee)
tea = np.array(tea)
soft_drink = np.array(soft_drink)
water = np.array(water)

# Calculate the percentages
totals = coffee + tea + soft_drink + water
coffee_percentage = coffee / totals * 100
tea_percentage = tea / totals * 100
soft_drink_percentage = soft_drink / totals * 100
water_percentage = water / totals * 100

# Plotting the stacked bar chart horizontally
barWidth = 0.85
plt.figure(figsize=(14, 8))

plt.barh(days, coffee_percentage, color='#1f77b4', edgecolor='white', height=barWidth, label='Coffee')
plt.barh(days, tea_percentage, left=coffee_percentage, color='#ff7f0e', edgecolor='white', height=barWidth, label='Tea')
plt.barh(days, soft_drink_percentage, left=coffee_percentage + tea_percentage, color='#2ca02c', edgecolor='white', height=barWidth, label='Soft Drink')
plt.barh(days, water_percentage, left=coffee_percentage + tea_percentage + soft_drink_percentage, color='#d62728', edgecolor='white', height=barWidth, label='Water')

plt.xlabel('Percentage (%)', fontsize=15)
plt.ylabel('Day of the Week', fontsize=15)
plt.title('Beverage Sales Distribution Over a Week (in %)', fontsize=18)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=1)

# Display the chart
plt.tight_layout()
plt.show()