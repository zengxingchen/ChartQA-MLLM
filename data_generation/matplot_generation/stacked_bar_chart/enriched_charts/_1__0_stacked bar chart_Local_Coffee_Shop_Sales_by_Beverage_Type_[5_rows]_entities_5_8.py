
import matplotlib.pyplot as plt

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
football_sales = [20000, 22000, 25000, 27000, 30000, 32000, 35000, 38000, 40000, 42000]
basketball_sales = [15000, 17000, 19000, 21000, 23000, 25000, 27000, 29000, 31000, 33000]
baseball_sales = [10000, 12000, 14000, 16000, 18000, 20000, 22000, 24000, 26000, 28000]

# Plot
fig, ax = plt.subplots(figsize=(12, 10))  # Change the figure size

bar_width = 0.4  # Change the bar width for a vertical bar chart

bar_football = ax.bar(years, football_sales, width=bar_width, color='#4CAF50', label='Football')
bar_basketball = ax.bar(years, basketball_sales, width=bar_width, bottom=football_sales, color='#2196F3', label='Basketball')
bar_baseball = ax.bar(years, baseball_sales, width=bar_width, bottom=[i+j for i,j in zip(football_sales, basketball_sales)], color='#FFC107', label='Baseball')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Total Participants')
ax.set_title('Annual Sports Participation by Type')
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)
ax.legend(loc='upper left', bbox_to_anchor=(1,1))

# Show the figure
plt.tight_layout()
plt.show()