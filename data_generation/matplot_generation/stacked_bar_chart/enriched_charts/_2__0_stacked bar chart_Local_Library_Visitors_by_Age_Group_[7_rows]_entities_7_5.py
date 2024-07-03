
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Year': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    'Running': [100, 110, 115, 120, 130, 140, 150, 160, 170, 180],
    'Cycling': [50, 55, 60, 65, 70, 75, 80, 85, 90, 95],
    'Swimming': [30, 35, 40, 45, 50, 55, 60, 65, 70, 75],
    'Weightlifting': [20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(12, 9))

bars1 = ax.bar(df['Year'], df['Running'], color='#1f77b4', edgecolor='grey', width=0.8, label='Running')
bars2 = ax.bar(df['Year'], df['Cycling'], bottom=df['Running'], color='#ff7f0e', edgecolor='grey', width=0.8, label='Cycling')
bars3 = ax.bar(df['Year'], df['Swimming'], bottom=df['Running'] + df['Cycling'], color='#2ca02c', edgecolor='grey', width=0.8, label='Swimming')
bars4 = ax.bar(df['Year'], df['Weightlifting'], bottom=df['Running'] + df['Cycling'] + df['Swimming'], color='#d62728', edgecolor='grey', width=0.8, label='Weightlifting')

ax.set_ylabel('Exercise Duration (Hours)')
ax.set_title('Exercise Trends Over Years')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

for bars in [bars1, bars2, bars3, bars4]:
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, bar.get_y() + height / 2),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='center')

plt.show()