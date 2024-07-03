
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = [
    {'Day': 'Monday', 'Fruits': '20%', 'Vegetables': '25%', 'Grains': '15%', 'Proteins': '30%', 'Dairy': '10%'},
    {'Day': 'Tuesday', 'Fruits': '18%', 'Vegetables': '30%', 'Grains': '15%', 'Proteins': '27%', 'Dairy': '10%'},
    {'Day': 'Wednesday', 'Fruits': '22%', 'Vegetables': '28%', 'Grains': '13%', 'Proteins': '27%', 'Dairy': '10%'},
    {'Day': 'Thursday', 'Fruits': '25%', 'Vegetables': '27%', 'Grains': '15%', 'Proteins': '23%', 'Dairy': '10%'},
    {'Day': 'Friday', 'Fruits': '28%', 'Vegetables': '30%', 'Grains': '12%', 'Proteins': '20%', 'Dairy': '10%'},
    {'Day': 'Saturday', 'Fruits': '30%', 'Vegetables': '35%', 'Grains': '10%', 'Proteins': '20%', 'Dairy': '5%'},
    {'Day': 'Sunday', 'Fruits': '27%', 'Vegetables': '32%', 'Grains': '15%', 'Proteins': '16%', 'Dairy': '10%'}
]

df = pd.DataFrame(data)

for col in df.columns:
    if col != 'Day':
        df[col] = df[col].str.rstrip('%').astype('float') / 100

df.set_index('Day', inplace=True)
df.sort_index(inplace=True)

cumsum_df = df.cumsum(axis=1)

fig, ax = plt.subplots(figsize=(10, 12))

colors = ['#4daf4a', '#377eb8', '#ff7f00', '#984ea3', '#e41a1c']
width = 0.8
for i, col in enumerate(df.columns):
    ax.bar(df.index, df[col], bottom=cumsum_df[col] - df[col], color=colors[i], edgecolor='white', width=width)

plt.xticks(rotation=90)
plt.yticks(ticks=[0, 0.2, 0.4, 0.6, 0.8, 1], labels=['0%', '20%', '40%', '60%', '80%', '100%'])
plt.xlabel('Day of the Week')
plt.ylabel('Percentage')
plt.title('Weekly Food Consumption Breakdown', pad=20)
plt.legend(df.columns, bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

plt.show()