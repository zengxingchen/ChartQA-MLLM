
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = {
    'Year': [i for i in range(2000, 2021)],
    'Science': [480 + i*10 for i in range(21)],
    'Technology': [500 + i*20 for i in range(21)],
    'Engineering': [460 + i*15 for i in range(21)],
    'Mathematics': [470 + i*10 for i in range(21)],
}
df = pd.DataFrame(data)

df_melted = df.melt('Year', var_name='Field', value_name='Enrollment')

df_melted['Cumulative'] = df_melted.groupby('Year')['Enrollment'].cumsum()

plt.figure(figsize=(18, 10))
colors = ["#D32F2F", "#1976D2", "#388E3C", "#FBC02D"]

for i, field in enumerate(df_melted['Field'].unique()):
    if i == 0:
        plt.fill_between(df['Year'], 0, df_melted[df_melted['Field'] == field]['Cumulative'], color=colors[i], label=field)
    else:
        plt.fill_between(df['Year'], 
                         df_melted[df_melted['Field'] == df_melted['Field'].unique()[i-1]]['Cumulative'], 
                         df_melted[df_melted['Field'] == field]['Cumulative'], 
                         color=colors[i], label=field)

last_year_data = df_melted[df_melted['Year'] == df['Year'].max()]
technology_last_value = last_year_data[last_year_data['Field'] == 'Technology']['Cumulative'].values[0]
plt.text(df['Year'].max(), technology_last_value - 100, "Technology", verticalalignment='center', horizontalalignment='center', color="black", fontsize=10)

plt.title("Enrollment in STEM Fields Over Time", fontsize=20)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Enrollment Numbers", fontsize=14)
plt.legend(loc='upper left')
sns.despine()
plt.show()