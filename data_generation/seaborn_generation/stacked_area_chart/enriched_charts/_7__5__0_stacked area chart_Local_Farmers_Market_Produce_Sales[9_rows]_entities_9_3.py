
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Quarter': ['Q1-2021', 'Q2-2021', 'Q3-2021', 'Q4-2021', 'Q1-2022', 'Q2-2022', 'Q3-2022', 'Q4-2022', 'Q1-2023', 'Q2-2023', 'Q3-2023', 'Q4-2023'],
    'Physical Health': [15.25, 18.30, 21.75, 24.90, 28.55, 32.10, 35.85, 39.50, 43.75, 47.80, 51.90, 56.00],
    'Healthy Eating': [20.35, 22.50, 25.80, 28.50, 32.00, 35.20, 38.75, 42.00, 45.60, 49.20, 52.75, 56.30],
    'Mental Health': [25.55, 28.65, 32.10, 35.00, 38.75, 42.30, 46.10, 50.25, 54.50, 58.30, 62.40, 66.50]
}

df = pd.DataFrame(data)
df.set_index('Quarter', inplace=True)

cumulative_revenue = df.cumsum(axis=1)

plt.figure(figsize=(16, 9))

plt.stackplot(df.index, cumulative_revenue['Physical Health'], cumulative_revenue['Healthy Eating'], cumulative_revenue['Mental Health'],
              labels=['Physical Health', 'Healthy Eating', 'Mental Health'],
              colors=['#FF9999', '#66B3FF', '#99FF99'], alpha=0.8)

plt.legend(loc='upper left')

plt.annotate('Significant Growth', xy=('Q4-2023', cumulative_revenue.loc['Q4-2023', 'Mental Health']),
             xytext=(-60, -30), textcoords='offset points', arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.5'))

plt.title('Trends in Health and Well-being Over Time')
plt.xlabel('Quarter')
plt.ylabel('Health Metrics (in millions)')

plt.tight_layout()
plt.show()