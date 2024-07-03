
import matplotlib.pyplot as plt
import pandas as pd

# Create dataframe from the data provided
data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Sleep': [8, 7, 8, 7, 8, 9, 9],
    'Work': [8, 9, 8, 9, 8, 4, 3],
    'Leisure': [4, 4, 4, 3, 5, 6, 7],
    'Exercise': [2, 2, 3, 3, 2, 3, 3],
    'Chores': [2, 2, 1, 2, 1, 2, 2]
}
df = pd.DataFrame(data)
df.set_index('Day', inplace=True)

# Plot stacked area chart
plt.figure(figsize=(12, 6))
plt.stackplot(df.index, df['Sleep'], df['Work'], df['Leisure'], df['Exercise'], df['Chores'], 
              colors=['#5DADE2', '#48C9B0', '#F4D03F', '#EB984E', '#7D3C98'])

# Add labels, title and customize axis
plt.xlabel('Day of the Week')
plt.ylabel('Hours')
plt.title('Average Time Spent on Daily Activities in a Week')

# Annotations
for i, day in enumerate(df.index):
    plt.text(i, df.loc[day].sum() - 0.5, f"{df.loc[day].sum()}h", ha='center', fontsize=9)

plt.legend(['Sleep', 'Work', 'Leisure', 'Exercise', 'Chores'], loc='upper left')
plt.tight_layout()

plt.show()