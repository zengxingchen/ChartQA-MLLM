
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Data Frame
data = {
    "Year": ['2021', '2021', '2021', '2021', '2021', '2021', '2021',
             '2022', '2022', '2022', '2022', '2022', '2022', '2022',
             '2023', '2023', '2023', '2023', '2023', '2023', '2023'],
    "Category": ['Stocks', 'Bonds', 'Real Estate', 'Mutual Funds', 'Commodities', 'ETFs', 'Foreign Exchange',
                 'Stocks', 'Bonds', 'Real Estate', 'Mutual Funds', 'Commodities', 'ETFs', 'Foreign Exchange',
                 'Stocks', 'Bonds', 'Real Estate', 'Mutual Funds', 'Commodities', 'ETFs', 'Foreign Exchange'],
    "Market Share": [30.12, 25.34, 15.56, 12.23, 8.67, 8.08, 4.00,
                     32.23, 24.14, 14.45, 13.56, 7.45, 6.17, 2.00,
                     34.87, 23.04, 13.34, 14.56, 6.23, 5.67, 2.00]
}
df = pd.DataFrame(data)

# Settings
plt.figure(figsize=(18, 12))
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f']

# Treemap plot
squarify.plot(sizes=df["Market Share"], label=df["Category"], color=colors, alpha=0.8)
plt.title("Investment Market Share (2021-2023)", fontsize=20, color='#333333')
plt.axis('off')
plt.show()