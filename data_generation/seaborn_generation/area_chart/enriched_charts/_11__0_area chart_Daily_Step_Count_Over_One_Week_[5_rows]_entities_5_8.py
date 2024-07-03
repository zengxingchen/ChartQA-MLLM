
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
    'AvgSteps': [5000, 5200, 5100, 5300, 5600, 5900, 6000, 6200, 6300, 6100, 6400, 6500, 6600, 6800, 7000, 7200, 7100, 7300, 7400, 7600, 7800, 7900, 8000, 8200, 8100, 8300, 8400, 8500, 8700, 8600, 8800]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 7))
area_chart = sns.lineplot(data=df, x='Day', y='AvgSteps', color='#1E90FF')
area_chart.fill_between(df['Day'], df['AvgSteps'], color='#87CEFA', alpha=0.6)

max_steps = df['AvgSteps'].max()
max_day = df['AvgSteps'].idxmax() + 1
plt.text(max_day, max_steps, 'Highest\nSteps', horizontalalignment='center', verticalalignment='bottom', color='#FF4500')

plt.title("Average Daily Steps Over a Month", fontsize=16, pad=20)
plt.xlabel("Day of the Month", fontsize=14)
plt.ylabel("Average Steps", fontsize=14)

plt.show()