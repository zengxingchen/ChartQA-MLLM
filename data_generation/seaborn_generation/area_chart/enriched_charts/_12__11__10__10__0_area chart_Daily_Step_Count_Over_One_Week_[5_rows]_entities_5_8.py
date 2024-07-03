
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Month': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
    'Revenue': [20000, 21000, 21500, 23000, 24000, 24500, 26000, 25500, 27000, 26500, 28000, 27500, 29000, 28500, 30000, 29500, 31000, 30500, 32000, 31500, 33000, 32500, 34000, 33500, 35000, 34500, 36000, 35500, 37000, 36500, 38000]
}

df = pd.DataFrame(data)

plt.figure(figsize=(20, 10))
area_chart = sns.lineplot(data=df, x='Month', y='Revenue', color='#FF6347')
area_chart.fill_between(df['Month'], df['Revenue'], color='#FFA07A', alpha=0.5)

max_revenue = df['Revenue'].max()
max_month = df['Revenue'].idxmax() + 1
plt.text(max_month, max_revenue, 'Peak\nRevenue', horizontalalignment='center', verticalalignment='bottom', color='#2E8B57')

plt.title("Monthly Revenue Over a Year", pad=20)
plt.xlabel("Month")
plt.ylabel("Revenue (in USD)")

plt.show()