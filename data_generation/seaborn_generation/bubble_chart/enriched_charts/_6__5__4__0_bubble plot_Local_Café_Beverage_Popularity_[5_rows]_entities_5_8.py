
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'Country': ['USA', 'China', 'Japan', 'Germany', 'India', 'UK', 'France', 'Italy', 'Brazil', 'Canada', 'Russia', 'South Korea', 'Australia', 'Spain', 'Mexico'],
    'Speed (m/s)': [9.58, 9.85, 9.95, 9.89, 10.2, 9.77, 9.82, 9.96, 9.81, 9.87, 10.1, 9.9, 9.84, 9.88, 10.0],
    'Strength (kg)': [250, 230, 220, 240, 210, 245, 235, 220, 225, 230, 215, 225, 240, 220, 210],
    'Endurance (minutes)': [120, 140, 150, 130, 180, 125, 140, 135, 150, 160, 170, 140, 155, 145, 175],
    'Population': [331002651, 1439323776, 126476461, 83783942, 1380004385, 67886011, 65273511, 60461826, 212559417, 37742154, 145912025, 51269185, 25499884, 46754778, 128932753]
})

plt.figure(figsize=(20, 12))
bubble_chart = sns.scatterplot(
    data=data,
    x='Speed (m/s)',
    y='Endurance (minutes)',
    size='Population',
    hue='Strength (kg)',
    palette=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#c5b0d5', '#ffbb78', '#98df8a', '#c49c94', '#f7b6d2'],
    sizes=(100, 3000),
    alpha=0.6
)

plt.legend(title='Strength (kg)', loc='upper left')
plt.title('Comparison of Athlete Performance Metrics', fontsize=22, pad=20)
plt.xlabel('Speed (m/s)', fontsize=16)
plt.ylabel('Endurance (minutes)', fontsize=16)
plt.show()