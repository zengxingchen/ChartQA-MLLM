
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Category': 'Portfolio 1', 'Stocks': '20%', 'Bonds': '30%', 'Real Estate': '15%', 'Commodities': '10%', 'Cryptocurrency': '15%', 'Art & Collectibles': '10%'},
    {'Category': 'Portfolio 2', 'Stocks': '25%', 'Bonds': '25%', 'Real Estate': '20%', 'Commodities': '10%', 'Cryptocurrency': '10%', 'Art & Collectibles': '10%'},
    {'Category': 'Portfolio 3', 'Stocks': '15%', 'Bonds': '20%', 'Real Estate': '25%', 'Commodities': '10%', 'Cryptocurrency': '15%', 'Art & Collectibles': '15%'},
    {'Category': 'Portfolio 4', 'Stocks': '30%', 'Bonds': '20%', 'Real Estate': '10%', 'Commodities': '15%', 'Cryptocurrency': '10%', 'Art & Collectibles': '15%'},
    {'Category': 'Portfolio 5', 'Stocks': '20%', 'Bonds': '15%', 'Real Estate': '25%', 'Commodities': '15%', 'Cryptocurrency': '15%', 'Art & Collectibles': '10%'},
    {'Category': 'Portfolio 6', 'Stocks': '25%', 'Bonds': '15%', 'Real Estate': '20%', 'Commodities': '10%', 'Cryptocurrency': '20%', 'Art & Collectibles': '10%'},
    {'Category': 'Portfolio 7', 'Stocks': '20%', 'Bonds': '25%', 'Real Estate': '15%', 'Commodities': '20%', 'Cryptocurrency': '10%', 'Art & Collectibles': '10%'},
    {'Category': 'Portfolio 8', 'Stocks': '30%', 'Bonds': '20%', 'Real Estate': '10%', 'Commodities': '20%', 'Cryptocurrency': '10%', 'Art & Collectibles': '10%'},
    {'Category': 'Portfolio 9', 'Stocks': '20%', 'Bonds': '20%', 'Real Estate': '20%', 'Commodities': '10%', 'Cryptocurrency': '15%', 'Art & Collectibles': '15%'},
    {'Category': 'Portfolio 10', 'Stocks': '25%', 'Bonds': '15%', 'Real Estate': '15%', 'Commodities': '15%', 'Cryptocurrency': '15%', 'Art & Collectibles': '15%'}
]

df = pd.DataFrame(data)
df = df.set_index('Category')
df = df.applymap(lambda x: int(x.replace('%', '')))

cumulative_sum = df.cumsum(axis=1)

colors = ['#1f78b4', '#33a02c', '#e31a1c', '#ff7f00', '#6a3d9a', '#b15928']

fig, ax = plt.subplots(figsize=(10, 14))

bottom = None

for column, color in zip(df.columns, colors):
    ax.bar(df.index, df[column], bottom=bottom, label=column, color=color, width=0.5)
    bottom = cumulative_sum[column]

ax.legend(title='Investment Types', bbox_to_anchor=(1.05, 1), loc='upper left')

ax.set_ylabel('Percentage')
ax.set_xlabel('Investment Portfolios')
ax.set_title('Investment Distribution Across Various Portfolios', pad=20)

plt.xticks(rotation=90)
plt.tight_layout()
plt.show()