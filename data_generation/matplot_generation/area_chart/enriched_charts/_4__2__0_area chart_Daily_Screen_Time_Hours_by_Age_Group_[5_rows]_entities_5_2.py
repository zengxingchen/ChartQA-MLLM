
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Day": list(range(1, 31)),
    "Distance_Cycled": [3.2, 3.5, 3.1, 3.8, 4.0, 4.3, 4.7, 4.6, 5.1, 5.3, 
                        5.7, 6.0, 6.3, 6.5, 6.8, 7.0, 7.4, 7.7, 8.0, 8.3, 
                        8.5, 8.8, 9.0, 9.3, 9.6, 9.9, 10.2, 10.5, 10.7, 11.0]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 9))
area_chart = sns.lineplot(data=df, x='Day', y='Distance_Cycled', color="#4682B4")
area_chart.fill_between(df['Day'], df['Distance_Cycled'], color="#4682B4", alpha=0.3)

plt.annotate('Longest Distance',
             xy=(30, 11.0),
             xytext=(25, 11.5),
             arrowprops=dict(facecolor='#333333', shrink=0.05),
             )

plt.title('Daily Distance Cycled in June', fontsize=16)
plt.xlabel('Day of the Month')
plt.ylabel('Distance Cycled (km)')

plt.show()