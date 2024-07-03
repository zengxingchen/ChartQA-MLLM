
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Month': 'January', 'Protein Intake (g)': '60', 'Carbohydrate Intake (g)': '120', 'Fat Intake (g)': '30'},
    {'Month': 'February', 'Protein Intake (g)': '70', 'Carbohydrate Intake (g)': '110', 'Fat Intake (g)': '40'},
    {'Month': 'March', 'Protein Intake (g)': '65', 'Carbohydrate Intake (g)': '115', 'Fat Intake (g)': '35'},
    {'Month': 'April', 'Protein Intake (g)': '80', 'Carbohydrate Intake (g)': '130', 'Fat Intake (g)': '50'},
    {'Month': 'May', 'Protein Intake (g)': '75', 'Carbohydrate Intake (g)': '125', 'Fat Intake (g)': '45'},
    {'Month': 'June', 'Protein Intake (g)': '85', 'Carbohydrate Intake (g)': '140', 'Fat Intake (g)': '55'},
    {'Month': 'July', 'Protein Intake (g)': '90', 'Carbohydrate Intake (g)': '135', 'Fat Intake (g)': '60'},
    {'Month': 'August', 'Protein Intake (g)': '95', 'Carbohydrate Intake (g)': '150', 'Fat Intake (g)': '65'}
]

df = pd.DataFrame(data)
for col in df.columns[1:]:
    df[col] = df[col].astype('float')

df_long = df.melt(id_vars='Month', var_name='Nutrient', value_name='Intake')

pivot_df = df_long.pivot(index='Month', columns='Nutrient', values='Intake')

colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
pivot_df.plot(kind='bar', stacked=True, color=colors, figsize=(12, 8), width=0.85)

plt.title('Monthly Nutrient Intake', pad=20)
plt.xlabel('Month', labelpad=15)
plt.ylabel('Intake (g)', labelpad=15)
plt.legend(title='Nutrient', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()