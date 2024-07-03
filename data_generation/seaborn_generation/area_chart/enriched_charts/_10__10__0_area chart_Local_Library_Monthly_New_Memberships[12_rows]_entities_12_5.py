
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Month': ['Jan-2021', 'Feb-2021', 'Mar-2021', 'Apr-2021', 'May-2021', 
              'Jun-2021', 'Jul-2021', 'Aug-2021', 'Sep-2021', 'Oct-2021',
              'Nov-2021', 'Dec-2021', 'Jan-2022', 'Feb-2022', 'Mar-2022',
              'Apr-2022', 'May-2022', 'Jun-2022', 'Jul-2022', 'Aug-2022',
              'Sep-2022', 'Oct-2022', 'Nov-2022', 'Dec-2022'],
    'Visitors': [350, 400, 420, 380, 450, 470, 480, 490, 510, 530,
                 550, 570, 600, 620, 650, 670, 700, 730, 750, 780,
                 800, 820, 850, 870]
}

df = pd.DataFrame(data)

sns.set_theme(style="whitegrid")

plt.figure(figsize=(14, 7))
ax = sns.lineplot(data=df, x='Month', y='Visitors', color="#1E90FF")
ax.fill_between(df['Month'], df['Visitors'], color="#1E90FF", alpha=0.3)

for item in ax.get_xticklabels():
    item.set_rotation(45)

ax.set_title('Monthly Museum Visitors Over Two Years', fontsize=20)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Visitors', fontsize=12)

ax.annotate('Reopening after lockdown', xy=('Jul-2021', 480), xytext=('Sep-2021', 510), fontsize=12,
            arrowprops=dict(facecolor='black', shrink=0.05))

plt.tight_layout()
plt.show()