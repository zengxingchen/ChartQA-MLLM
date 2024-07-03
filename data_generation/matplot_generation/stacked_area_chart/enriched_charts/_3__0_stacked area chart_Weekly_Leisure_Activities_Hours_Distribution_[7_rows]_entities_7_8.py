
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Meditation': [1, 1, 2, 1, 1, 2, 2],
    'Work': [8, 9, 8, 9, 8, 4, 3],
    'Leisure': [5, 4, 4, 4, 5, 6, 7],
    'Exercise': [2, 2, 2, 3, 2, 3, 3],
    'Reading': [1, 1, 2, 1, 2, 3, 3]
}
df = pd.DataFrame(data)
df.set_index('Day', inplace=True)

plt.figure(figsize=(14, 7))
plt.stackplot(df.index, df['Meditation'], df['Work'], df['Leisure'], df['Exercise'], df['Reading'], 
              colors=['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#FF9633'])

plt.xlabel('Day of the Week')
plt.ylabel('Hours')
plt.title('Daily Activities for Mental and Physical Health')

for i, day in enumerate(df.index):
    plt.text(i, df.loc[day].sum() - 0.5, f"{df.loc[day].sum()}h", ha='center', fontsize=9)

plt.legend(['Meditation', 'Work', 'Leisure', 'Exercise', 'Reading'], loc='upper right')
plt.tight_layout()

plt.show()