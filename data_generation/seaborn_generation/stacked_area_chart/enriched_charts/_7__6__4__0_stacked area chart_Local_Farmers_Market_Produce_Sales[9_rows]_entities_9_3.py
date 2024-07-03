
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Quarter': ['Q1-2021', 'Q2-2021', 'Q3-2021', 'Q4-2021', 'Q1-2022', 'Q2-2022', 'Q3-2022', 'Q4-2022',
                'Q1-2023', 'Q2-2023', 'Q3-2023', 'Q4-2023', 'Q1-2024', 'Q2-2024', 'Q3-2024', 'Q4-2024'],
    'Carbon Dioxide': [25.5, 27.3, 29.0, 30.8, 32.5, 34.1, 35.7, 37.3, 39.0, 40.6, 42.3, 44.0, 45.5, 47.0, 48.5, 50.0],
    'Methane': [8.7, 9.2, 9.7, 10.1, 10.6, 11.0, 11.4, 11.8, 12.3, 12.7, 13.1, 13.5, 14.0, 14.4, 14.8, 15.2],
    'Nitrous Oxide': [2.4, 2.8, 3.2, 3.6, 4.0, 4.4, 4.8, 5.2, 5.6, 6.0, 6.4, 6.8, 7.1, 7.4, 7.7, 8.0]
}

df = pd.DataFrame(data)
df.set_index('Quarter', inplace=True)

cumulative_emissions = df.cumsum(axis=1)

plt.figure(figsize=(14, 8))

plt.stackplot(df.index, cumulative_emissions['Carbon Dioxide'],
              cumulative_emissions['Methane'],
              cumulative_emissions['Nitrous Oxide'],
              labels=['Carbon Dioxide', 'Methane', 'Nitrous Oxide'],
              colors=['#1f77b4', '#ff7f0e', '#2ca02c'], alpha=0.8)

plt.legend(loc='upper left')

plt.annotate('Highest Methane Emissions', xy=('Q4-2024', cumulative_emissions.loc['Q4-2024', 'Methane']),
             xytext=(-100, 50), textcoords='offset points', arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.5'))

plt.title('Quarterly Greenhouse Gas Emissions (in million metric tons)', fontsize=16)
plt.xlabel('Quarter')
plt.ylabel('Emissions')

plt.tight_layout()
plt.show()