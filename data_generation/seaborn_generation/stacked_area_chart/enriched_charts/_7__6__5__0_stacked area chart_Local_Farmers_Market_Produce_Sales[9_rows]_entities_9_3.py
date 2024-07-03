
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Quarter': ['Q1-2021', 'Q2-2021', 'Q3-2021', 'Q4-2021', 'Q1-2022', 'Q2-2022', 'Q3-2022', 'Q4-2022', 'Q1-2023', 'Q2-2023', 'Q3-2023', 'Q4-2023', 'Q1-2024', 'Q2-2024', 'Q3-2024', 'Q4-2024'],
    'Physical Activity': [45.12, 48.34, 51.78, 55.45, 58.70, 62.30, 65.90, 69.55, 73.20, 76.85, 80.50, 84.20, 87.85, 91.50, 95.15, 98.80],
    'Healthy Eating': [30.25, 32.45, 35.90, 39.15, 42.50, 45.75, 48.95, 52.30, 55.60, 58.90, 62.20, 65.55, 68.85, 72.15, 75.45, 78.75],
    'Mental Well-being': [35.60, 38.10, 40.75, 43.60, 46.80, 50.20, 53.60, 57.05, 60.50, 64.00, 67.55, 71.15, 74.70, 78.30, 81.95, 85.60]
}

df = pd.DataFrame(data)
df.set_index('Quarter', inplace=True)

cumulative_emissions = df.cumsum(axis=1)

plt.figure(figsize=(14, 8))

plt.stackplot(df.index, cumulative_emissions['Physical Activity'], cumulative_emissions['Healthy Eating'], cumulative_emissions['Mental Well-being'],
              labels=['Physical Activity', 'Healthy Eating', 'Mental Well-being'],
              colors=['#4B0082', '#FF1493', '#00CED1'], alpha=0.8)

plt.legend(loc='upper left')

plt.annotate('Significant Improvement', xy=('Q4-2024', cumulative_emissions.loc['Q4-2024', 'Mental Well-being']),
             xytext=(-70, -50), textcoords='offset points', arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.5'))

plt.title('Quarterly Health & Well-being Trends (2021-2024)', fontsize=16, pad=20)
plt.xlabel('Quarter', fontsize=14)
plt.ylabel('Health Index', fontsize=14)

plt.tight_layout()
plt.show()