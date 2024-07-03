
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'Country': ['USA', 'China', 'Japan', 'Germany', 'India', 'UK', 'France', 'Italy', 'Brazil', 'Canada', 'Russia', 'South Korea', 'Australia', 'Spain', 'Mexico'],
    'CarbonEmissions': [5000, 10000, 1200, 800, 2500, 400, 350, 300, 1600, 500, 1700, 800, 550, 300, 1200],
    'RenewableEnergy': [11, 20, 15, 35, 25, 40, 38, 33, 45, 70, 15, 5, 25, 30, 20],
    'EPI': [71.1, 65.2, 74.9, 81.3, 58.7, 79.2, 83.6, 80.1, 67.4, 84.1, 63.5, 68.1, 76.5, 81.7, 65.0],
    'Population': [331002651, 1439323776, 126476461, 83783942, 1380004385, 67886011, 65273511, 60461826, 212559417, 37742154, 145912025, 51269185, 25499884, 46754778, 128932753]
})

plt.figure(figsize=(18, 14))
bubble_chart = sns.scatterplot(
    data=data,
    x='CarbonEmissions',
    y='RenewableEnergy',
    size='Population',
    hue='EPI',
    palette=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#c5b0d5', '#ffbb78', '#98df8a', '#c49c94', '#f7b6d2'],
    sizes=(100, 3000),
    alpha=0.6
)

plt.legend(title='Environmental Performance Index', loc='upper right')
plt.title('Comparison of Carbon Emissions, Renewable Energy Usage, and EPI', fontsize=22, pad=20)
plt.xlabel('Carbon Emissions (in million tons)', fontsize=16)
plt.ylabel('Renewable Energy Usage (%)', fontsize=16)
plt.show()