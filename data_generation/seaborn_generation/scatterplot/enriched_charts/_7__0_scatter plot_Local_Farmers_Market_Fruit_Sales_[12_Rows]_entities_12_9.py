
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
            16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    'StockPrice': [100, 102, 104, 101, 107, 110, 115, 117, 113, 111,
                   112, 118, 121, 125, 123, 120, 119, 121, 124, 126,
                   129, 130, 128, 127, 131, 133, 135, 136, 134, 137],
    'Volume': [12000, 15000, 16000, 14000, 17000, 18000, 19000, 20000,
               21000, 19500, 18000, 20500, 22000, 22500, 23000, 21000,
               20500, 21500, 22000, 23000, 24000, 25000, 24500, 23500,
               25500, 26000, 27000, 27500, 26500, 28000]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(14, 7))
scatterplot = sns.scatterplot(x='StockPrice', y='Volume',
                              data=df, palette=['#1f77b4', '#ff7f0e'])

scatterplot.set_title('Daily Stock Prices and Trading Volumes', fontsize=16, pad=20)
scatterplot.set_xlabel('Stock Price ($)', fontsize=14)
scatterplot.set_ylabel('Trading Volume', fontsize=14)

plt.show()