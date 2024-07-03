
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = [
    {'Day': 'Monday', 'Pop': '22%', 'Rock': '28%', 'Jazz': '20%', 'Classical': '15%', 'Hip-Hop': '10%', 'Electronic': '5%'},
    {'Day': 'Tuesday', 'Pop': '24%', 'Rock': '20%', 'Jazz': '22%', 'Classical': '18%', 'Hip-Hop': '10%', 'Electronic': '6%'},
    {'Day': 'Wednesday', 'Pop': '20%', 'Rock': '30%', 'Jazz': '18%', 'Classical': '15%', 'Hip-Hop': '10%', 'Electronic': '7%'},
    {'Day': 'Thursday', 'Pop': '26%', 'Rock': '18%', 'Jazz': '22%', 'Classical': '15%', 'Hip-Hop': '10%', 'Electronic': '9%'},
    {'Day': 'Friday', 'Pop': '25%', 'Rock': '22%', 'Jazz': '20%', 'Classical': '17%', 'Hip-Hop': '11%', 'Electronic': '5%'},
    {'Day': 'Saturday', 'Pop': '28%', 'Rock': '20%', 'Jazz': '18%', 'Classical': '18%', 'Hip-Hop': '10%', 'Electronic': '6%'},
    {'Day': 'Sunday', 'Pop': '27%', 'Rock': '25%', 'Jazz': '17%', 'Classical': '15%', 'Hip-Hop': '9%', 'Electronic': '7%'}
]

df = pd.DataFrame(data)

for col in df.columns:
    if col != 'Day':
        df[col] = df[col].str.rstrip('%').astype('float') / 100

df.set_index('Day', inplace=True)
df.sort_index(inplace=True)

cumsum_df = df.cumsum(axis=1)

fig, ax = plt.subplots(figsize=(10, 14))

colors = ['#FF5733', '#33FF57', '#3357FF', '#F333FF', '#FF33A1', '#33FFF6']
width = 0.7
for i, col in enumerate(df.columns):
    ax.barh(df.index, df[col], left=cumsum_df[col] - df[col], color=colors[i], edgecolor='white', height=width)

plt.xticks(ticks=[0, 0.2, 0.4, 0.6, 0.8, 1], labels=['0%', '20%', '40%', '60%', '80%', '100%'])
plt.xlabel('Percentage')
plt.ylabel('Day of the Week')
plt.title('Daily Music Genre Preferences', pad=20)
plt.legend(df.columns, bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

plt.show()