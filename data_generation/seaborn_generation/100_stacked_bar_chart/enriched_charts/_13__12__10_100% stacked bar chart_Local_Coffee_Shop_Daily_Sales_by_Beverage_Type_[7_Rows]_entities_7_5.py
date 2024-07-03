
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = [
    {'Day': 'Monday', 'Investment': '15%', 'Revenue': '25%', 'Cost': '20%', 'Profit': '30%', 'Loss': '10%'},
    {'Day': 'Tuesday', 'Investment': '20%', 'Revenue': '30%', 'Cost': '15%', 'Profit': '25%', 'Loss': '10%'},
    {'Day': 'Wednesday', 'Investment': '18%', 'Revenue': '28%', 'Cost': '17%', 'Profit': '27%', 'Loss': '10%'},
    {'Day': 'Thursday', 'Investment': '22%', 'Revenue': '27%', 'Cost': '18%', 'Profit': '23%', 'Loss': '10%'},
    {'Day': 'Friday', 'Investment': '25%', 'Revenue': '30%', 'Cost': '20%', 'Profit': '15%', 'Loss': '10%'},
    {'Day': 'Saturday', 'Investment': '30%', 'Revenue': '35%', 'Cost': '25%', 'Profit': '5%', 'Loss': '5%'},
    {'Day': 'Sunday', 'Investment': '28%', 'Revenue': '32%', 'Cost': '22%', 'Profit': '8%', 'Loss': '10%'}
]

df = pd.DataFrame(data)

for col in df.columns:
    if col != 'Day':
        df[col] = df[col].str.rstrip('%').astype('float') / 100

df.set_index('Day', inplace=True)
df.sort_index(inplace=True)

cumsum_df = df.cumsum(axis=1)

fig, ax = plt.subplots(figsize=(12, 8))

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
width = 0.6
for i, col in enumerate(df.columns):
    ax.bar(df.index, df[col], bottom=cumsum_df[col] - df[col], color=colors[i], edgecolor='white', width=width)

plt.xticks(rotation=0)
plt.yticks(ticks=[0, 0.2, 0.4, 0.6, 0.8, 1], labels=['0%', '20%', '40%', '60%', '80%', '100%'])
plt.xlabel('Day of the Week')
plt.ylabel('Percentage')
plt.title('Weekly Financial Overview', pad=20)
plt.legend(df.columns, bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

plt.show()