
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Data Frame
data = {
    "Year": ['2021', '2021', '2021', '2021', '2021', '2021',
             '2022', '2022', '2022', '2022', '2022', '2022',
             '2023', '2023', '2023', '2023', '2023', '2023'],
    "Browser": ['Chrome', 'Edge', 'Firefox', 'Safari', 'Opera', 'Others',
                'Chrome', 'Edge', 'Firefox', 'Safari', 'Opera', 'Others',
                'Chrome', 'Edge', 'Firefox', 'Safari', 'Opera', 'Others'],
    "Market Share": [63.58, 4.01, 3.87, 19.16, 2.43, 6.95,
                     64.95, 4.19, 3.76, 18.65, 2.35, 6.10,
                     65.87, 4.23, 3.65, 18.34, 2.28, 5.63]
}
df = pd.DataFrame(data)

# Settings
plt.figure(figsize=(14, 8))
colors = ['#1f78b4', '#33a02c', '#6a3d9a', '#b2df8a', '#fdbf6f', '#ff7f00']

# Treemap plot
squarify.plot(sizes=df["Market Share"], label=df["Browser"], color=colors, alpha=0.8)
plt.title("Web Browser Market Share (2021-2023)", fontsize=18, color='#555555')
plt.axis('off')
plt.show()