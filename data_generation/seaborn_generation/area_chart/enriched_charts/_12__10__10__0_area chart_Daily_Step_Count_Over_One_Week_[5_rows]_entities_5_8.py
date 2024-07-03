
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
    'Page_Views': [100, 110, 115, 120, 130, 125, 140, 135, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 8))
area_chart = sns.lineplot(data=df, x='Day', y='Page_Views', color='#4682B4')
area_chart.fill_between(df['Day'], df['Page_Views'], color='#87CEEB', alpha=0.5)

max_views = df['Page_Views'].max()
max_day = df['Page_Views'].idxmax() + 1
plt.text(max_day, max_views, 'Peak\nViews', horizontalalignment='center', verticalalignment='bottom', color='#2E8B57')

plt.title("Daily Website Page Views Over a Month", pad=20)
plt.xlabel("Day of the Month")
plt.ylabel("Page Views")

plt.show()