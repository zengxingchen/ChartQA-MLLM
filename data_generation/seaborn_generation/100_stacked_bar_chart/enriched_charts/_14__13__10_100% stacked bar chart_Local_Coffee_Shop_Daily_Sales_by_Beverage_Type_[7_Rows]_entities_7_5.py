
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = [
    {'Day': 'Monday', 'Appetizers': '25%', 'Main Course': '30%', 'Desserts': '15%', 'Beverages': '20%', 'Salads': '5%', 'Soups': '5%'},
    {'Day': 'Tuesday', 'Appetizers': '20%', 'Main Course': '25%', 'Desserts': '20%', 'Beverages': '20%', 'Salads': '10%', 'Soups': '5%'},
    {'Day': 'Wednesday', 'Appetizers': '30%', 'Main Course': '25%', 'Desserts': '10%', 'Beverages': '20%', 'Salads': '10%', 'Soups': '5%'},
    {'Day': 'Thursday', 'Appetizers': '25%', 'Main Course': '30%', 'Desserts': '15%', 'Beverages': '15%', 'Salads': '10%', 'Soups': '5%'},
    {'Day': 'Friday', 'Appetizers': '20%', 'Main Course': '35%', 'Desserts': '15%', 'Beverages': '15%', 'Salads': '10%', 'Soups': '5%'},
    {'Day': 'Saturday', 'Appetizers': '25%', 'Main Course': '25%', 'Desserts': '15%', 'Beverages': '20%', 'Salads': '10%', 'Soups': '5%'},
    {'Day': 'Sunday', 'Appetizers': '30%', 'Main Course': '20%', 'Desserts': '15%', 'Beverages': '20%', 'Salads': '10%', 'Soups': '5%'}
]

df = pd.DataFrame(data)

for col in df.columns:
    if col != 'Day':
        df[col] = df[col].str.rstrip('%').astype('float') / 100

df.set_index('Day', inplace=True)
df.sort_index(inplace=True)

cumsum_df = df.cumsum(axis=1)

fig, ax = plt.subplots(figsize=(14, 10))

colors = ['#FF5733', '#33FF57', '#3357FF', '#F333FF', '#FF33A1', '#33FFF6']
width = 0.85
for i, col in enumerate(df.columns):
    ax.bar(df.index, df[col], bottom=cumsum_df[col] - df[col], color=colors[i], edgecolor='white', width=width)

plt.yticks(ticks=[0, 0.2, 0.4, 0.6, 0.8, 1], labels=['0%', '20%', '40%', '60%', '80%', '100%'])
plt.ylabel('Percentage')
plt.xlabel('Day of the Week')
plt.title('Daily Food Consumption by Type', pad=20)
plt.legend(df.columns, bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

plt.show()