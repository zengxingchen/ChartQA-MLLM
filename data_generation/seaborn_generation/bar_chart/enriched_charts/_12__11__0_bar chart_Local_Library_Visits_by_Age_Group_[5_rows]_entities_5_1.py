
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Country': [
        'United States', 'Germany', 'France', 'Italy', 'United Kingdom',
        'Canada', 'Japan', 'South Korea', 'China', 'India',
        'Mexico', 'Brazil', 'Russia', 'Australia', 'Netherlands',
        'Spain', 'Switzerland', 'Belgium', 'Hong Kong', 'Singapore',
        'New Zealand', 'Norway', 'Sweden', 'Denmark', 'Finland'
    ],
    'Calorie Intake': [
        3750, 3550, 3450, 3200, 3100,
        3050, 2800, 2700, 2600, 2400,
        2300, 2250, 2200, 2150, 2100,
        2050, 2000, 1950, 1900, 1850,
        1800, 1750, 1700, 1650, 1600
    ]
}
df = pd.DataFrame(data)

sns.set(style="whitegrid")
plt.figure(figsize=(10, 12))

barplot = sns.barplot(
    y="Country",
    x="Calorie Intake",
    data=df,
    palette=[
        '#4C72B0', '#55A868', '#C44E52', '#8172B3', '#CCB974',
        '#64B5CD', '#FFB5B8', '#FFA07A', '#8A2BE2', '#FF6347',
        '#4682B4', '#A52A2A', '#5F9EA0', '#D2691E', '#FF7F50',
        '#6495ED', '#DC143C', '#00FFFF', '#00008B', '#008B8B',
        '#B8860B', '#A9A9A9', '#006400', '#8B008B', '#FF1493'
    ],
    ci=None
)

barplot.set_title('Average Daily Calorie Intake by Country (2021)', fontsize=16, weight='bold', pad=20)
barplot.bar_label(barplot.containers[0], fmt='%.0f')
barplot.set(ylabel="Country", xlabel="Calorie Intake (kcal)")

for bar in barplot.containers[0]:
    bar.set_height(0.6)

plt.xticks(rotation=0)
plt.tight_layout()
plt.show()