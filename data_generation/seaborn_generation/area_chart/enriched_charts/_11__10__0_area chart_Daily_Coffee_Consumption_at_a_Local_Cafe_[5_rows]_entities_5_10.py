
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Year': ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'],
    'CO2 Emissions (Mt)': [5.1, 5.5, 5.8, 6.0, 6.2, 6.5, 6.8, 7.1, 7.3, 7.5, 7.8, 8.0, 8.3]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 8))
chart = sns.lineplot(x='Year', y='CO2 Emissions (Mt)', data=df, color="#FF5733")

plt.fill_between(x=df['Year'], y1=df['CO2 Emissions (Mt)'], color="#FF5733", alpha=0.3)

for i in range(df.shape[0]):
    plt.text(df['Year'][i], df['CO2 Emissions (Mt)'][i]+0.1, f"{df['CO2 Emissions (Mt)'][i]} Mt", horizontalalignment='center')

plt.title('Annual CO2 Emissions Over Time', fontsize=18)
plt.xlabel('Year')
plt.ylabel('CO2 Emissions (Million tonnes)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()