
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 
            31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
    'StockPrice': [150, 155, 160, 158, 162, 161, 165, 168, 170, 169, 172, 174, 175, 173, 177, 179, 176, 180, 182, 181, 
                   184, 186, 188, 185, 189, 190, 192, 191, 194, 195, 193, 196, 198, 197, 199, 200, 202, 201, 204, 206, 
                   205, 208, 207, 209, 210, 212, 211, 214, 213, 215],
    'TradingVolume': [20000, 21000, 19500, 22000, 22500, 20500, 23000, 21500, 24000, 23500, 25000, 24500, 25500, 26000, 
                      26500, 27000, 27500, 28000, 28500, 29000, 29500, 30000, 30500, 31000, 31500, 32000, 32500, 33000, 
                      33500, 34000, 34500, 35000, 35500, 36000, 36500, 37000, 37500, 38000, 38500, 39000, 39500, 40000, 
                      40500, 41000, 41500, 42000, 42500, 43000, 43500, 44000]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 12))
scatterplot = sns.scatterplot(x='StockPrice', y='TradingVolume', data=df, color='#32CD32')

scatterplot.set_title('Daily Stock Prices vs Trading Volume', fontsize=22, pad=20)
scatterplot.set_xlabel('Stock Price (USD)', fontsize=18)
scatterplot.set_ylabel('Trading Volume', fontsize=18)

plt.show()