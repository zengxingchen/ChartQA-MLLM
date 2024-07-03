
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Quarter': ['Q1-2021', 'Q2-2021', 'Q3-2021', 'Q4-2021', 'Q1-2022', 'Q2-2022', 'Q3-2022', 'Q4-2022',
                'Q1-2023', 'Q2-2023', 'Q3-2023', 'Q4-2023', 'Q1-2024', 'Q2-2024', 'Q3-2024', 'Q4-2024'],
    'Solar': [15.1, 18.3, 22.5, 25.8, 28.9, 32.4, 35.6, 38.9, 42.3, 45.6, 48.9, 52.1, 55.3, 58.6, 61.9, 65.1],
    'Wind': [35.2, 38.7, 42.0, 45.3, 48.1, 51.0, 54.0, 57.4, 60.8, 64.1, 67.4, 70.8, 74.2, 77.5, 80.8, 84.2],
    'Hydroelectric': [42.6, 44.1, 46.0, 47.8, 50.3, 52.5, 54.8, 57.1, 59.5, 61.9, 64.1, 66.4, 68.7, 71.0, 73.2, 75.5]
}

df = pd.DataFrame(data)
df.set_index('Quarter', inplace=True)

cumulative_production = df.cumsum(axis=1)

plt.figure(figsize=(14, 8))

plt.stackplot(df.index, cumulative_production['Solar'],
              cumulative_production['Wind'],
              cumulative_production['Hydroelectric'],
              labels=['Solar', 'Wind', 'Hydroelectric'],
              colors=['#FFA07A', '#20B2AA', '#87CEFA'], alpha=0.85)

plt.legend(loc='upper left')
plt.annotate('Highest Solar Production', xy=('Q4-2024', cumulative_production.loc['Q4-2024', 'Solar']),
             xytext=(-80, 20), textcoords='offset points', arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.5'))

plt.title('Quarterly Renewable Energy Production (in Terawatt-hours)', fontsize=16, y=1.02)
plt.xlabel('Quarter')
plt.ylabel('Production (in Terawatt-hours)')

plt.tight_layout()
plt.show()