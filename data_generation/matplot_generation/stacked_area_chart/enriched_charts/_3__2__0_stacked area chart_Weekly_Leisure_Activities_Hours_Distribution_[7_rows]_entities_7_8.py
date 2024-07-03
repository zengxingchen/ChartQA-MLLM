
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Hours Studied': [4, 5, 3, 6, 2, 1, 4],
    'Hours on Entertainment': [2, 1, 2.5, 1, 3, 4, 3],
    'Hours on Exercise': [1, 1.5, 2, 1, 2, 2, 1.5],
    'Hours on Sleep': [7, 6, 6, 8, 7, 9, 8],
    'Hours on Social Activities': [2, 1.5, 1, 1, 2, 3, 2.5]
}

df = pd.DataFrame(data)
df.set_index('Day', inplace=True)

plt.figure(figsize=(16, 9))
plt.stackplot(df.index, df['Hours Studied'], df['Hours on Entertainment'], df['Hours on Exercise'], df['Hours on Sleep'], df['Hours on Social Activities'], 
              colors=['#FF6F61', '#6B5B95', '#88B04B', '#FFA07A', '#0E7C7B'])

plt.xlabel('Day of the Week')
plt.ylabel('Hours')
plt.title('Weekly Activity Breakdown: Study, Entertainment, Exercise, Sleep, Social Activities', pad=20)

for i, day in enumerate(df.index):
    plt.text(i, df.loc[day].sum() - 2, f"{df.loc[day].sum()} hrs", ha='center', fontsize=10, color='white', weight='bold')

plt.legend(['Hours Studied', 'Hours on Entertainment', 'Hours on Exercise', 'Hours on Sleep', 'Hours on Social Activities'], loc='upper left')
plt.tight_layout()

plt.show()