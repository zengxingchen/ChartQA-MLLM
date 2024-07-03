
import matplotlib.pyplot as plt
import numpy as np

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
vegetables = [300, 320, 330, 340, 360, 370, 390, 400, 420, 430, 450, 460]
fruits = [400, 420, 430, 450, 470, 480, 500, 520, 540, 560, 580, 600]
grains = [500, 520, 530, 550, 570, 590, 610, 630, 650, 670, 690, 710]
proteins = [200, 210, 230, 250, 260, 270, 280, 290, 300, 310, 320, 330]

y = np.arange(len(months))  # the label locations
width = 0.4  # the width of the bars

fig, ax = plt.subplots(figsize=(12, 10))  # Changing width and height of the chart

# Stacked vertical bar chart
ax.bar(y, vegetables, width, label='Vegetables', color='#FF7F50')
ax.bar(y, fruits, width, bottom=vegetables, label='Fruits', color='#87CEEB')
ax.bar(y, grains, width, bottom=np.add(vegetables, fruits), label='Grains', color='#32CD32')
ax.bar(y, proteins, width, bottom=np.add(np.add(vegetables, fruits), grains), label='Proteins', color='#FFD700')

# Add some text for labels and custom y-axis tick labels
ax.set_ylabel('Consumption (Kg)')
ax.set_title('Monthly Food Consumption by Category', pad=20)
ax.set_xticks(y)
ax.set_xticklabels(months)
ax.legend(loc='upper left', bbox_to_anchor=(1,1))

plt.show()