
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Day': [i for i in range(1, 32)],
    'Average Daily Humidity (%)': [
        45.2, 46.8, 44.5, 47.1, 48.3, 50.2, 49.1, 51.3, 52.8,
        54.1, 55.6, 57.3, 58.7, 59.8, 60.5, 62.1, 61.3, 60.2,
        58.9, 57.4, 55.9, 54.3, 52.8, 51.1, 49.5, 48.3, 47.1,
        46.0, 45.5, 44.8, 43.6
    ]
}

df = pd.DataFrame(data)

sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 8))

humidity_plot = sns.lineplot(
    x='Day',
    y='Average Daily Humidity (%)',
    data=df,
    color="#1f77b4",
    lw=2
)

plt.title('Average Daily Humidity in Death Valley Over a Month', pad=20)
plt.xlabel('Day of the Month')
plt.ylabel('Average Humidity (%)')

plt.annotate(
    'Lowest Humidity',
    xy=(31, 43.6),
    xytext=(25, 45),
    arrowprops=dict(facecolor='black', shrink=0.05),
    fontsize=12,
    color='#333333'
)

plt.show()