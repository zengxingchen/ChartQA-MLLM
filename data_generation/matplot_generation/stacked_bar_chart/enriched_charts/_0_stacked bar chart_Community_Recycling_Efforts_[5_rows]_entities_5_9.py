
import matplotlib.pyplot as plt
import numpy as np

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
electronics = [500, 520, 530, 550, 580, 600, 630, 640, 650, 660, 680, 700]
clothing = [400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 520]
home_goods = [300, 310, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420]
books = [200, 210, 230, 250, 260, 270, 280, 290, 300, 310, 320, 330]

y = np.arange(len(months))  # the label locations
height = 0.35  # the height of the bars

fig, ax = plt.subplots(figsize=(14, 8))  # Changing width and height of the chart

# Stacked horizontal bar chart
ax.barh(y - height/2, electronics, height, label='Electronics', color='#FF5733')
ax.barh(y - height/2, clothing, height, left=electronics, label='Clothing', color='#33FF57')
ax.barh(y - height/2, home_goods, height, left=np.add(electronics, clothing), label='Home Goods', color='#3357FF')
ax.barh(y - height/2, books, height, left=np.add(np.add(electronics, clothing), home_goods), label='Books', color='#FFFF33')

# Add some text for labels and custom x-axis tick labels
ax.set_xlabel('Revenue (Thousands)')
ax.set_title('Monthly Sales Revenue by Product Category')
ax.set_yticks(y)
ax.set_yticklabels(months)
ax.invert_yaxis()  # labels read top-to-bottom
ax.legend()

plt.show()