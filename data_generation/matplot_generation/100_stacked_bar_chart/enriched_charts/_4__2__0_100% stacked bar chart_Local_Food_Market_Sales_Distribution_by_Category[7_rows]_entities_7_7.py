
import matplotlib.pyplot as plt
import numpy as np

# Data
countries = ["USA", "China", "Germany", "India", "Brazil", "Australia", "France", "Canada", "Japan", "UK"]
fruits = [20, 15, 25, 10, 10, 30, 15, 20, 15, 20]
vegetables = [25, 35, 20, 30, 20, 15, 25, 20, 25, 20]
grains = [30, 25, 15, 40, 30, 25, 20, 30, 25, 20]
dairy = [15, 10, 25, 10, 20, 15, 20, 10, 20, 20]
proteins = [10, 15, 15, 10, 20, 15, 20, 20, 15, 20]

# Stack data
data = np.array([fruits, vegetables, grains, dairy, proteins])
data_cum = data.cumsum(axis=0)

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

category_colors = ['#FF6347', '#3CB371', '#FFD700', '#1E90FF', '#FF4500']
bar_width = 0.65

for i, (colname, color) in enumerate(zip(['Fruits', 'Vegetables', 'Grains', 'Dairy', 'Proteins'], category_colors)):
    heights = data[i]
    starts = data_cum[i] - heights
    ax.bar(countries, heights, bottom=starts, width=bar_width, label=colname, color=color)

# Title and labels
ax.set_title('Dietary Composition in Various Countries (Percentage)', loc='center', fontsize=14)
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1), title='Food Categories')
ax.set_ylabel('Percentage')
ax.set_xlabel('Country')

plt.show()