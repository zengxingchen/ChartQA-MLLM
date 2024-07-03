
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Quarter': ['Q1-2021', 'Q2-2021', 'Q3-2021', 'Q4-2021', 'Q1-2022', 'Q2-2022', 'Q3-2022', 'Q4-2022',
                'Q1-2023', 'Q2-2023', 'Q3-2023', 'Q4-2023', 'Q1-2024', 'Q2-2024', 'Q3-2024', 'Q4-2024'],
    'Walking': [5.2, 6.3, 7.5, 8.6, 9.7, 10.8, 11.9, 13.0, 14.2, 15.3, 16.4, 17.5, 18.6, 19.7, 20.8, 21.9],
    'Cycling': [3.4, 3.8, 4.2, 4.5, 4.9, 5.3, 5.7, 6.1, 6.5, 6.9, 7.3, 7.7, 8.1, 8.5, 8.9, 9.3],
    'Running': [2.3, 2.8, 3.1, 3.5, 3.8, 4.2, 4.6, 4.9, 5.3, 5.7, 6.1, 6.4, 6.8, 7.2, 7.5, 7.9]
}

df = pd.DataFrame(data)
df.set_index('Quarter', inplace=True)

cumulative_production = df.cumsum(axis=1)

plt.figure(figsize=(16, 10))

plt.stackplot(df.index, cumulative_production['Walking'],
              cumulative_production['Cycling'],
              cumulative_production['Running'],
              labels=['Walking', 'Cycling', 'Running'],
              colors=['#FF6347', '#4682B4', '#32CD32'], alpha=0.85)

plt.legend(loc='upper left')
plt.annotate('Highest Running Activity', xy=('Q4-2024', cumulative_production.loc['Q4-2024', 'Running']),
             xytext=(-100, 20), textcoords='offset points', arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.5'))

plt.title('Quarterly Physical Activity Levels (in Hours)', fontsize=18, y=1.03)
plt.xlabel('Quarter')
plt.ylabel('Activity Levels (in Hours)')

plt.tight_layout()
plt.show()