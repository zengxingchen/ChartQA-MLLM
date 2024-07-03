
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Region 1', 'Region 2', 'Region 3', 'Region 4', 'Region 5', 'Region 6', 'Region 7', 'Region 8']
science_fiction = [220, 180, 230, 195, 215, 210, 225, 235]
fantasy = [140, 155, 165, 160, 175, 180, 170, 190]
mystery = [110, 120, 115, 125, 130, 140, 135, 145]
romance = [60, 75, 85, 70, 80, 95, 100, 105]

bar_height = 0.4
fig, ax = plt.subplots(figsize=(12, 8))

# Location of bars on y-axis
ind = np.arange(len(categories))

# Stacked bar chart
plt.barh(ind, science_fiction, height=bar_height, color='#4B0082')
plt.barh(ind, fantasy, height=bar_height, left=science_fiction, color='#8A2BE2')
plt.barh(ind, mystery, height=bar_height, left=np.add(science_fiction, fantasy), color='#00CED1')
plt.barh(ind, romance, height=bar_height, left=np.add(science_fiction, np.add(fantasy, mystery)), color='#FFD700')

# Labels and Titles
ax.set_xlabel('Book Sales (in thousands)')
ax.set_title('Regional Book Sales Distribution by Genre', pad=20)
ax.set_yticks(ind)
ax.set_yticklabels(categories)
ax.set_ylabel('Region')

# Legend
plt.legend(['Science Fiction', 'Fantasy', 'Mystery', 'Romance'], loc='lower right')

# Adding numerical labels
for i in range(len(categories)):
    plt.text(science_fiction[i] / 2, i, str(science_fiction[i]), ha='center', va='center', color='white')
    plt.text(science_fiction[i] + fantasy[i] / 2, i, str(fantasy[i]), ha='center', va='center', color='white')
    plt.text(science_fiction[i] + fantasy[i] + mystery[i] / 2, i, str(mystery[i]), ha='center', va='center', color='white')
    plt.text(science_fiction[i] + fantasy[i] + mystery[i] + romance[i] / 2, i, str(romance[i]), ha='center', va='center', color='black')

# Display the chart
plt.show()