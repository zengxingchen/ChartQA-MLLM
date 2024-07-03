
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December'],
    'StockPrice': [150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205],
    'TradingVolume': [1200, 1250, 1300, 1400, 1500, 1600, 1550, 1650, 1700, 1750, 1800, 1850],
    'BondYield': [2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6]
}

df = pd.DataFrame(data)
df = df.set_index('Month')

df_cum = df.cumsum(axis=1)

colors = ['#4682B4', '#32CD32', '#FFD700']

plt.figure(figsize=(14, 8))

plt.fill_between(df.index, 0, df_cum['StockPrice'], color=colors[0], alpha=0.7, label='Stock Price')
plt.fill_between(df.index, df_cum['StockPrice'], df_cum['StockPrice'] + df_cum['TradingVolume'], color=colors[1], alpha=0.7, label='Trading Volume')
plt.fill_between(df.index, df_cum['StockPrice'] + df_cum['TradingVolume'], df_cum['StockPrice'] + df_cum['TradingVolume'] + df_cum['BondYield'], color=colors[2], alpha=0.7, label='Bond Yield')

for category in ['StockPrice', 'TradingVolume', 'BondYield']:
    plt.text(df.index[-1], df_cum[category][-1] - (df_cum[category][-1] - df_cum[category].shift(1)[-1]) / 2, category.replace('Price', ' Price').replace('Volume', ' Volume').replace('Yield', ' Yield'), verticalalignment='center')

plt.title('Monthly Stock Prices and Trading Volume', fontsize=16, pad=20)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Values', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.legend(loc='upper right', fontsize=12)
plt.tight_layout()

plt.show()