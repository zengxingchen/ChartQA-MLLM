
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Month': ['Jan-2021', 'Feb-2021', 'Mar-2021', 'Apr-2021', 'May-2021', 
              'Jun-2021', 'Jul-2021', 'Aug-2021', 'Sep-2021', 'Oct-2021',
              'Nov-2021', 'Dec-2021', 'Jan-2022', 'Feb-2022', 'Mar-2022',
              'Apr-2022', 'May-2022', 'Jun-2022', 'Jul-2022', 'Aug-2022',
              'Sep-2022', 'Oct-2022', 'Nov-2022', 'Dec-2022'],
    'Visitors': [500, 650, 700, 680, 720, 750, 800, 850, 900, 950,
                 1000, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500,
                 1550, 1600, 1650, 1700]
}

df = pd.DataFrame(data)

sns.set_theme(style="whitegrid")

plt.figure(figsize=(18, 10))
ax = sns.lineplot(data=df, x='Month', y='Visitors', color="#1f77b4")
ax.fill_between(df['Month'], df['Visitors'], color="#1f77b4", alpha=0.3)

for item in ax.get_xticklabels():
    item.set_rotation(45)

ax.set_title('Monthly Visitors to the Museum Over Two Years', fontsize=22)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Number of Visitors', fontsize=14)

ax.annotate('Post-Pandemic Reopening Surge', xy=('Jul-2021', 800), xytext=('Sep-2021', 900), fontsize=12,
            arrowprops=dict(facecolor='black', shrink=0.05))

plt.tight_layout()
plt.show()