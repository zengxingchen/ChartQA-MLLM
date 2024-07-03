
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Q1', 'Q2', 'Q3', 'Q4']
fruits = [30, 35, 25, 20]
vegetables = [40, 30, 35, 25]
grains = [20, 25, 30, 40]
proteins = [10, 10, 10, 15]

# Normalize the data
total = np.array(fruits) + np.array(vegetables) + np.array(grains) + np.array(proteins)
fruits_percentage = np.array(fruits) / total * 100
vegetables_percentage = np.array(vegetables) / total * 100
grains_percentage = np.array(grains) / total * 100
proteins_percentage = np.array(proteins) / total * 100

# Plotting
barWidth = 0.6
fig, ax = plt.subplots(figsize=(12, 8))

bar1 = np.add(fruits_percentage, vegetables_percentage).tolist()
bar2 = np.add(bar1, grains_percentage).tolist()

# Create bars
plt.bar(categories, fruits_percentage, color='#FF9999', edgecolor='grey', width=barWidth)
plt.bar(categories, vegetables_percentage, bottom=fruits_percentage, color='#66B2FF', edgecolor='grey', width=barWidth)
plt.bar(categories, grains_percentage, bottom=bar1, color='#99FF99', edgecolor='grey', width=barWidth)
plt.bar(categories, proteins_percentage, bottom=bar2, color='#FFCC99', edgecolor='grey', width=barWidth)

# Add title and labels
plt.ylabel('Percentage')
plt.title('Quarterly Food Consumption Distribution by Category', pad=20)
plt.legend(['Fruits', 'Vegetables', 'Grains', 'Proteins'], loc='upper right')

plt.show()