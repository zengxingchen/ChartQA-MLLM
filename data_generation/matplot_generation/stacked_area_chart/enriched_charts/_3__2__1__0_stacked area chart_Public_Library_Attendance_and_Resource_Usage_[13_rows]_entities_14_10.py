
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Quarter': [
        'Q1-2021', 'Q2-2021', 'Q3-2021', 'Q4-2021', 
        'Q1-2022', 'Q2-2022', 'Q3-2022', 'Q4-2022',
        'Q1-2023', 'Q2-2023', 'Q3-2023', 'Q4-2023'
    ],
    'Baseball': [4000, 4200, 4400, 4600, 4800, 5000, 5200, 5400, 5600, 5800, 6000, 6200],
    'Football': [3500, 3600, 3700, 3800, 3900, 4000, 4100, 4200, 4300, 4400, 4500, 4600],
    'Basketball': [3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 4000, 4100]
}

df = pd.DataFrame(data)

# Figure and Plot
fig, ax = plt.subplots(figsize=(16, 10))
ax.stackplot(df['Quarter'], df['Baseball'], df['Football'], df['Basketball'],
             labels=['Baseball', 'Football', 'Basketball'],
             colors=['#FF5733', '#33FFCE', '#3375FF'])

# Title and labels
plt.title('Quarterly Sports Equipment Sales', pad=30)
plt.xlabel('Quarter')
plt.ylabel('Sales Value (in $1000s)')
plt.legend(loc='upper left')

# Annotations
for i, (quarter, baseball, football, basketball) in enumerate(zip(df['Quarter'], df['Baseball'], df['Football'], df['Basketball'])):
    total_value = baseball + football + basketball
    ax.annotate(f'Total: {total_value}', (i, total_value), textcoords="offset points", xytext=(0,10), ha='center')

# Show plot
plt.tight_layout()
plt.show()