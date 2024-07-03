
import matplotlib.pyplot as plt

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
fiction_sales = [15000, 17000, 18000, 20000, 22000, 24000, 26000, 28000, 30000, 32000]
non_fiction_sales = [12000, 14000, 16000, 18000, 20000, 22000, 24000, 26000, 28000, 30000]
sci_fi_sales = [8000, 9000, 11000, 13000, 15000, 17000, 19000, 21000, 23000, 25000]

# Plot
fig, ax = plt.subplots(figsize=(14, 8))  # Change the figure size

bar_height = 0.4  # Change the bar height for a horizontal bar chart

bar_fiction = ax.barh(years, fiction_sales, height=bar_height, color='#FF5733', label='Fiction')
bar_non_fiction = ax.barh(years, non_fiction_sales, height=bar_height, left=fiction_sales, color='#33FFCE', label='Non-Fiction')
bar_sci_fi = ax.barh(years, sci_fi_sales, height=bar_height, left=[i+j for i,j in zip(fiction_sales, non_fiction_sales)], color='#3375FF', label='Sci-Fi')

# Add some text for labels, title, and custom y-axis tick labels, etc.
ax.set_xlabel('Total Books Sold')
ax.set_title('Annual Book Sales by Genre')
ax.set_yticks(range(len(years)))
ax.set_yticklabels(years)
ax.legend(loc='upper left', bbox_to_anchor=(1,1))

# Add numerical labels to each bar segment
for i in range(len(years)):
    ax.text(fiction_sales[i] / 2, i, str(fiction_sales[i]), va='center', ha='center', color='white', fontweight='bold')
    ax.text(fiction_sales[i] + (non_fiction_sales[i] / 2), i, str(non_fiction_sales[i]), va='center', ha='center', color='white', fontweight='bold')
    ax.text(fiction_sales[i] + non_fiction_sales[i] + (sci_fi_sales[i] / 2), i, str(sci_fi_sales[i]), va='center', ha='center', color='white', fontweight='bold')

# Show the figure
plt.tight_layout()
plt.show()