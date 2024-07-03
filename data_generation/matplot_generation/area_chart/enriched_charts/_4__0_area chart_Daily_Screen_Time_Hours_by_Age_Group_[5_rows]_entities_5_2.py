
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Day": list(range(1, 32)),
    "Steps": [5000, 5200, 5300, 5400, 5500, 5600, 5700, 5800, 5900, 6000, 
              6100, 6200, 6300, 6400, 6500, 6600, 6700, 6800, 6900, 7000, 
              7100, 7200, 7300, 7400, 7500, 7600, 7700, 7800, 7900, 8000, 8100]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 7))
area_chart = sns.lineplot(data=df, x='Day', y='Steps', color="#FF6347")
area_chart.fill_between(df['Day'], df['Steps'], color="#FF6347", alpha=0.3)

plt.annotate('Highest Steps Count',
             xy=(31, 8100),
             xytext=(20, 7800),
             arrowprops=dict(facecolor='#000000', shrink=0.05),
             )

plt.title('Daily Step Count in January')
plt.xlabel('Day of the Month')
plt.ylabel('Number of Steps')

plt.show()