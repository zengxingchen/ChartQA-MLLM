
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Articles': [5, 6, 7, 5, 6, 8, 7],
    'Books': [3, 2, 4, 5, 3, 4, 5],
    'Magazines': [4, 5, 3, 6, 5, 6, 7],
    'Journals': [2, 3, 4, 2, 3, 4, 5],
    'Newsletters': [3, 4, 5, 3, 4, 5, 6]
}
df = pd.DataFrame(data)
df.set_index('Day', inplace=True)

plt.figure(figsize=(18, 12))
plt.stackplot(df.index, df['Articles'], df['Books'], df['Magazines'], df['Journals'], df['Newsletters'], 
              colors=['#FF6347', '#4682B4', '#8A2BE2', '#32CD32', '#FFD700'])

plt.xlabel('Day of the Week')
plt.ylabel('Reading Material')
plt.title('Weekly Reading Material Consumption', pad=20)

for i, day in enumerate(df.index):
    plt.text(i, df.loc[day].sum() - 1, f"{df.loc[day].sum()} items", ha='center', fontsize=12, color='black')

plt.legend(['Articles', 'Books', 'Magazines', 'Journals', 'Newsletters'], loc='upper right')
plt.tight_layout()

plt.show()