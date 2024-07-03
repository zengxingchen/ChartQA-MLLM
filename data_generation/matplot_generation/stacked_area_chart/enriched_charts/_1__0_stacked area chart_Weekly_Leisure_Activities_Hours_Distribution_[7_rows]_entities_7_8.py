
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Cardio': [1, 2, 1, 2, 1, 2, 1],
    'Strength': [1, 1, 2, 1, 1, 2, 2],
    'Flexibility': [1, 1, 1, 1, 2, 1, 1],
    'Team Sports': [1, 1, 1, 1, 1, 2, 1],
    'Other': [2, 2, 2, 2, 2, 1, 3]
}
df = pd.DataFrame(data)
df.set_index('Day', inplace=True)

plt.figure(figsize=(14, 8))
plt.stackplot(df.index, df['Cardio'], df['Strength'], df['Flexibility'], df['Team Sports'], df['Other'], 
              colors=['#FF5733', '#33FF57', '#3357FF', '#F333FF', '#FF33C4'])

plt.xlabel('Day of the Week')
plt.ylabel('Hours')
plt.title('Weekly Exercise Routine')

for i, day in enumerate(df.index):
    plt.text(i, df.loc[day].sum() - 0.5, f"{df.loc[day].sum()}h", ha='center', fontsize=10)

plt.legend(['Cardio', 'Strength', 'Flexibility', 'Team Sports', 'Other'], loc='upper right')
plt.tight_layout()

plt.show()