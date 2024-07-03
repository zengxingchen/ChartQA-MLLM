
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Month': ['Jan-2021', 'Feb-2021', 'Mar-2021', 'Apr-2021', 'May-2021', 
              'Jun-2021', 'Jul-2021', 'Aug-2021', 'Sep-2021', 'Oct-2021',
              'Nov-2021', 'Dec-2021', 'Jan-2022', 'Feb-2022', 'Mar-2022',
              'Apr-2022', 'May-2022', 'Jun-2022', 'Jul-2022', 'Aug-2022',
              'Sep-2022', 'Oct-2022', 'Nov-2022', 'Dec-2022'],
    'Revenue': [1200, 1350, 1400, 1300, 1500, 1600, 1550, 1700, 1750, 1800,
                1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800,
                2900, 3000, 3100, 3200]
}

df = pd.DataFrame(data)

sns.set_theme(style="whitegrid")

plt.figure(figsize=(16, 8))
ax = sns.lineplot(data=df, x='Month', y='Revenue', color="#FF5733")
ax.fill_between(df['Month'], df['Revenue'], color="#FF5733", alpha=0.4)

for item in ax.get_xticklabels():
    item.set_rotation(45)

ax.set_title('Monthly Revenue of Online Store Over Two Years', fontsize=22)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Revenue (in USD)', fontsize=14)

ax.annotate('Holiday Season Sales Peak', xy=('Dec-2021', 2000), xytext=('Feb-2022', 2200), fontsize=12,
            arrowprops=dict(facecolor='black', shrink=0.05))

plt.tight_layout()
plt.show()