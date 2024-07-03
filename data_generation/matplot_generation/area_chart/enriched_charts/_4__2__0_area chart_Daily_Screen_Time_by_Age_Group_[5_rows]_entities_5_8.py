
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'Day': list(range(1, 31)),
    'StepsWalked': [
        5600, 6100, 5800, 6200, 6300, 6400, 5200, 6500, 6600, 6700,
        6800, 6900, 7000, 7100, 7200, 7300, 7400, 7500, 7600, 7700,
        7800, 7900, 8000, 8100, 8200, 8300, 8400, 8500, 8600, 8700
    ]
})

plt.figure(figsize=(16, 8))
sns.set_theme(style="whitegrid")

ax = sns.lineplot(data=data, x='Day', y='StepsWalked', color="#6A5ACD")
ax.fill_between(data.Day, data.StepsWalked, color="#48D1CC", alpha=0.6)

highest_steps = data.StepsWalked.max()
highest_day = data.Day[data.StepsWalked.idxmax()]
plt.annotate(f'Highest\n{highest_steps} steps', xy=(highest_day, highest_steps), xytext=(highest_day+2, highest_steps+200),
             arrowprops=dict(facecolor='#FF4500', shrink=0.05))

plt.title('Daily Steps Walked in January')
plt.xlabel('Day')
plt.ylabel('Steps Walked')

plt.show()