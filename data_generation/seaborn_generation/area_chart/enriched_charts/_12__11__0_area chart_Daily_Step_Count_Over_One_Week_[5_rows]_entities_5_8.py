
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
    'DistanceRun': [2.5, 2.8, 3.0, 2.9, 3.1, 3.4, 3.6, 3.8, 3.7, 3.9, 4.0, 4.2, 4.5, 4.6, 4.8, 4.7, 5.0, 5.1, 5.3, 5.5, 5.4, 5.6, 5.8, 6.0, 6.1, 6.3, 6.5, 6.4, 6.7, 6.8, 7.0]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 8))
area_chart = sns.lineplot(data=df, x='Day', y='DistanceRun', color='#FF6347')
area_chart.fill_between(df['Day'], df['DistanceRun'], color='#FFD700', alpha=0.6)

max_distance = df['DistanceRun'].max()
max_day = df['DistanceRun'].idxmax() + 1
plt.text(max_day, max_distance, 'Longest Distance', horizontalalignment='center', verticalalignment='bottom', color='#8A2BE2')

plt.title("Daily Running Distance Over a Month", fontsize=18, pad=25)
plt.xlabel("Day of the Month", fontsize=14)
plt.ylabel("Distance Run (km)", fontsize=14)

plt.show()