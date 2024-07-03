
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Category': 'Rock', 'Live Concerts': '35%', 'Albums': '25%', 'Music Videos': '15%', 'Radio Shows': '10%', 'Podcasts': '5%', 'Documentaries': '10%'},
    {'Category': 'Jazz', 'Live Concerts': '20%', 'Albums': '30%', 'Music Videos': '20%', 'Radio Shows': '10%', 'Podcasts': '10%', 'Documentaries': '10%'},
    {'Category': 'Classical', 'Live Concerts': '15%', 'Albums': '25%', 'Music Videos': '25%', 'Radio Shows': '15%', 'Podcasts': '10%', 'Documentaries': '10%'},
    {'Category': 'Hip Hop', 'Live Concerts': '25%', 'Albums': '20%', 'Music Videos': '20%', 'Radio Shows': '15%', 'Podcasts': '10%', 'Documentaries': '10%'},
    {'Category': 'Pop', 'Live Concerts': '30%', 'Albums': '25%', 'Music Videos': '20%', 'Radio Shows': '10%', 'Podcasts': '10%', 'Documentaries': '5%'},
    {'Category': 'Country', 'Live Concerts': '25%', 'Albums': '30%', 'Music Videos': '15%', 'Radio Shows': '10%', 'Podcasts': '10%', 'Documentaries': '10%'},
    {'Category': 'Electronic', 'Live Concerts': '30%', 'Albums': '20%', 'Music Videos': '25%', 'Radio Shows': '10%', 'Podcasts': '5%', 'Documentaries': '10%'},
    {'Category': 'Reggae', 'Live Concerts': '20%', 'Albums': '25%', 'Music Videos': '20%', 'Radio Shows': '10%', 'Podcasts': '15%', 'Documentaries': '10%'},
    {'Category': 'Blues', 'Live Concerts': '15%', 'Albums': '30%', 'Music Videos': '20%', 'Radio Shows': '10%', 'Podcasts': '15%', 'Documentaries': '10%'},
    {'Category': 'Folk', 'Live Concerts': '25%', 'Albums': '20%', 'Music Videos': '20%', 'Radio Shows': '15%', 'Podcasts': '10%', 'Documentaries': '10%'}
]

df = pd.DataFrame(data)
df = df.set_index('Category')
df = df.applymap(lambda x: int(x.replace('%', '')))

cumulative_sum = df.cumsum(axis=1)

colors = ['#4daf4a', '#377eb8', '#ff7f00', '#984ea3', '#e41a1c', '#ffff33']

fig, ax = plt.subplots(figsize=(18, 14))

bottom = None

for column, color in zip(df.columns, colors):
    ax.bar(df.index, df[column], bottom=bottom, label=column, color=color, width=0.7)
    bottom = cumulative_sum[column]

ax.legend(title='Resources', bbox_to_anchor=(1.05, 1), loc='upper left')

ax.set_ylabel('Percentage')
ax.set_xlabel('Genres')
ax.set_title('Resource Distribution Across Various Music & Performing Arts Genres', pad=40)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()