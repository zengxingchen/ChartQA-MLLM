
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Calories Consumed': [2500, 2300, 2400, 2600, 2450, 2700, 2500],
    'Calories Burned': [2000, 1900, 1950, 2050, 2000, 2200, 2100],
    'Calories from Carbs': [1000, 900, 950, 1050, 1000, 1100, 1000],
    'Calories from Proteins': [800, 700, 750, 850, 750, 800, 800],
    'Calories from Fats': [700, 700, 700, 700, 700, 800, 700]
}
df = pd.DataFrame(data)
df.set_index('Day', inplace=True)

plt.figure(figsize=(14, 8))
plt.stackplot(df.index, df['Calories Consumed'], df['Calories Burned'], df['Calories from Carbs'], df['Calories from Proteins'], df['Calories from Fats'], 
              colors=['#FF5733', '#C70039', '#900C3F', '#581845', '#1C2833'])

plt.xlabel('Day of the Week')
plt.ylabel('Calories')
plt.title('Daily Caloric Intake and Burn Breakdown')

for i, day in enumerate(df.index):
    plt.text(i, df.loc[day].sum() - 500, f"{df.loc[day].sum()} cal", ha='center', fontsize=10, color='white', weight='bold')

plt.legend(['Calories Consumed', 'Calories Burned', 'Calories from Carbs', 'Calories from Proteins', 'Calories from Fats'], loc='upper right')
plt.tight_layout()

plt.show()