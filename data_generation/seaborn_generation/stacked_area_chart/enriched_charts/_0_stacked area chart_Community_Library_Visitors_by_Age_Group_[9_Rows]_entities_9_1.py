
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Given that generating an enormous amount of data points manually is per definition not feasible, 
# we'll assume the "as much as you can to provide" part refers to preparing a realistically manageable dataset for illustrative purposes.

# Data
data = {
    'Year': [i for i in range(2000, 2021)],
    'Energy': [i * 30 + 3000 for i in range(21)],
    'Industry': [i * 15 + 1500 for i in range(21)],
    'Transportation': [i * 20 + 2000 for i in range(21)],
    'Residential': [i * 5 + 500 for i in range(21)],
    'Commercial': [i * 3 + 300 for i in range(21)],
}
df = pd.DataFrame(data)

# Melting the data to long format
df_melted = df.melt('Year', var_name='Sector', value_name='Emissions')

# Pivot for cumulative sum to stack the sectors on top of each other
df_melted['Cumulative'] = df_melted.groupby('Year')['Emissions'].cumsum()

# Plot
plt.figure(figsize=(12, 6))
colors = ["#FFD700", "#FF8C00", "#1E90FF", "#32CD32", "#8A2BE2"]

# Loop to create the stacked area plot
for i, sector in enumerate(df_melted['Sector'].unique()):
    if i == 0:
        plt.fill_between(df['Year'], 0, df_melted[df_melted['Sector'] == sector]['Cumulative'], color=colors[i], label=sector)
    else:
        plt.fill_between(df['Year'], 
                         df_melted[df_melted['Sector'] == df_melted['Sector'].unique()[i-1]]['Cumulative'], 
                         df_melted[df_melted['Sector'] == sector]['Cumulative'], 
                         color=colors[i], label=sector)

# Annotating the last value of Energy for example
last_year_data = df_melted[df_melted['Year'] == df['Year'].max()]
energy_last_value = last_year_data[last_year_data['Sector'] == 'Energy']['Cumulative'].values[0]
plt.text(df['Year'].max(), energy_last_value - 250, "Energy", verticalalignment='center', horizontalalignment='center', color="white", fontsize=10)

# Customizing the plot
plt.title("CO2 Emissions Over Time by Sector")
plt.xlabel("Year")
plt.ylabel("CO2 Emissions (MtCO2)")
plt.legend(loc='upper left')
sns.despine()
plt.show()