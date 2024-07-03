
import matplotlib.pyplot as plt
import numpy as np

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
technology = [500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050]
healthcare = [300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500, 520]
finance = [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310]
education = [150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260]

x = np.arange(len(months))  # the label locations
height = 0.6  # the height of the bars

fig, ax = plt.subplots(figsize=(18, 12))  # Changing width and height of the chart

# Stacked horizontal bar chart
bar1 = ax.barh(x, technology, height, label='Technology', color='#1f77b4')
bar2 = ax.barh(x, healthcare, height, left=technology, label='Healthcare', color='#ff7f0e')
bar3 = ax.barh(x, finance, height, left=np.add(technology, healthcare), label='Finance', color='#2ca02c')
bar4 = ax.barh(x, education, height, left=np.add(np.add(technology, healthcare), finance), label='Education', color='#d62728')

# Add some text for labels and custom y-axis tick labels
ax.set_xlabel('Revenue (Thousands)')
ax.set_title('Monthly Revenue from Different Business Sectors')
ax.set_yticks(x)
ax.set_yticklabels(months)
ax.legend()

# Adding numerical labels
def add_labels(bars):
    for bar in bars:
        width = bar.get_width()
        ax.annotate(f'{width}',
                    xy=(bar.get_x() + width / 2, bar.get_y() + bar.get_height() / 2),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

add_labels(bar1)
add_labels(bar2)
add_labels(bar3)
add_labels(bar4)

plt.show()