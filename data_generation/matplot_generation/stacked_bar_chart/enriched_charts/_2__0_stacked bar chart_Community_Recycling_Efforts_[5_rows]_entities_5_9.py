
import matplotlib.pyplot as plt
import numpy as np

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
basketball = [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310]
football = [150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260]
swimming = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210]
tennis = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105]

x = np.arange(len(months))  # the label locations
width = 0.6  # the width of the bars

fig, ax = plt.subplots(figsize=(16, 10))  # Changing width and height of the chart

# Stacked vertical bar chart
bar1 = ax.bar(x, basketball, width, label='Basketball', color='#FF5733')
bar2 = ax.bar(x, football, width, bottom=basketball, label='Football', color='#33FF57')
bar3 = ax.bar(x, swimming, width, bottom=np.add(basketball, football), label='Swimming', color='#3357FF')
bar4 = ax.bar(x, tennis, width, bottom=np.add(np.add(basketball, football), swimming), label='Tennis', color='#FFFF33')

# Add some text for labels and custom x-axis tick labels
ax.set_ylabel('Participants (Thousands)')
ax.set_title('Monthly Participation in Different Sports Activities')
ax.set_xticks(x)
ax.set_xticklabels(months)
ax.legend()

# Adding numerical labels
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, bar.get_y() + height / 2),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

add_labels(bar1)
add_labels(bar2)
add_labels(bar3)
add_labels(bar4)

plt.show()