
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Books': [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105],
    'Music': [100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155],
    'Games': [150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205]
}

df = pd.DataFrame(data)
df_melted = df.melt('Month', var_name='Leisure Activity', value_name='Hours Spent')

df_melted['Month'] = pd.Categorical(df_melted['Month'],
                                    categories=data['Month'],
                                    ordered=True)

plt.figure(figsize=(18, 12))

colors = ["#4CAF50", "#2196F3", "#FFC107"]

plt.stackplot(df['Month'], df.iloc[:, 1:].values.T, labels=df.columns[1:], colors=colors, alpha=0.8)

plt.title('Monthly Leisure Time Allocation', fontsize=22, loc='center', pad=20)
plt.ylabel('Hours Spent', fontsize=18)
plt.xlabel('Month', fontsize=18)
plt.xticks(rotation=45)
plt.legend(title='Leisure Activity', loc='upper left')

for i, row in df.iterrows():
    total_hours = row['Books'] + row['Music'] + row['Games']
    plt.text(row['Month'], total_hours, f'{total_hours}', ha='center', va='bottom')

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.tight_layout()
plt.show()