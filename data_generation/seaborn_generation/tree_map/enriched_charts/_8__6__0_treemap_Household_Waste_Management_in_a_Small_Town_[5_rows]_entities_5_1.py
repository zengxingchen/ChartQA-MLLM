
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Data Frame
data = {
    "Year": ['2021', '2021', '2021', '2021', '2021', '2021', '2021', '2021', '2021',
             '2022', '2022', '2022', '2022', '2022', '2022', '2022', '2022', '2022',
             '2023', '2023', '2023', '2023', '2023', '2023', '2023', '2023', '2023'],
    "Investment_Type": ['Stocks', 'Bonds', 'Real Estate', 'Mutual Funds', 'ETFs', 'Cryptocurrency', 'Gold', 'Commodities', 'Other',
                        'Stocks', 'Bonds', 'Real Estate', 'Mutual Funds', 'ETFs', 'Cryptocurrency', 'Gold', 'Commodities', 'Other',
                        'Stocks', 'Bonds', 'Real Estate', 'Mutual Funds', 'ETFs', 'Cryptocurrency', 'Gold', 'Commodities', 'Other'],
    "Percentage": [35.5, 15.2, 18.3, 10.5, 8.7, 5.4, 3.9, 2.5, 0.9,
                   36.0, 14.9, 18.8, 10.7, 9.1, 5.6, 4.0, 2.4, 1.0,
                   37.2, 14.3, 19.0, 11.0, 9.5, 5.7, 4.2, 2.3, 1.1]
}
df = pd.DataFrame(data)

# Settings
plt.figure(figsize=(18, 12))
colors = ['#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3', '#fdb462', '#b3de69', '#fccde5', '#d9d9d9']

# Treemap plot
squarify.plot(sizes=df["Percentage"], label=df["Investment_Type"], color=colors, alpha=0.8)
plt.title("Investment Types Distribution (2021-2023)", fontsize=20, color='#333333', pad=20, loc='center')
plt.axis('off')
plt.show()