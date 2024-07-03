
import matplotlib.pyplot as plt

countries = ['France', 'Spain', 'USA', 'China', 'Italy', 'Turkey', 'Mexico', 'Thailand', 'Germany', 'UK', 'Japan', 'Austria', 'Greece', 'Malaysia', 'Russia', 'Canada', 'Australia', 'South Korea', 'Netherlands', 'Brazil']
year = [2022] * len(countries)
tourists = [89000000, 84000000, 79000000, 60000000, 58000000, 46000000, 45000000, 41000000, 39000000, 38000000, 32000000, 30000000, 29000000, 26000000, 25000000, 24000000, 23000000, 22000000, 20000000, 19000000]
revenue = [70000000000, 68000000000, 72000000000, 50000000000, 45000000000, 35000000000, 38000000000, 31000000000, 36000000000, 34000000000, 29000000000, 26000000000, 27000000000, 25000000000, 24000000000, 23000000000, 22000000000, 21000000000, 20000000000, 19000000000]

size = [x / 1000000 for x in tourists]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#1a55b4', '#ff1f0e', '#2ca03c', '#d61728', '#9467ad', '#8c664b', '#e357c2', '#7f8f7f', '#bccd22', '#17aebf']

fig, ax = plt.subplots(figsize=(14, 7))

sc = ax.scatter(countries, year, s=size, c=colors, alpha=0.6, edgecolors='w')

ax.set_title('Top Tourist Destinations and Revenue - 2022')
ax.set_xlabel('Countries')
ax.set_ylabel('Year')
ax.set_yticks([2022])
ax.grid(True)

revenue_tick_vals = range(18000000000, 75000000000, 5000000000)
revenue_tick_labels = ['$' + str(val // 1000000000) + 'B' for val in revenue_tick_vals]
sm = plt.cm.ScalarMappable(cmap=plt.cm.jet, norm=plt.Normalize(vmin=min(revenue), vmax=max(revenue)))
sm._A = []
cbar = plt.colorbar(sm, ticks=revenue_tick_vals)
cbar.ax.set_yticklabels(revenue_tick_labels)
cbar.set_label('Tourism Revenue')

plt.show()