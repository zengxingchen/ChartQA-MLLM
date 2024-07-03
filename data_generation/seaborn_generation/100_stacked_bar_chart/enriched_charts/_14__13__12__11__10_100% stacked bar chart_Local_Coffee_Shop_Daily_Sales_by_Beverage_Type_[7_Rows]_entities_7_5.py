
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = [
    {'Day': 'Monday', 'Action': 0.20, 'Comedy': 0.25, 'Drama': 0.15, 'Romance': 0.10, 'Sci-Fi': 0.20, 'Documentary': 0.10},
    {'Day': 'Tuesday', 'Action': 0.18, 'Comedy': 0.22, 'Drama': 0.18, 'Romance': 0.12, 'Sci-Fi': 0.20, 'Documentary': 0.10},
    {'Day': 'Wednesday', 'Action': 0.25, 'Comedy': 0.20, 'Drama': 0.15, 'Romance': 0.10, 'Sci-Fi': 0.18, 'Documentary': 0.12},
    {'Day': 'Thursday', 'Action': 0.22, 'Comedy': 0.18, 'Drama': 0.20, 'Romance': 0.10, 'Sci-Fi': 0.15, 'Documentary': 0.15},
    {'Day': 'Friday', 'Action': 0.20, 'Comedy': 0.20, 'Drama': 0.15, 'Romance': 0.18, 'Sci-Fi': 0.12, 'Documentary': 0.15},
    {'Day': 'Saturday', 'Action': 0.15, 'Comedy': 0.25, 'Drama': 0.20, 'Romance': 0.12, 'Sci-Fi': 0.18, 'Documentary': 0.10},
    {'Day': 'Sunday', 'Action': 0.18, 'Comedy': 0.15, 'Drama': 0.22, 'Romance': 0.13, 'Sci-Fi': 0.20, 'Documentary': 0.12}
]

df = pd.DataFrame(data)
df.set_index('Day', inplace=True)
df.sort_index(inplace=True)
cumsum_df = df.cumsum(axis=1)

fig, ax = plt.subplots(figsize=(12, 8))
colors = ['#FF6347', '#4682B4', '#3CB371', '#FFD700', '#9370DB', '#FF8C00']
width = 0.8

for i, col in enumerate(df.columns):
    ax.bar(df.index, df[col], bottom=cumsum_df[col] - df[col], color=colors[i], edgecolor='white', width=width)

plt.xticks(rotation=0)
plt.yticks(ticks=[0, 0.2, 0.4, 0.6, 0.8, 1], labels=['0%', '20%', '40%', '60%', '80%', '100%'])
plt.xlabel('Day of the Week')
plt.ylabel('Percentage')
plt.title('Daily Popularity of Movie Genres', pad=20)
plt.legend(df.columns, bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()