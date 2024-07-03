
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Region 1', 'Region 2', 'Region 3', 'Region 4', 'Region 5', 'Region 6', 'Region 7', 'Region 8', 'Region 9', 'Region 10']
fresh_produce = [220, 210, 200, 230, 240, 250, 260, 270, 280, 290]
dairy = [180, 190, 170, 200, 210, 220, 230, 240, 250, 260]
snacks = [150, 160, 140, 170, 180, 190, 200, 210, 220, 230]
beverages = [120, 130, 110, 140, 150, 160, 170, 180, 190, 200]

bar_height = 0.6  # Change the bar height
fig, ax = plt.subplots(figsize=(12, 8))  # Change the figure size

# Location of bars on y-axis
ind = np.arange(len(categories))

# Stacked bar chart (horizontal)
plt.barh(ind, fresh_produce, height=bar_height, color='#FF4500')
plt.barh(ind, dairy, height=bar_height, left=fresh_produce, color='#1E90FF')
plt.barh(ind, snacks, height=bar_height, left=np.add(fresh_produce, dairy), color='#32CD32')
plt.barh(ind, beverages, height=bar_height, left=np.add(fresh_produce, np.add(dairy, snacks)), color='#FFD700')

# Labels and Titles
ax.set_xlabel('Revenue (in millions)')
ax.set_title('Regional Sales Distribution of Grocery Categories', pad=20)
ax.set_yticks(ind)
ax.set_yticklabels(categories)
ax.set_ylabel('Region')

# Numerical Labels
for i in range(len(categories)):
    plt.text(fresh_produce[i] / 2, i, str(fresh_produce[i]), va='center', ha='center', color='white', fontweight='bold')
    plt.text(fresh_produce[i] + dairy[i] / 2, i, str(dairy[i]), va='center', ha='center', color='white', fontweight='bold')
    plt.text(fresh_produce[i] + dairy[i] + snacks[i] / 2, i, str(snacks[i]), va='center', ha='center', color='white', fontweight='bold')
    plt.text(fresh_produce[i] + dairy[i] + snacks[i] + beverages[i] / 2, i, str(beverages[i]), va='center', ha='center', color='white', fontweight='bold')

# Legend
plt.legend(['Fresh Produce', 'Dairy', 'Snacks', 'Beverages'], loc='upper right')

# Display the chart
plt.show()