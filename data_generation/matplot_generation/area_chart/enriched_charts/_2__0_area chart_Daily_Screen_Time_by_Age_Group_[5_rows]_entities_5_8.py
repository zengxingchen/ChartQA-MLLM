import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'Day': list(range(1, 31)),
    'CaloriesBurned': [
        2300, 2450, 2350, 2500, 2600, 2700, 2200, 2650, 2750, 2800, 
        2900, 3000, 3100, 2950, 2850, 2750, 2650, 2550, 2450, 2350, 
        2250, 2150, 2050, 1950, 1850, 1750, 1650, 1550, 1450, 1350
    ]
})

plt.figure(figsize=(14, 7))
sns.set_theme(style="whitegrid")

ax = sns.lineplot(data=data, x='Day', y='CaloriesBurned', color="#FFA07A")
ax.fill_between(data.Day, data.CaloriesBurned, color="#87CEFA", alpha=0.5)

highest_calories = data.CaloriesBurned.max()
highest_day = data.Day[data.CaloriesBurned.idxmax()]
plt.annotate(f'Highest\n{highest_calories} kcal', xy=(highest_day, highest_calories), xytext=(highest_day+2, highest_calories+100),
             arrowprops=dict(facecolor='#FF4500', shrink=0.05))

plt.title('Daily Calories Burned in January')
plt.xlabel('Day')
plt.ylabel('Calories Burned (kcal)')

plt.show()