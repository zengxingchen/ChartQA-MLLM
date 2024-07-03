
import matplotlib.pyplot as plt

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
action_sales = [15000, 16000, 17000, 17500, 18000, 19000, 20000, 21000, 22000, 23000]
drama_sales = [12000, 12500, 13000, 13500, 14000, 14500, 15000, 15500, 16000, 16500]
comedy_sales = [13000, 14000, 14500, 15000, 15500, 16000, 17000, 17500, 18000, 19000]
thriller_sales = [9000, 9500, 10000, 11000, 12000, 12500, 13000, 14000, 15000, 15500]

# Plot
fig, ax = plt.subplots(figsize=(10, 14))  # Change the figure size

bar_height = 0.35  # Change the bar height for a horizontal bar chart

bar_action = ax.barh(years, action_sales, height=bar_height, color='#FF5733', label='Action')
bar_drama = ax.barh(years, drama_sales, height=bar_height, left=action_sales, color='#33FF57', label='Drama')
bar_comedy = ax.barh(years, comedy_sales, height=bar_height, left=[i+j for i,j in zip(action_sales, drama_sales)], color='#3357FF', label='Comedy')
bar_thriller = ax.barh(years, thriller_sales, height=bar_height, left=[i+j+k for i,j,k in zip(action_sales, drama_sales, comedy_sales)], color='#FF33A8', label='Thriller')

# Add some text for labels, title, and custom y-axis tick labels, etc.
ax.set_xlabel('Total Audience')
ax.set_title('Annual Movie Genre Popularity', pad=20)
ax.set_yticks(years)
ax.set_yticklabels(years)
ax.legend(loc='upper left', bbox_to_anchor=(1,1))

# Add numerical labels
for bars in [bar_action, bar_drama, bar_comedy, bar_thriller]:
    for bar in bars:
        width = bar.get_width()
        ax.annotate(f'{width}',
                    xy=(width, bar.get_y() + bar.get_height() / 2),
                    xytext=(3, 0),  # 3 points horizontal offset
                    textcoords="offset points",
                    ha='left', va='center')

# Show the figure
plt.tight_layout()
plt.show()