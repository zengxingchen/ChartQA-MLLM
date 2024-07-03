
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Quarter': ['Q1-2021', 'Q2-2021', 'Q3-2021', 'Q4-2021', 'Q1-2022', 'Q2-2022', 'Q3-2022', 'Q4-2022',
                'Q1-2023', 'Q2-2023', 'Q3-2023', 'Q4-2023'],
    'Cardio': [45.3, 48.7, 51.2, 54.1, 56.7, 59.3, 62.1, 65.4, 68.1, 70.8, 73.5, 76.2],
    'Yoga': [32.6, 34.1, 36.0, 37.8, 39.4, 41.0, 42.7, 44.3, 46.0, 47.6, 49.1, 50.8],
    'Strength': [21.7, 23.5, 25.1, 26.3, 27.6, 28.9, 30.1, 31.2, 32.5, 33.8, 35.1, 36.4]
}

df = pd.DataFrame(data)
df.set_index('Quarter', inplace=True)

cumulative_revenue = df.cumsum(axis=1)

plt.figure(figsize=(16, 10))

plt.stackplot(df.index, cumulative_revenue['Cardio'],
              cumulative_revenue['Yoga'],
              cumulative_revenue['Strength'],
              labels=['Cardio', 'Yoga', 'Strength'],
              colors=['#FF6347', '#4682B4', '#32CD32'], alpha=0.85)

plt.legend(loc='upper left')
plt.annotate('Highest Cardio Revenue', xy=('Q4-2023', cumulative_revenue.loc['Q4-2023', 'Cardio']),
             xytext=(-100, 30), textcoords='offset points', arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.5'))

plt.title('Quarterly Revenue of Fitness Activities (in millions)', fontsize=16, y=1.05)
plt.xlabel('Quarter')
plt.ylabel('Revenue (in millions)')

plt.tight_layout()
plt.show()