
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Month': ['Jan-2021', 'Feb-2021', 'Mar-2021', 'Apr-2021', 'May-2021', 
              'Jun-2021', 'Jul-2021', 'Aug-2021', 'Sep-2021', 'Oct-2021',
              'Nov-2021', 'Dec-2021', 'Jan-2022', 'Feb-2022', 'Mar-2022',
              'Apr-2022', 'May-2022', 'Jun-2022', 'Jul-2022', 'Aug-2022',
              'Sep-2022', 'Oct-2022', 'Nov-2022', 'Dec-2022'],
    'Participants': [150, 200, 220, 180, 250, 270, 300, 320, 350, 370,
                     390, 410, 450, 480, 500, 530, 560, 590, 620, 650,
                     680, 710, 740, 770]
}

df = pd.DataFrame(data)

sns.set_theme(style="whitegrid")

plt.figure(figsize=(16, 8))
ax = sns.lineplot(data=df, x='Month', y='Participants', color="#FF6347")
ax.fill_between(df['Month'], df['Participants'], color="#FF6347", alpha=0.3)

for item in ax.get_xticklabels():
    item.set_rotation(45)

ax.set_title('Monthly Fitness Class Participants Over Two Years', fontsize=20)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Participants', fontsize=14)

ax.annotate('New Year Resolution Spike', xy=('Jan-2022', 450), xytext=('Mar-2022', 500), fontsize=12,
            arrowprops=dict(facecolor='black', shrink=0.05))

plt.tight_layout()
plt.show()