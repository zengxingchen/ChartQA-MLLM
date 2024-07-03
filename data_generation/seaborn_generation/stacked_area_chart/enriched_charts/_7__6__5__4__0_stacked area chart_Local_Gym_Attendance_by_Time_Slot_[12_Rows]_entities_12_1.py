
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Streaming': [100, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220],
    'Books': [150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260],
    'Subscriptions': [200, 220, 250, 270, 290, 310, 320, 330, 340, 350, 360, 370],
    'Gadgets': [120, 140, 130, 150, 160, 180, 190, 200, 220, 230, 240, 250],
}

df = pd.DataFrame(data)

palette = ["#5A9BD4", "#FAA43A", "#60BD68", "#F17CB0"]

df_melted = df.melt('Month', var_name='Expense Type', value_name='Amount')

plt.figure(figsize=(24, 14))

sns.set_style("whitegrid")
df.set_index('Month').plot(kind='area', stacked=True, color=palette, alpha=0.8, figsize=(24, 14))

plt.title('Monthly Entertainment Expense Analysis', fontsize=26, pad=35)
plt.xlabel('Month', fontsize=20)
plt.ylabel('Amount ($)', fontsize=20)
plt.xticks(rotation=45)
plt.legend(title='Expense Types', loc='upper left')

for i, expense in enumerate(df.columns[1:]):
    y = df[expense].cumsum() - (0.5 * df[expense])
    for x, value in enumerate(y):
        if x == len(df) - 1:
            plt.text(x, value, f'{expense}', fontsize=16, ha='left', va='center')

plt.tight_layout()
plt.show()