
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Year': [2019, 2019, 2019, 2019, 2020, 2020, 2020, 2020, 2021, 2021, 2021, 2021, 2022, 2022, 2022, 2022, 2023, 2023, 2023, 2023],
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q4', 'Q1', 'Q2', 'Q3', 'Q4', 'Q1', 'Q2', 'Q3', 'Q4', 'Q1', 'Q2', 'Q3', 'Q4', 'Q1', 'Q2', 'Q3', 'Q4'],
    'CO2 Emissions (Million Metric Tons)': [4300, 4250, 4280, 4220, 4100, 3950, 4000, 4050, 4100, 4200, 4300, 4250, 4350, 4400, 4450, 4500, 4550, 4600, 4650, 4700]
}

df = pd.DataFrame(data)
df['Period'] = df['Year'].astype(str) + '-' + df['Quarter']

plt.figure(figsize=(14, 7))
plt.fill_between(df['Period'], df['CO2 Emissions (Million Metric Tons)'], color='#4682B4', alpha=0.7)

for i in range(len(df)):
    plt.text(i, df['CO2 Emissions (Million Metric Tons)'][i], str(df['CO2 Emissions (Million Metric Tons)'][i]), ha='center', va='bottom', fontsize=8)

plt.title('Quarterly CO2 Emissions (Million Metric Tons) Over Five Years', fontsize=18, pad=20)
plt.xlabel('Period', fontsize=14)
plt.ylabel('CO2 Emissions (Million Metric Tons)', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('CO2_Emissions_Area_Chart.png')
plt.show()