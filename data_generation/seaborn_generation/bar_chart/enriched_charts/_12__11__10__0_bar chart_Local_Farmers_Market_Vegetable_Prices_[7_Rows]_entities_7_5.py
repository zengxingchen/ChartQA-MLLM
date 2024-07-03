
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia',
             'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Jacksonville',
             'Fort Worth', 'Columbus', 'Charlotte'],
    'average_workout_hours': [1.2, 1.5, 1.1, 1.3, 1.4, 1.6, 1.8, 1.9, 1.7, 1.4, 1.3, 1.2, 1.5, 1.6, 1.4]
}

df = pd.DataFrame(data)

plt.figure(figsize=(10, 14))
barplot = sns.barplot(
    x='city',
    y='average_workout_hours',
    data=df,
    palette=['#A52A2A', '#5F9EA0', '#7FFF00', '#D2691E', '#FF7F50', '#6495ED', '#DC143C', '#00008B', '#008B8B',
             '#B8860B', '#006400', '#8B008B', '#556B2F', '#FF8C00', '#9932CC'],
    orient='v'
)

for bar in barplot.patches:
    bar.set_width(0.5)

plt.title('Average Daily Workout Hours in Different Cities', fontsize=16, pad=20)
plt.ylabel('Average Workout Hours', fontsize=14)
plt.xlabel('City', fontsize=14)

plt.show()