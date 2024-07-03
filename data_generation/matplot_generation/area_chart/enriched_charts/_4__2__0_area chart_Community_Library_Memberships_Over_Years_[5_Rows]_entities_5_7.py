
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Day": list(range(1, 31)),
    "Steps": [5500, 6800, 7200, 6100, 8300, 7800, 9000, 10000, 9500, 8900, 10300, 9700, 8800, 10500, 11000, 9500, 9200, 10800, 9700, 10000, 9500, 9000, 10500, 10900, 9600, 9300, 9800, 10200, 11000, 10800]
}

data_df = pd.DataFrame(data)

plt.figure(figsize=(16, 10))
sns_line = sns.lineplot(data=data_df, x="Day", y="Steps", color="#FF5733")
sns_line.fill_between(data_df.Day, data_df.Steps, color="#FF5733", alpha=0.3)

plt.annotate('Highest Activity', xy=(15, data_df.loc[14, 'Steps']),
             xytext=(20, data_df.Steps.max() + 500),
             arrowprops=dict(facecolor='black', shrink=0.05))

sns_line.set_title('Daily Step Count for a Month', fontsize=20, loc='center')
sns_line.set_xlabel('Day')
sns_line.set_ylabel('Steps')
plt.show()