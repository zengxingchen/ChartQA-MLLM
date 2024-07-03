
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Day": list(range(1, 32)),
    "Steps_Count": [3000, 3200, 2900, 3500, 3700, 3900, 4200,
                    4100, 4500, 4600, 4800, 5000, 5200, 5400,
                    5600, 5800, 6000, 6200, 6400, 6600, 6800,
                    7000, 7200, 7400, 7600, 7800, 8000, 8200,
                    8400, 8600, 8800]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 8))
area_chart = sns.lineplot(data=df, x='Day', y='Steps_Count', color="#FF6347")
area_chart.fill_between(df['Day'], df['Steps_Count'], color="#FF6347", alpha=0.3)

plt.annotate('Highest Step Count',
             xy=(31, 8800),
             xytext=(25, 9000),
             arrowprops=dict(facecolor='#333333', shrink=0.05),
             )

plt.title('Daily Step Count in January')
plt.xlabel('Day of the Month')
plt.ylabel('Step Count')

plt.show()