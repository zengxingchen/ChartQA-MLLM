
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Data
data = {
    'Year': [i for i in range(2000, 2023)],
    'Technology': [1000 + 100 * i for i in range(23)],
    'Marketing': [800 + 50 * i for i in range(23)],
    'Sales': [700 + 50 * i for i in range(23)],
    'Customer Support': [400 + 50 * i for i in range(23)],
    'HR': [200 + 20 * i for i in range(23)],
}
df = pd.DataFrame(data)

# Melting the data to long format
df_melted = df.melt('Year', var_name='Sector', value_name='Expenses')

# Pivot for cumulative sum to stack the sectors on top of each other
df_melted['Cumulative'] = df_melted.groupby('Year')['Expenses'].cumsum()

# Plot
plt.figure(figsize=(18, 10))
colors = ["#e41a1c", "#377eb8", "#4daf4a", "#984ea3", "#ff7f00"]

# Loop to create the stacked area plot
for i, sector in enumerate(df_melted['Sector'].unique()):
    if i == 0:
        plt.fill_between(df['Year'], 0, df_melted[df_melted['Sector'] == sector]['Cumulative'], color=colors[i], label=sector)
    else:
        plt.fill_between(df['Year'], 
                         df_melted[df_melted['Sector'] == df_melted['Sector'].unique()[i-1]]['Cumulative'], 
                         df_melted[df_melted['Sector'] == sector]['Cumulative'], 
                         color=colors[i], label=sector)

# Annotating the last value of Technology for example
last_year_data = df_melted[df_melted['Year'] == df['Year'].max()]
technology_last_value = last_year_data[last_year_data['Sector'] == 'Technology']['Cumulative'].values[0]
plt.text(df['Year'].max(), technology_last_value - 150, "Technology", verticalalignment='center', horizontalalignment='center', color="white", fontsize=12)

# Customizing the plot
plt.title("Business Expenses Over Time by Sector", fontsize=20)
plt.xlabel("Year", fontsize=16)
plt.ylabel("Expenses (Million USD)", fontsize=16)
plt.legend(loc='upper left', fontsize=14)
sns.despine()
plt.show()