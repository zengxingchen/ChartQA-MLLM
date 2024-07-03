
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Fruits': [2, 2, 1, 2, 1, 2, 1],
    'Vegetables': [1, 2, 1, 1, 2, 2, 1],
    'Proteins': [1, 1, 2, 1, 2, 2, 2],
    'Dairy': [1, 1, 2, 2, 1, 1, 1],
    'Grains': [1, 1, 1, 2, 1, 2, 3]
}
df = pd.DataFrame(data)
df.set_index('Day', inplace=True)

plt.figure(figsize=(16, 10))
plt.stackplot(df.index, df['Fruits'], df['Vegetables'], df['Proteins'], df['Dairy'], df['Grains'], 
              colors=['#FF6347', '#3CB371', '#FFD700', '#8A2BE2', '#4682B4'])

plt.xlabel('Day of the Week')
plt.ylabel('Servings')
plt.title('Weekly Food Consumption', pad=20)

for i, day in enumerate(df.index):
    plt.text(i, df.loc[day].sum() - 0.5, f"{df.loc[day].sum()} servings", ha='center', fontsize=10)

plt.legend(['Fruits', 'Vegetables', 'Proteins', 'Dairy', 'Grains'], loc='upper left')
plt.tight_layout()

plt.show()