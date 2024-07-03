
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Renewable Energy': [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210],
    'Non-Renewable Energy': [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310],
    'Nuclear Energy': [150, 140, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250]
}

df = pd.DataFrame(data)
df_melted = df.melt('Month', var_name='Energy Type', value_name='Production')

df_melted['Month'] = pd.Categorical(df_melted['Month'],
                                    categories=data['Month'],
                                    ordered=True)

plt.figure(figsize=(16, 10))

colors = ["#FF7F50", "#6A5ACD", "#FFD700"]

plt.stackplot(df['Month'], df.iloc[:, 1:].values.T, labels=df.columns[1:], colors=colors, alpha=0.8)

plt.title('Monthly Energy Production by Source', fontsize=20, loc='left', pad=20)
plt.ylabel('Energy Production (in GWh)', fontsize=16)
plt.xlabel('Month', fontsize=16)
plt.xticks(rotation=45)
plt.legend(title='Energy Type', loc='upper right')

for i, row in df.iterrows():
    total_production = row['Renewable Energy'] + row['Non-Renewable Energy'] + row['Nuclear Energy']
    plt.text(row['Month'], total_production, f'{total_production}', ha='center', va='bottom')

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.tight_layout()
plt.show()