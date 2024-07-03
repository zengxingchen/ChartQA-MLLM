
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = [
    {'Room': 'Office', 'Lighting (%)': 15, 'Refrigeration (%)': 25, 'Heating and Cooling (%)': 20, 'Electronics (%)': 25, 'Washing and Drying (%)': 15},
    {'Room': 'Garage', 'Lighting (%)': 20, 'Refrigeration (%)': 10, 'Heating and Cooling (%)': 30, 'Electronics (%)': 15, 'Washing and Drying (%)': 25},
    {'Room': 'Basement', 'Lighting (%)': 10, 'Refrigeration (%)': 15, 'Heating and Cooling (%)': 40, 'Electronics (%)': 20, 'Washing and Drying (%)': 15},
    {'Room': 'Attic', 'Lighting (%)': 25, 'Refrigeration (%)': 20, 'Heating and Cooling (%)': 15, 'Electronics (%)': 20, 'Washing and Drying (%)': 20}
]

df = pd.DataFrame(data)
df.set_index('Room', inplace=True)

df_percentage = df.div(df.sum(axis=1), axis=0) * 100

plt.figure(figsize=(8, 10))

bottom = np.zeros(len(df))

colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700']

for i, col in enumerate(df.columns):
    plt.bar(df_percentage.index, df_percentage[col], bottom=bottom, label=col, color=colors[i], width=0.6)
    bottom += df_percentage[col]

plt.xlabel('Rooms')
plt.ylabel('Percentage')
plt.title('Room Energy Usage Breakdown (100% Stacked)', pad=20)
plt.legend(title='Categories', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()