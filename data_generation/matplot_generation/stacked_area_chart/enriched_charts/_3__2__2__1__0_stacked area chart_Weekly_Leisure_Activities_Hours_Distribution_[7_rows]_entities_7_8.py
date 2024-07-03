
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Renewable Energy': [7, 8, 6, 7, 8, 9, 8],
    'Fossil Fuels': [5, 6, 7, 6, 5, 7, 6],
    'Nuclear Energy': [3, 4, 5, 4, 6, 5, 4],
    'Hydropower': [4, 5, 4, 6, 7, 6, 7],
    'Solar Power': [6, 7, 6, 5, 6, 7, 8]
}
df = pd.DataFrame(data)
df.set_index('Day', inplace=True)

plt.figure(figsize=(20, 14))
plt.stackplot(df.index, df['Renewable Energy'], df['Fossil Fuels'], df['Nuclear Energy'], df['Hydropower'], df['Solar Power'], 
              colors=['#FF5733', '#33C1FF', '#FFC300', '#DAF7A6', '#C70039'])

plt.xlabel('Day of the Week')
plt.ylabel('Energy Consumption (in units)')
plt.title('Weekly Energy Consumption by Source', pad=40)

for i, day in enumerate(df.index):
    plt.text(i, df.loc[day].sum() - 2, f"{df.loc[day].sum()} units", ha='center', fontsize=14, color='black')

plt.legend(['Renewable Energy', 'Fossil Fuels', 'Nuclear Energy', 'Hydropower', 'Solar Power'], loc='upper left')
plt.tight_layout()

plt.show()