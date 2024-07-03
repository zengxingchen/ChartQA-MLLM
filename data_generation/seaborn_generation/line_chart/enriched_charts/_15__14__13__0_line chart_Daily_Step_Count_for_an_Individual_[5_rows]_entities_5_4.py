
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Week': [i for i in range(1, 53)],
    'Number_of_Tourists': [
        1200, 1300, 1250, 1400, 1500, 1550, 1600, 1580, 1620, 1700, 1650, 1680, 1750, 1800, 1850, 1900, 1950, 2000, 1980, 2050, 2100, 2200, 2250, 2300, 2350, 2400, 2500, 2450, 2550, 2600, 2650, 2700, 2750, 2800, 2850, 2900, 2950, 3000, 3100, 3150, 3200, 3250, 3300, 3350, 3400, 3450, 3500, 3550, 3600, 3700, 3750, 3800
    ]
}

df = pd.DataFrame(data)

sns.set_theme(style="whitegrid")

plt.figure(figsize=(14, 7))
plot = sns.lineplot(x='Week', y='Number_of_Tourists', data=df, linewidth=2.5, color="#1f77b4")

plt.annotate('Peak tourist influx', 
             xy=(50, df.loc[49, 'Number_of_Tourists']), 
             xycoords='data',
             xytext=(40, 3700),
             textcoords='data',
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))

plt.annotate('Lowest tourist count', 
             xy=(1, df.loc[0, 'Number_of_Tourists']), 
             xycoords='data',
             xytext=(10, 1000),
             textcoords='data',
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))

plt.title('Weekly Tourist Visits to Fantasy Island')
plt.xlabel('Week')
plt.ylabel('Number of Tourists')

plt.show()