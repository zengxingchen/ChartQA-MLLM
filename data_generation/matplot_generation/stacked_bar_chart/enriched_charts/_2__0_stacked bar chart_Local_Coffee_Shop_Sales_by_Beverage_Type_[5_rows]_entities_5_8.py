
import matplotlib.pyplot as plt

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021']
beach_visitors = [18000, 19000, 21000, 23000, 25000, 27000, 29000]
mountain_visitors = [12000, 13000, 14000, 15000, 16000, 17000, 18000]
city_visitors = [7000, 8000, 9000, 10000, 11000, 12000, 13000]

# Plot
fig, ax = plt.subplots(figsize=(12, 9))  # Change the figure size

bar_width = 0.6  # Change the bar width for a vertical bar chart

bar_beach = ax.bar(years, beach_visitors, width=bar_width, color='#FF5733', label='Beach')
bar_mountain = ax.bar(years, mountain_visitors, width=bar_width, bottom=beach_visitors, color='#33FF57', label='Mountain')
bar_city = ax.bar(years, city_visitors, width=bar_width, bottom=[i+j for i,j in zip(beach_visitors, mountain_visitors)], color='#3357FF', label='City')

# Add some text for labels, title and custom y-axis tick labels, etc.
ax.set_ylabel('Visitor Count')
ax.set_title('Annual Visitor Counts to Tourist Attractions')
ax.set_xticks([x for x in range(len(years))])
ax.set_xticklabels(years)
ax.legend()

# Adding numerical labels
for rect in bar_beach:
    height = rect.get_height()
    ax.annotate('{}'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
for rect in bar_mountain:
    height = rect.get_height() + rect.get_y()
    ax.annotate('{}'.format(rect.get_height()),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom')
for rect in bar_city:
    height = rect.get_height() + rect.get_y()
    ax.annotate('{}'.format(rect.get_height()),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom')

# Show the figure
plt.show()