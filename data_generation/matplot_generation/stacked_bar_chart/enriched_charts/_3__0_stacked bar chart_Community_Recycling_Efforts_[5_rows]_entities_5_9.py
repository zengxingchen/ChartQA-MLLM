
import matplotlib.pyplot as plt
import numpy as np

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
pop = [300, 320, 330, 350, 380, 400, 430, 440, 450, 470, 490, 510]
rock = [450, 480, 500, 530, 560, 590, 620, 650, 680, 710, 740, 770]
jazz = [200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420]
classical = [150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260]

y = np.arange(len(months))  # the label locations
width = 0.45  # the width of the bars

fig, ax = plt.subplots(figsize=(12, 10))  # Changing width and height of the chart

# Stacked vertical bar chart
ax.bar(y - width/2, pop, width, label='Pop', color='#FF5733')
ax.bar(y - width/2, rock, width, bottom=pop, label='Rock', color='#33FF57')
ax.bar(y - width/2, jazz, width, bottom=np.add(pop, rock), label='Jazz', color='#3357FF')
ax.bar(y - width/2, classical, width, bottom=np.add(np.add(pop, rock), jazz), label='Classical', color='#FFFF33')

# Add some text for labels and custom y-axis tick labels
ax.set_ylabel('Ticket Sales (Thousands)')
ax.set_title('Monthly Music Concert Ticket Sales by Genre')
ax.set_xticks(y)
ax.set_xticklabels(months)
ax.legend(loc='upper left')

# Numerical labels for each bar
for i in range(len(months)):
    ax.text(i - width/2, pop[i] / 2, str(pop[i]), ha='center', va='bottom', color='black')
    ax.text(i - width/2, pop[i] + rock[i] / 2, str(rock[i]), ha='center', va='bottom', color='black')
    ax.text(i - width/2, pop[i] + rock[i] + jazz[i] / 2, str(jazz[i]), ha='center', va='bottom', color='black')
    ax.text(i - width/2, pop[i] + rock[i] + jazz[i] + classical[i] / 2, str(classical[i]), ha='center', va='bottom', color='black')

plt.show()