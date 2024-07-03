
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({
    'Country': ['United States', 'China', 'Japan', 'Germany', 'India',
                'United Kingdom', 'France', 'Brazil', 'Canada', 'Russia',
                'Australia', 'South Korea', 'Italy', 'Mexico', 'Spain'],
    'Carbon_Emissions_MtCO2': [5100, 10600, 1200, 750, 2500, 400, 300, 500, 700, 1700, 400, 700, 350, 450, 300],
    'Renewable_Energy_GWh': [700000, 2200000, 100000, 160000, 300000, 80000, 120000, 250000, 180000, 70000, 50000, 40000, 80000, 60000, 90000],
    'Total_Energy_Consumption_MWh': [4000000, 10000000, 3000000, 2500000, 6000000, 1300000, 1100000, 1000000, 900000, 4000000, 1000000, 1600000, 1200000, 1300000, 1000000],
    'Population_Millions': [331, 1441, 126, 83, 1380, 68, 65, 213, 38, 146, 25, 52, 60, 129, 47]
})

data['Energy_Per_Capita'] = data['Total_Energy_Consumption_MWh'] / data['Population_Millions']
data['Renewable_Ratio'] = data['Renewable_Energy_GWh'] / data['Total_Energy_Consumption_MWh']

sns.set(style='whitegrid')

plt.figure(figsize=(16, 12))
bubble = sns.scatterplot(data=data, x='Carbon_Emissions_MtCO2', y='Energy_Per_Capita',
                         size='Renewable_Ratio', hue='Renewable_Ratio',
                         palette=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'],
                         legend='brief', alpha=0.7, sizes=(100, 2000))

plt.xlabel('Carbon Emissions (MtCO2)')
plt.ylabel('Energy Consumption Per Capita (MWh)')
plt.title('Renewable Energy vs. Carbon Emissions by Country', fontsize=16, pad=20)

plt.legend(title='Renewable Ratio', loc='upper left', bbox_to_anchor=(1, 1))
plt.show()