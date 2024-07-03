
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December'],
    'GalleryVisitors': [300, 320, 330, 340, 350, 370, 390, 400, 420, 440, 460, 480],
    'ArtSales': [5000, 5200, 5300, 5400, 5500, 5700, 5900, 6000, 6200, 6400, 6600, 6800],
    'WorkshopsAttended': [20, 25, 22, 28, 30, 35, 40, 38, 42, 45, 48, 50]
}

df = pd.DataFrame(data)
df = df.set_index('Month')

df_cum = df.cumsum(axis=1)

colors = ['#FF6347', '#4682B4', '#32CD32']

plt.figure(figsize=(16, 10))

plt.fill_between(df.index, 0, df_cum['GalleryVisitors'], color=colors[0], alpha=0.7, label='Gallery Visitors')
plt.fill_between(df.index, df_cum['GalleryVisitors'], df_cum['GalleryVisitors'] + df_cum['ArtSales'], color=colors[1], alpha=0.7, label='Art Sales')
plt.fill_between(df.index, df_cum['GalleryVisitors'] + df_cum['ArtSales'], df_cum['GalleryVisitors'] + df_cum['ArtSales'] + df_cum['WorkshopsAttended'], color=colors[2], alpha=0.7, label='Workshops Attended')

for category in ['GalleryVisitors', 'ArtSales', 'WorkshopsAttended']:
    plt.text(df.index[-1], df_cum[category][-1] - (df_cum[category][-1] - df_cum[category].shift(1)[-1]) / 2, category.replace('Visitors', ' Visitors').replace('Sales', ' Sales').replace('Attended', ' Attended'), verticalalignment='center')

plt.title('Monthly Art Gallery Statistics', fontsize=20, pad=20)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Values', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.legend(loc='upper left', fontsize=12)
plt.tight_layout()

plt.show()