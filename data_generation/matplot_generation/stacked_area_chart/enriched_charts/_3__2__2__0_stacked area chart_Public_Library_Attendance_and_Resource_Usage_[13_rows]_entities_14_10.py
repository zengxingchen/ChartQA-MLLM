
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Category': ['2021-Q1', '2021-Q2', '2021-Q3', '2021-Q4', '2022-Q1', '2022-Q2', '2022-Q3', '2022-Q4', '2023-Q1', '2023-Q2', '2023-Q3', '2023-Q4', '2024-Q1', '2024-Q2', '2024-Q3', '2024-Q4'],
    'Stocks': [1050, 1150, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900],
    'Bonds': [850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600],
    'Real Estate': [900, 1000, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(16, 10))
ax.stackplot(df['Category'], df['Stocks'], df['Bonds'], df['Real Estate'],
             labels=['Stocks', 'Bonds', 'Real Estate'],
             colors=['#8c564b', '#e377c2', '#7f7f7f'])

plt.title('Quarterly Investment Trends', pad=40, fontsize=20)
plt.xlabel('Quarter')
plt.ylabel('Investment Amount (in thousands)')
plt.legend(loc='upper left')

for i, (category, stocks, bonds, real_estate) in enumerate(zip(df['Category'], df['Stocks'], df['Bonds'], df['Real Estate'])):
    total_investment = stocks + bonds + real_estate
    ax.annotate(f'Total: {total_investment}', (category, total_investment), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)

plt.tight_layout()
plt.show()