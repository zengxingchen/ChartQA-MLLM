
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Data
data = {
    'Year': [i for i in range(2000, 2023)],
    'Healthcare': [6000 + 100 * i for i in range(23)],
    'Research': [1600 + 100 * i for i in range(23)],
    'Development': [1300 + 100 * i for i in range(23)],
    'Wellness': [900 + 100 * i for i in range(23)],
    'Administration': [700 + 100 * i for i in range(23)],
}
df = pd.DataFrame(data)

# Melting the data to long format
df_melted = df.melt('Year', var_name='Sector', value_name='Expenses')

# Pivot for cumulative sum to stack the sectors on top of each other
df_melted['Cumulative'] = df_melted.groupby('Year')['Expenses'].cumsum()

# Plot
plt.figure(figsize=(16, 8))
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]

# Loop to create the stacked area plot
for i, sector in enumerate(df_melted['Sector'].unique()):
    if i == 0:
        plt.fill_between(df['Year'], 0, df_melted[df_melted['Sector'] == sector]['Cumulative'], color=colors[i], label=sector)
    else:
        plt.fill_between(df['Year'], 
                         df_melted[df_melted['Sector'] == df_melted['Sector'].unique()[i-1]]['Cumulative'], 
                         df_melted[df_melted['Sector'] == sector]['Cumulative'], 
                         color=colors[i], label=sector)

# Annotating the last value of Healthcare for example
last_year_data = df_melted[df_melted['Year'] == df['Year'].max()]
healthcare_last_value = last_year_data[last_year_data['Sector'] == 'Healthcare']['Cumulative'].values[0]
plt.text(df['Year'].max(), healthcare_last_value - 500, "Healthcare", verticalalignment='center', horizontalalignment='center', color="white", fontsize=12)

# Customizing the plot
plt.title("Healthcare Expenses Over Time by Sector", fontsize=18)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Expenses (Million USD)", fontsize=14)
plt.legend(loc='upper left', fontsize=12)
sns.despine()
plt.show()