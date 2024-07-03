
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 
              'September', 'October', 'November', 'December'],
    'Meditation': [8000, 9500, 10200, 12000, 13000, 13500, 14500, 15000, 15500, 16000, 16500, 17000],
    'Exercise': [12000, 13000, 12500, 14000, 14500, 15000, 16000, 16500, 17000, 17500, 18000, 18500],
    'Yoga': [7000, 8500, 9200, 10500, 11000, 11500, 12500, 13000, 13500, 14000, 14500, 15000]
}

df = pd.DataFrame(data)

df['Month'] = pd.Categorical(df['Month'], 
                             categories=['January', 'February', 'March', 'April', 'May', 'June', 
                                         'July', 'August', 'September', 'October', 'November', 'December'],
                             ordered=True)

plt.figure(figsize=(18, 14))

sns.set_theme(style="whitegrid")
pal = ['#007ACC', '#FF5733', '#33FF57']

ax = df.set_index('Month').plot(kind='area', stacked=True, color=pal)

df['Total'] = df['Meditation'] + df['Exercise'] + df['Yoga']
for idx, total in enumerate(df['Total']):
    ax.text(idx, total, str(total), va='bottom', ha='center')

ax.set_title('Monthly Participation in Health Activities', fontsize=20, pad=20)
ax.set_ylabel('Number of Participants', fontsize=16)
ax.set_xlabel('Month', fontsize=16)

plt.xticks(rotation=45)

plt.legend(title='Activity', loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()