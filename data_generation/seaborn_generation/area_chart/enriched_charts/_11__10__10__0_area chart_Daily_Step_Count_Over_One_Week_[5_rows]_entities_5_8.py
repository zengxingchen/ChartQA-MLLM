
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
    'Steps_Count': [5000, 5200, 5100, 5300, 5250, 5400, 5350, 5500, 5450, 5600, 5550, 5700, 5650, 5800, 5750, 5900, 5850, 6000, 5950, 6100, 6050, 6200, 6150, 6300, 6250, 6400, 6350, 6500, 6450, 6600, 6550]
}

df = pd.DataFrame(data)

plt.figure(figsize=(18, 8))
area_chart = sns.lineplot(data=df, x='Day', y='Steps_Count', color='#1E90FF')
area_chart.fill_between(df['Day'], df['Steps_Count'], color='#87CEFA', alpha=0.5)

max_steps = df['Steps_Count'].max()
max_day = df['Steps_Count'].idxmax() + 1
plt.text(max_day, max_steps, 'Peak\nSteps', horizontalalignment='center', verticalalignment='bottom', color='#2E8B57')

plt.title("Daily Steps Count Over a Month", pad=20)
plt.xlabel("Day of the Month")
plt.ylabel("Steps Count")

plt.show()