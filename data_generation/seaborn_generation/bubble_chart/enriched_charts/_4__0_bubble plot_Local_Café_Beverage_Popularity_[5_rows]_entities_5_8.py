
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'Country': ['USA', 'China', 'Japan', 'Germany', 'India', 'UK', 'France', 'Italy', 'Brazil', 'Canada', 'Russia', 'South Korea', 'Australia', 'Spain', 'Mexico'],
    'GDP': [21427700, 14342903, 5081770, 3845630, 2875142, 2825208, 2715518, 2001196, 1444731, 1647784, 1483490, 1655608, 1392687, 1393355, 1265772],
    'LifeExpectancy': [78.5, 76.4, 84.6, 81.3, 69.7, 81.2, 82.7, 83.4, 75.7, 82.3, 72.6, 82.8, 83.3, 83.6, 75.0],
    'Population': [331002651, 1439323776, 126476461, 83783942, 1380004385, 67886011, 65273511, 60461826, 212559417, 37742154, 145912025, 51269185, 25499884, 46754778, 128932753],
    'HappinessScore': [7.0, 5.1, 5.9, 6.7, 4.0, 7.2, 6.5, 6.0, 6.3, 7.6, 5.9, 6.4, 7.2, 6.4, 6.5]
})

plt.figure(figsize=(16, 12))
bubble_chart = sns.scatterplot(
    data=data,
    x='GDP',
    y='HappinessScore',
    size='Population',
    hue='LifeExpectancy',
    palette=['#4c72b0', '#55a868', '#c44e52', '#8172b2', '#ccb974', '#64b5cd', '#ff9f6b', '#cfcfcf', '#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3', '#fdb462', '#b3de69'],
    sizes=(100, 2500),
    alpha=0.6
)

plt.legend(title='Life Expectancy')
plt.title('Comparison of GDP, Population, and Happiness', fontsize=22)
plt.xlabel('GDP (in million USD)', fontsize=16)
plt.ylabel('Happiness Score', fontsize=16)
plt.show()