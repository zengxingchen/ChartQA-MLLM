
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = [
    {'Category': 'Rock', 'Monday': 0.22, 'Tuesday': 0.24, 'Wednesday': 0.18, 'Thursday': 0.20, 'Friday': 0.19, 'Saturday': 0.30, 'Sunday': 0.27},
    {'Category': 'Pop', 'Monday': 0.18, 'Tuesday': 0.22, 'Wednesday': 0.20, 'Thursday': 0.21, 'Friday': 0.22, 'Saturday': 0.19, 'Sunday': 0.20},
    {'Category': 'Jazz', 'Monday': 0.15, 'Tuesday': 0.16, 'Wednesday': 0.20, 'Thursday': 0.14, 'Friday': 0.16, 'Saturday': 0.13, 'Sunday': 0.16},
    {'Category': 'Classical', 'Monday': 0.17, 'Tuesday': 0.14, 'Wednesday': 0.22, 'Thursday': 0.18, 'Friday': 0.20, 'Saturday': 0.16, 'Sunday': 0.17},
    {'Category': 'Hip-Hop', 'Monday': 0.12, 'Tuesday': 0.10, 'Wednesday': 0.08, 'Thursday': 0.13, 'Friday': 0.10, 'Saturday': 0.11, 'Sunday': 0.09},
    {'Category': 'Electronic', 'Monday': 0.16, 'Tuesday': 0.14, 'Wednesday': 0.12, 'Thursday': 0.14, 'Friday': 0.13, 'Saturday': 0.11, 'Sunday': 0.11}
]

df = pd.DataFrame(data)
df.set_index('Category', inplace=True)
df = df.T

cumsum_df = df.cumsum(axis=1)

fig, ax = plt.subplots(figsize=(10, 14))

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFF6', '#FF8C33']
width = 0.6
for i, col in enumerate(df.columns):
    ax.barh(df.index, df[col], left=cumsum_df[col] - df[col], color=colors[i], edgecolor='white', height=width)

plt.xticks(ticks=[0, 0.2, 0.4, 0.6, 0.8, 1], labels=['0%', '20%', '40%', '60%', '80%', '100%'])
plt.xlabel('Percentage')
plt.ylabel('Day of the Week')
plt.title('Distribution of Music Genres Played Over a Week', pad=20)
plt.legend(df.columns, bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()