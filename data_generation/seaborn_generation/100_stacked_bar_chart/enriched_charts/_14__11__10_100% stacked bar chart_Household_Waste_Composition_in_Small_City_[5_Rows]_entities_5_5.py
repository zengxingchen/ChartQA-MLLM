
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = [
    {'Year': 2019, 'Aerobic': '35%', 'Strength': '30%', 'Flexibility': '20%', 'Balance': '10%', 'Mindfulness': '5%'},
    {'Year': 2020, 'Aerobic': '40%', 'Strength': '25%', 'Flexibility': '15%', 'Balance': '15%', 'Mindfulness': '5%'},
    {'Year': 2021, 'Aerobic': '45%', 'Strength': '20%', 'Flexibility': '15%', 'Balance': '15%', 'Mindfulness': '5%'},
    {'Year': 2022, 'Aerobic': '50%', 'Strength': '15%', 'Flexibility': '10%', 'Balance': '20%', 'Mindfulness': '5%'},
    {'Year': 2023, 'Aerobic': '55%', 'Strength': '10%', 'Flexibility': '10%', 'Balance': '20%', 'Mindfulness': '5%'},
    {'Year': 2024, 'Aerobic': '60%', 'Strength': '10%', 'Flexibility': '10%', 'Balance': '15%', 'Mindfulness': '5%'}
]

df = pd.DataFrame(data)

for col in df.columns[1:]:
    df[col] = df[col].str.rstrip('%').astype('float') / 100

df_long = df.melt(id_vars='Year', var_name='Activity', value_name='Percentage')
df_long['Bottom'] = df_long.groupby('Year')['Percentage'].cumsum() - df_long['Percentage']

plt.figure(figsize=(12, 8))

colors = ['#4B8BBE', '#306998', '#FFE873', '#FFD43B', '#646464']

for i, activity in enumerate(df.columns[1:]):
    sns.barplot(
        data=df_long[df_long['Activity'] == activity],
        x='Year',
        y='Percentage',
        color=colors[i],
        label=activity,
        bottom=df_long[df_long['Activity'] == activity]['Bottom'],
        width=0.5
    )

plt.title('Trends in Physical Activities (2019-2024)', fontsize=16, pad=20)
plt.ylabel('Percentage (%)', fontsize=12)
plt.xlabel('Year', fontsize=12)

plt.legend(title='Activity', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()