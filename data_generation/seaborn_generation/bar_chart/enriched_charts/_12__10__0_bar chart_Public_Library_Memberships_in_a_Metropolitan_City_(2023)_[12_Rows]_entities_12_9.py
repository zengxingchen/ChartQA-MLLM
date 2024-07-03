
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Topic': ['Classical Music', 'Jazz Music', 'Pop Music', 'Rock Music', 'Hip Hop', 'Electronic Dance Music', 
              'Country Music', 'Reggae Music', 'Blues Music', 'Latin Music', 'Folk Music', 'Opera', 
              'Indie Music', 'K-Pop', 'Metal Music', 'R&B', 'Gospel Music', 'Soul Music', 'Punk Rock', 'Alternative Rock'],
    'Popularity': [78, 85, 92, 88, 80, 95, 76, 82, 90, 84, 87, 89, 77, 91, 86, 79, 81, 93, 83, 75]
}

df = pd.DataFrame(data)

sns.set_theme(style="whitegrid")

plt.figure(figsize=(12, 8))
barplot = sns.barplot(y='Topic', x='Popularity', data=df, color="#1f77b4", ci=None)

barplot.set(xlim=(0, 100))
sns.despine(left=True, bottom=True)

plt.title('Popularity of Music Genres', fontsize=18, pad=20)
plt.xlabel('Popularity', fontsize=14)
plt.ylabel('Music Genre', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.show()