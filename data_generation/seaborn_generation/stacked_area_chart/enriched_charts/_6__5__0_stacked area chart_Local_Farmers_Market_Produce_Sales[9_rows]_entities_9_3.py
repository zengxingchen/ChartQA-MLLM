
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Quarter': ['Q1-2021', 'Q2-2021', 'Q3-2021', 'Q4-2021', 'Q1-2022', 'Q2-2022', 'Q3-2022', 'Q4-2022', 'Q1-2023', 'Q2-2023', 'Q3-2023', 'Q4-2023'],
    'Transport': [50.15, 55.67, 60.70, 65.88, 70.55, 75.20, 80.25, 85.70, 90.90, 95.80, 100.95, 105.50],
    'Industry': [70.45, 75.50, 78.55, 81.20, 85.30, 88.70, 92.10, 95.30, 98.60, 101.40, 105.10, 108.50],
    'Residential': [20.30, 25.60, 30.85, 35.90, 40.95, 45.75, 50.85, 55.95, 60.05, 65.25, 70.45, 75.75]
}

df = pd.DataFrame(data)
df.set_index('Quarter', inplace=True)

cumulative_emissions = df.cumsum(axis=1)

plt.figure(figsize=(16, 10))

plt.stackplot(df.index, cumulative_emissions['Transport'], cumulative_emissions['Industry'], cumulative_emissions['Residential'],
              labels=['Transport', 'Industry', 'Residential'],
              colors=['#1E90FF', '#FF6347', '#3CB371'], alpha=0.8)

plt.legend(loc='upper left')

plt.annotate('Peak Emissions', xy=('Q4-2023', cumulative_emissions.loc['Q4-2023', 'Residential']),
             xytext=(-70, -50), textcoords='offset points', arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.5'))

plt.title('Quarterly CO2 Emissions by Sector (2021-2023)', fontsize=16, pad=20)
plt.xlabel('Quarter', fontsize=14)
plt.ylabel('CO2 Emissions (in million tonnes)', fontsize=14)

plt.tight_layout()
plt.show()