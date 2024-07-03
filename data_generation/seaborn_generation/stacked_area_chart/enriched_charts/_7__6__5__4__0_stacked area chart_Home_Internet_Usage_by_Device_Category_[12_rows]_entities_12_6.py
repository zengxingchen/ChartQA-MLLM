
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Books': [52, 57, 62, 68, 73, 78, 83, 88, 93, 98, 103, 108],
    'Music': [110, 112, 118, 123, 128, 133, 138, 143, 148, 153, 158, 163],
    'Games': [155, 157, 162, 167, 172, 177, 182, 187, 192, 197, 202, 207],
    'Sports': [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105]
}

df = pd.DataFrame(data)
df_melted = df.melt('Month', var_name='Leisure Activity', value_name='Hours Spent')

df_melted['Month'] = pd.Categorical(df_melted['Month'],
                                    categories=data['Month'],
                                    ordered=True)

plt.figure(figsize=(20, 14))

colors = ["#FF5733", "#33FF57", "#3357FF", "#FF33A1"]

plt.stackplot(df['Month'], df.iloc[:, 1:].values.T, labels=df.columns[1:], colors=colors, alpha=0.8)

plt.title('Monthly Leisure Time Allocation in Hours', fontsize=24, loc='center', pad=30)
plt.ylabel('Hours Spent', fontsize=20)
plt.xlabel('Month', fontsize=20)
plt.xticks(rotation=45, fontsize=14)
plt.yticks(fontsize=14)
plt.legend(title='Leisure Activity', loc='upper left', fontsize=14, title_fontsize=16)

for i, row in df.iterrows():
    total_hours = row['Books'] + row['Music'] + row['Games'] + row['Sports']
    plt.text(row['Month'], total_hours, f'{total_hours}', ha='center', va='bottom', fontsize=12)

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.tight_layout()
plt.show()