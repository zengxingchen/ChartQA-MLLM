import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Category': 'Cardio', 'Gym Workouts': '20%', 'Outdoor Activities': '15%', 'Online Tutorials': '20%', 'Diet Plans': '10%', 'Group Classes': '20%', 'Fitness Apps': '15%'},
    {'Category': 'Strength Training', 'Gym Workouts': '25%', 'Outdoor Activities': '10%', 'Online Tutorials': '20%', 'Diet Plans': '15%', 'Group Classes': '15%', 'Fitness Apps': '15%'},
    {'Category': 'Flexibility', 'Gym Workouts': '15%', 'Outdoor Activities': '20%', 'Online Tutorials': '25%', 'Diet Plans': '10%', 'Group Classes': '15%', 'Fitness Apps': '15%'},
    {'Category': 'Balance', 'Gym Workouts': '10%', 'Outdoor Activities': '25%', 'Online Tutorials': '15%', 'Diet Plans': '10%', 'Group Classes': '20%', 'Fitness Apps': '20%'},
    {'Category': 'Endurance', 'Gym Workouts': '20%', 'Outdoor Activities': '15%', 'Online Tutorials': '15%', 'Diet Plans': '20%', 'Group Classes': '15%', 'Fitness Apps': '15%'},
    {'Category': 'High-Intensity Interval Training (HIIT)', 'Gym Workouts': '30%', 'Outdoor Activities': '15%', 'Online Tutorials': '15%', 'Diet Plans': '10%', 'Group Classes': '20%', 'Fitness Apps': '10%'},
    {'Category': 'Yoga', 'Gym Workouts': '15%', 'Outdoor Activities': '20%', 'Online Tutorials': '25%', 'Diet Plans': '10%', 'Group Classes': '20%', 'Fitness Apps': '10%'},
    {'Category': 'Pilates', 'Gym Workouts': '15%', 'Outdoor Activities': '25%', 'Online Tutorials': '15%', 'Diet Plans': '15%', 'Group Classes': '15%', 'Fitness Apps': '15%'},
    {'Category': 'Zumba', 'Gym Workouts': '25%', 'Outdoor Activities': '10%', 'Online Tutorials': '20%', 'Diet Plans': '15%', 'Group Classes': '15%', 'Fitness Apps': '15%'},
    {'Category': 'CrossFit', 'Gym Workouts': '20%', 'Outdoor Activities': '10%', 'Online Tutorials': '15%', 'Diet Plans': '20%', 'Group Classes': '15%', 'Fitness Apps': '20%'},
    {'Category': 'Martial Arts', 'Gym Workouts': '15%', 'Outdoor Activities': '20%', 'Online Tutorials': '15%', 'Diet Plans': '10%', 'Group Classes': '20%', 'Fitness Apps': '20%'}
]

df = pd.DataFrame(data)
df = df.set_index('Category')
df = df.applymap(lambda x: int(x.replace('%', '')))

cumulative_sum = df.cumsum(axis=1)

colors = ['#FF5733', '#33FFBD', '#FF33EC', '#3375FF', '#FF8F33', '#33FF57']

fig, ax = plt.subplots(figsize=(12, 8))

bottom = None

for column, color in zip(df.columns, colors):
    ax.bar(df.index, df[column], bottom=bottom, label=column, color=color, width=0.4)
    bottom = cumulative_sum[column]

ax.legend(title='Fitness Resources', bbox_to_anchor=(1.05, 1), loc='upper left')

ax.set_ylabel('Percentage')
ax.set_xlabel('Fitness Categories')
ax.set_title('Resource Distribution Across Various Fitness Categories', pad=20)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()