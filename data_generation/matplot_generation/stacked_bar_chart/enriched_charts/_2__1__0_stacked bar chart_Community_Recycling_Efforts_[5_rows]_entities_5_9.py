
import matplotlib.pyplot as plt
import numpy as np

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
smartphones = [1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750]
laptops = [800, 850, 870, 900, 950, 980, 1020, 1050, 1100, 1150, 1200, 1250]
tablets = [400, 420, 430, 450, 470, 490, 510, 530, 550, 570, 590, 610]
accessories = [300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410]

y = np.arange(len(months))  # the label locations
height = 0.4  # the height of the bars

fig, ax = plt.subplots(figsize=(14, 8))  # Changing width and height of the chart

# Stacked horizontal bar chart
ax.barh(y, smartphones, height, label='Smartphones', color='#1f77b4')
ax.barh(y, laptops, height, left=smartphones, label='Laptops', color='#ff7f0e')
ax.barh(y, tablets, height, left=np.add(smartphones, laptops), label='Tablets', color='#2ca02c')
ax.barh(y, accessories, height, left=np.add(np.add(smartphones, laptops), tablets), label='Accessories', color='#d62728')

# Add some text for labels and custom y-axis tick labels
ax.set_xlabel('Sales (Units)')
ax.set_title('Monthly Sales of Electronic Products', pad=20)
ax.set_yticks(y)
ax.set_yticklabels(months)
ax.legend(loc='upper right', bbox_to_anchor=(1.25, 1))

# Assign numerical label of each bar
for i in range(len(months)):
    plt.text(smartphones[i]/2, i, str(smartphones[i]), ha='center', va='center', color='white')
    plt.text(smartphones[i] + laptops[i]/2, i, str(laptops[i]), ha='center', va='center', color='white')
    plt.text(smartphones[i] + laptops[i] + tablets[i]/2, i, str(tablets[i]), ha='center', va='center', color='white')
    plt.text(smartphones[i] + laptops[i] + tablets[i] + accessories[i]/2, i, str(accessories[i]), ha='center', va='center', color='white')

plt.show()