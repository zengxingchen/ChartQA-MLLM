
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'Country': ['USA', 'China', 'Japan', 'Germany', 'India', 'UK', 'France', 'Italy', 'Brazil', 'Canada', 'Russia', 'South Korea', 'Australia', 'Spain', 'Mexico'],
    'ArtIndex': [85, 78, 90, 88, 65, 82, 87, 86, 72, 80, 68, 89, 83, 84, 70],
    'CreativeEconomy': [1500, 1300, 1100, 1150, 900, 1200, 1100, 1000, 850, 1250, 950, 1050, 1150, 1080, 850],
    'Population': [331002651, 1439323776, 126476461, 83783942, 1380004385, 67886011, 65273511, 60461826, 212559417, 37742154, 145912025, 51269185, 25499884, 46754778, 128932753],
    'LifeExpectancy': [78.5, 76.4, 84.6, 81.3, 69.7, 81.2, 82.7, 83.4, 75.7, 82.3, 72.6, 82.8, 83.3, 83.6, 75.0]
})

plt.figure(figsize=(18, 14))
bubble_chart = sns.scatterplot(
    data=data,
    x='CreativeEconomy',
    y='ArtIndex',
    size='Population',
    hue='LifeExpectancy',
    palette=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#fdae61', '#d73027', '#4575b4', '#fee08b', '#91bfdb'],
    sizes=(100, 2500),
    alpha=0.6
)

plt.legend(title='Life Expectancy')
plt.title('Art & Design: Correlation between Creative Economy and Art Index', fontsize=22)
plt.xlabel('Creative Economy (in million USD)', fontsize=16)
plt.ylabel('Art Index', fontsize=16)
plt.show()