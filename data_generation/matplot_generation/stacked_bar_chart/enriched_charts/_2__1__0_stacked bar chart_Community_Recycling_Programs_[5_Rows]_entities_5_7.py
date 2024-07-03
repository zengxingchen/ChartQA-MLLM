
import matplotlib.pyplot as plt

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021']
online_sales = [12000, 15000, 18000, 21000, 24000, 28000, 31000]
in_store_sales = [15000, 17000, 20000, 23000, 25000, 27000, 29000]
subscriptions = [5000, 7000, 8000, 10000, 12000, 14000, 16000]

# Bottom data for stacking
in_store_sales_bottom = online_sales
subscriptions_bottom = [i + j for i, j in zip(online_sales, in_store_sales)]

# Figure and Axes
fig, ax = plt.subplots(figsize=(10, 6))

# Stacked Bars
ax.barh(years, online_sales, color='#1f77b4', edgecolor='white', height=0.5, label='Online Sales')
ax.barh(years, in_store_sales, left=in_store_sales_bottom, color='#ff7f0e', edgecolor='white', height=0.5, label='In-Store Sales')
ax.barh(years, subscriptions, left=subscriptions_bottom, color='#2ca02c', edgecolor='white', height=0.5, label='Subscriptions')

# Labels and Title
ax.set_xlabel('Number of Sales')
ax.set_ylabel('Year')
ax.set_title('Annual Sales Overview by Type (2015-2021)', pad=20)

# Adding numerical labels
for i in range(len(years)):
    ax.text(online_sales[i] / 2, years[i], str(online_sales[i]), va='center', ha='center', color='white', fontsize=8, fontweight='bold')
    ax.text(in_store_sales_bottom[i] + (in_store_sales[i] / 2), years[i], str(in_store_sales[i]), va='center', ha='center', color='white', fontsize=8, fontweight='bold')
    ax.text(subscriptions_bottom[i] + (subscriptions[i] / 2), years[i], str(subscriptions[i]), va='center', ha='center', color='white', fontsize=8, fontweight='bold')

# Legend
ax.legend(loc='upper right')

# Display the plot
plt.show()