
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = [
    {'Year': 2019, 'Carbohydrates': '48%', 'Proteins': '22%', 'Fats': '18%', 'Fibers': '8%', 'Vitamins': '4%'},
    {'Year': 2020, 'Carbohydrates': '47%', 'Proteins': '23%', 'Fats': '18%', 'Fibers': '8%', 'Vitamins': '4%'},
    {'Year': 2021, 'Carbohydrates': '45%', 'Proteins': '25%', 'Fats': '18%', 'Fibers': '8%', 'Vitamins': '4%'},
    {'Year': 2022, 'Carbohydrates': '46%', 'Proteins': '24%', 'Fats': '18%', 'Fibers': '8%', 'Vitamins': '4%'},
    {'Year': 2023, 'Carbohydrates': '44%', 'Proteins': '26%', 'Fats': '18%', 'Fibers': '8%', 'Vitamins': '4%'}
]

df = pd.DataFrame(data)

for col in df.columns[1:]:
    df[col] = df[col].str.rstrip('%').astype('float') / 100

df_long = df.melt(id_vars='Year', var_name='Nutrient', value_name='Percentage')
df_long['Bottom'] = df_long.groupby('Year')['Percentage'].cumsum() - df_long['Percentage']

plt.figure(figsize=(10, 6))

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

for i, nutrient in enumerate(df.columns[1:]):
    sns.barplot(
        data=df_long[df_long['Nutrient'] == nutrient],
        x='Year',
        y='Percentage',
        color=colors[i],
        label=nutrient,
        bottom=df_long[df_long['Nutrient'] == nutrient]['Bottom'],
        width=0.5
    )

plt.title('Nutrient Distribution in Diets Over Years', fontsize=16)
plt.ylabel('Percentage (%)', fontsize=12)
plt.xlabel('Year', fontsize=12)

plt.legend(title='Nutrient', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()