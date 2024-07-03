
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = [
    {'Year': 2018, 'Primary_School': 0.35, 'High_School': 0.25, 'Undergraduate': 0.2, 'Postgraduate': 0.1, 'Other': 0.1},
    {'Year': 2019, 'Primary_School': 0.32, 'High_School': 0.28, 'Undergraduate': 0.22, 'Postgraduate': 0.12, 'Other': 0.06},
    {'Year': 2020, 'Primary_School': 0.34, 'High_School': 0.27, 'Undergraduate': 0.23, 'Postgraduate': 0.1, 'Other': 0.06},
    {'Year': 2021, 'Primary_School': 0.31, 'High_School': 0.3, 'Undergraduate': 0.21, 'Postgraduate': 0.12, 'Other': 0.06},
    {'Year': 2022, 'Primary_School': 0.33, 'High_School': 0.29, 'Undergraduate': 0.2, 'Postgraduate': 0.1, 'Other': 0.08}
]

df = pd.DataFrame(data)
df_long = df.melt(id_vars='Year', var_name='Education_Level', value_name='Percentage')
df_long.sort_values(by=['Year', 'Education_Level'], inplace=True)

colors = ['#d4a6c8', '#a6bddb', '#b2df8a', '#fb9a99', '#fdbf6f']

fig, ax = plt.subplots(figsize=(12, 8))

bottom = pd.Series([0.0] * df['Year'].nunique())

for index, (name, group) in enumerate(df_long.groupby('Education_Level')):
    sns.barplot(
        x='Year', y='Percentage', data=group, 
        label=name, color=colors[index], ci=None, edgecolor='black', linewidth=0.5
    )
    bottom += group['Percentage'].values

ax.set_ylim(0, 1)
ax.set_ylabel('Percentage')
ax.set_xlabel('Year')
ax.set_title('Distribution of Education Levels Over Years')

plt.legend(title='Education Level', loc='upper left', bbox_to_anchor=(1, 1))
ax.yaxis.set_major_formatter(plt.FuncFormatter('{:.0%}'.format))

plt.tight_layout()
plt.show()