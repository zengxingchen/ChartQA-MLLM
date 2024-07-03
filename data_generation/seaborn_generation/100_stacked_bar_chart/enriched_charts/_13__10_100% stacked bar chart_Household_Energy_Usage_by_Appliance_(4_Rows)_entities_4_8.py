
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = [
    {'Room': 'Kitchen', 'Lighting (%)': 10, 'Refrigeration (%)': 30, 'Heating and Cooling (%)': 20, 'Electronics (%)': 25, 'Washing and Drying (%)': 15},
    {'Room': 'Living Room', 'Lighting (%)': 15, 'Refrigeration (%)': 5, 'Heating and Cooling (%)': 30, 'Electronics (%)': 30, 'Washing and Drying (%)': 20},
    {'Room': 'Bedroom', 'Lighting (%)': 25, 'Refrigeration (%)': 10, 'Heating and Cooling (%)': 20, 'Electronics (%)': 25, 'Washing and Drying (%)': 20},
    {'Room': 'Bathroom', 'Lighting (%)': 20, 'Refrigeration (%)': 15, 'Heating and Cooling (%)': 25, 'Electronics (%)': 20, 'Washing and Drying (%)': 20},
    {'Room': 'Dining Room', 'Lighting (%)': 15, 'Refrigeration (%)': 25, 'Heating and Cooling (%)': 15, 'Electronics (%)': 30, 'Washing and Drying (%)': 15}
]

df = pd.DataFrame(data)
df.set_index('Room', inplace=True)

df_percentage = df.div(df.sum(axis=1), axis=0) * 100

plt.figure(figsize=(12, 8))

bottom = np.zeros(len(df))

colors = ['#FF5733', '#33FFBD', '#337BFF', '#FF33A8', '#DAFF33']

for i, col in enumerate(df.columns):
    plt.bar(df_percentage.index, df_percentage[col], bottom=bottom, label=col, color=colors[i], width=0.5)
    bottom += df_percentage[col]

plt.xlabel('Rooms')
plt.ylabel('Percentage')
plt.title('Energy Usage by Room (100% Stacked Bar)', pad=20)
plt.legend(title='Categories', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()