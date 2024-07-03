
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = [
    {'Year': 2018, 'Transportation': '30%', 'Industry': '20%', 'Residential': '20%', 'Commercial': '15%', 'Agriculture': '15%'},
    {'Year': 2019, 'Transportation': '25%', 'Industry': '30%', 'Residential': '15%', 'Commercial': '20%', 'Agriculture': '10%'},
    {'Year': 2020, 'Transportation': '28%', 'Industry': '25%', 'Residential': '18%', 'Commercial': '17%', 'Agriculture': '12%'},
    {'Year': 2021, 'Transportation': '27%', 'Industry': '22%', 'Residential': '20%', 'Commercial': '18%', 'Agriculture': '13%'},
    {'Year': 2022, 'Transportation': '26%', 'Industry': '23%', 'Residential': '21%', 'Commercial': '19%', 'Agriculture': '11%'}
]

df = pd.DataFrame(data)

def percent_to_float(s):
    return float(s.strip('%')) / 100

for col in df.columns[1:]:
    df[col] = df[col].apply(percent_to_float)

df_long = df.melt(id_vars='Year', var_name='Sector', value_name='Percentage')
df_long.sort_values(by=['Year', 'Sector'], inplace=True)

colors = ['#003f5c', '#58508d', '#bc5090', '#ff6361', '#ffa600']

fig, ax = plt.subplots(figsize=(10, 6))

bottom = pd.Series([0.0, 0.0, 0.0, 0.0, 0.0])

for index, (name, group) in enumerate(df_long.groupby('Sector')):
    sns.barplot(
        x='Year', y='Percentage', data=group, 
        label=name, color=colors[index], ci=None, edgecolor='black', linewidth=0.5
    )
    bottom += group['Percentage'].values

ax.set_ylim(0, 1)
ax.set_ylabel('Percentage')
ax.set_xlabel('Year')
ax.set_title('100% Stacked Bar Chart of Resource Allocation by Sector')

plt.legend(title='Sector', loc='upper left', bbox_to_anchor=(1, 1))

ax.yaxis.set_major_formatter(plt.FuncFormatter('{:.0%}'.format))

plt.tight_layout()
plt.show()