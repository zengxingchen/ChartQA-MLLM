
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Quarter': ['Q1-2021', 'Q2-2021', 'Q3-2021', 'Q4-2021', 'Q1-2022', 'Q2-2022', 'Q3-2022', 'Q4-2022'],
    'Wind Energy': [12000, 15000, 17000, 16000, 18000, 20000, 22000, 21000],
    'Solar Energy': [8000, 10000, 12000, 14000, 11000, 13000, 15000, 16000],
    'Hydro Energy': [5000, 6000, 7000, 7500, 8000, 8500, 9000, 9500]
}

df = pd.DataFrame(data)

# Figure and Plot
fig, ax = plt.subplots(figsize=(12, 7))
ax.stackplot(df['Quarter'], df['Wind Energy'], df['Solar Energy'], df['Hydro Energy'],
             labels=['Wind Energy', 'Solar Energy', 'Hydro Energy'],
             colors=['#1f78b4', '#33a02c', '#fb9a99'])

# Title and labels
plt.title('Quarterly Renewable Energy Production', pad=20)
plt.xlabel('Quarter')
plt.ylabel('Energy Production (in GWh)')
plt.legend(loc='upper right')

# Annotations
for i, (quarter, wind, solar, hydro) in enumerate(zip(df['Quarter'], df['Wind Energy'], df['Solar Energy'], df['Hydro Energy'])):
    total_energy = wind + solar + hydro
    ax.annotate(f'Total: {total_energy}', (i, total_energy), textcoords="offset points", xytext=(0,10), ha='center')

# Show plot
plt.tight_layout()
plt.show()