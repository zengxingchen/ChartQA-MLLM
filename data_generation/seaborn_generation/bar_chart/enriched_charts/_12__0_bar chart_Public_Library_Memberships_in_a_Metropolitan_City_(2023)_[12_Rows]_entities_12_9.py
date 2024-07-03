
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Category': ['Rock', 'Pop', 'Jazz', 'Classical', 'Hip-Hop', 'Country', 'Reggae', 'Blues', 'Electronic', 'Folk', 'R&B', 'Soul', 'Metal', 'Punk', 'Latin', 'Disco', 'Gospel', 'Funk', 'Opera', 'Ska'],
    'Value': [100, 150, 130, 200, 180, 160, 170, 190, 210, 230, 220, 240, 260, 250, 270, 280, 300, 290, 310, 320]
}

df = pd.DataFrame(data)

sns.set_theme(style="whitegrid")

plt.figure(figsize=(12, 8))
barplot = sns.barplot(x='Category', y='Value', data=df, palette=['#FFA07A', '#20B2AA', '#778899', '#B0C4DE', '#8FBC8F', '#6495ED', '#FF7F50', '#CD5C5C', '#4682B4', '#D2691E', '#7FFF00', '#8A2BE2', '#FF6347', '#40E0D0', '#9370DB', '#FF4500', '#2E8B57', '#BA55D3', '#1E90FF', '#FF1493'])

barplot.set(ylim=(0, 350))
sns.despine(left=True, bottom=True)

plt.title('Popularity of Music Genres', fontsize=18, y=1.05)
plt.xlabel('Music Genre', fontsize=14)
plt.ylabel('Popularity Score', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)

plt.show()