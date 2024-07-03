
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Data Frame
data = {
    "Year": ['2019', '2019', '2019', '2019', '2019', '2019', '2019',
             '2020', '2020', '2020', '2020', '2020', '2020', '2020',
             '2021', '2021', '2021', '2021', '2021', '2021', '2021',
             '2022', '2022', '2022', '2022', '2022', '2022', '2022'],
    "Company": ['Apple', 'Microsoft', 'Amazon', 'Google', 'Facebook', 'Netflix', 'Tesla',
                'Apple', 'Microsoft', 'Amazon', 'Google', 'Facebook', 'Netflix', 'Tesla',
                'Apple', 'Microsoft', 'Amazon', 'Google', 'Facebook', 'Netflix', 'Tesla',
                'Apple', 'Microsoft', 'Amazon', 'Google', 'Facebook', 'Netflix', 'Tesla'],
    "Revenue": [260.2, 125.8, 280.5, 161.9, 70.7, 20.2, 24.6,
                274.5, 143.0, 386.1, 182.5, 85.9, 25.0, 31.5,
                365.8, 168.1, 469.8, 257.6, 117.9, 29.7, 53.8,
                394.3, 198.3, 514.0, 280.8, 128.3, 31.6, 81.5]
}
df = pd.DataFrame(data)

# Settings
plt.figure(figsize=(16, 10))
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFF5', '#FFC300', '#DAF7A6']

# Treemap plot
squarify.plot(sizes=df["Revenue"], label=df["Company"], color=colors, alpha=0.8)
plt.title("Top Tech Companies' Revenue (2019-2022)", fontsize=18, color='#555555', y=1.05)
plt.axis('off')
plt.show()