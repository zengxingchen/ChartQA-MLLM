
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = [
    {'Year': 2018, 'Basketball': '22%', 'Football': '18%', 'Running': '25%', 'Swimming': '20%', 'Cycling': '15%'},
    {'Year': 2019, 'Basketball': '20%', 'Football': '22%', 'Running': '23%', 'Swimming': '18%', 'Cycling': '17%'},
    {'Year': 2020, 'Basketball': '23%', 'Football': '21%', 'Running': '20%', 'Swimming': '22%', 'Cycling': '14%'},
    {'Year': 2021, 'Basketball': '21%', 'Football': '20%', 'Running': '24%', 'Swimming': '19%', 'Cycling': '16%'},
    {'Year': 2022, 'Basketball': '19%', 'Football': '23%', 'Running': '22%', 'Swimming': '20%', 'Cycling': '16%'}
]

df = pd.DataFrame(data)

def percent_to_float(s):
    return float(s.strip('%')) / 100

for col in df.columns[1:]:
    df[col] = df[col].apply(percent_to_float)

df_long = df.melt(id_vars='Year', var_name='Sport', value_name='Percentage')
df_long.sort_values(by=['Year', 'Sport'], inplace=True)

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

fig, ax = plt.subplots(figsize=(12, 8))

bottom = pd.Series([0.0] * len(df['Year']))

for index, (name, group) in enumerate(df_long.groupby('Sport')):
    sns.barplot(
        x='Year', y='Percentage', data=group, 
        label=name, color=colors[index], ci=None, edgecolor='black', linewidth=0.7
    )
    bottom += group['Percentage'].values

ax.set_ylim(0, 1)
ax.set_ylabel('Percentage')
ax.set_xlabel('Year')
ax.set_title('Percentage Distribution of Sports Activities (2018-2022)', pad=20)

plt.legend(title='Sport', loc='upper right', bbox_to_anchor=(1.2, 1))

ax.yaxis.set_major_formatter(plt.FuncFormatter('{:.0%}'.format))

plt.tight_layout()
plt.show()