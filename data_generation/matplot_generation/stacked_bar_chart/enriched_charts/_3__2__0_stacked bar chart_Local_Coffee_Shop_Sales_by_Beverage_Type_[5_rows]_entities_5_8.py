
import matplotlib.pyplot as plt

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021']
apples = [15000, 16000, 17000, 18000, 19000, 20000, 21000]
bananas = [8000, 8500, 9000, 9500, 10000, 10500, 11000]
oranges = [12000, 13000, 14000, 15000, 16000, 17000, 18000]

# Plot
fig, ax = plt.subplots(figsize=(10, 7))  # Change the figure size

bar_height = 0.5  # Change the bar height for a horizontal bar chart

bar_apples = ax.barh(years, apples, height=bar_height, color='#FF6347', label='Apples')
bar_bananas = ax.barh(years, bananas, height=bar_height, left=apples, color='#FFD700', label='Bananas')
bar_oranges = ax.barh(years, oranges, height=bar_height, left=[i+j for i, j in zip(apples, bananas)], color='#FF8C00', label='Oranges')

# Add some text for labels, title and custom y-axis tick labels, etc.
ax.set_xlabel('Consumption Count')
ax.set_title('Annual Fruit Consumption')
ax.set_yticks([x for x in range(len(years))])
ax.set_yticklabels(years)
ax.legend(loc='upper right')

# Adding numerical labels
for rect in bar_apples:
    width = rect.get_width()
    ax.annotate('{}'.format(width),
                xy=(width, rect.get_y() + rect.get_height() / 2),
                xytext=(3, 0),  # 3 points horizontal offset
                textcoords="offset points",
                ha='left', va='center')
for rect in bar_bananas:
    width = rect.get_width() + rect.get_x()
    ax.annotate('{}'.format(rect.get_width()),
                xy=(width, rect.get_y() + rect.get_height() / 2),
                xytext=(3, 0),
                textcoords="offset points",
                ha='left', va='center')
for rect in bar_oranges:
    width = rect.get_width() + rect.get_x()
    ax.annotate('{}'.format(rect.get_width()),
                xy=(width, rect.get_y() + rect.get_height() / 2),
                xytext=(3, 0),
                textcoords="offset points",
                ha='left', va='center')

# Show the figure
plt.show()