
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Month": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
    "Income": [4500, 4700, 4900, 5300, 5500, 5800, 6000, 6200, 6500, 6800, 7000, 7200],
    "Expenses": [3200, 3000, 3500, 3300, 3100, 3600, 3400, 3800, 4000, 3700, 4200, 3900],
    "Investments": [1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400],
    "Savings": [600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.2

indices = df.index
r1 = range(len(indices))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]
r4 = [x + bar_width for x in r3]

ax.bar(r1, df['Income'], color='#1E90FF', edgecolor='white', width=bar_width, label='Income')
ax.bar(r2, df['Expenses'], color='#32CD32', edgecolor='white', width=bar_width, label='Expenses')
ax.bar(r3, df['Investments'], color='#FFD700', edgecolor='white', width=bar_width, label='Investments')
ax.bar(r4, df['Savings'], color='#FF4500', edgecolor='white', width=bar_width, label='Savings')

ax.set_ylabel('Amount ($)', fontsize=15)
ax.set_xlabel('Month', fontsize=15)
ax.set_title('Monthly Financial Overview', fontsize=18, pad=20)

ax.set_xticks([r + bar_width for r in range(len(r1))])
ax.set_xticklabels(df['Month'], rotation=45, ha='right')
ax.set_ylim(2500, 7500)

ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()