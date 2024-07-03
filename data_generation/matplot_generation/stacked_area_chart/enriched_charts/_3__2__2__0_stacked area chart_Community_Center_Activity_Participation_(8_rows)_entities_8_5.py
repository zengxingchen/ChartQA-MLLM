
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

csv_data = """Month,Fruits,Vegetables,Grains
January,50000,35000,20000
February,52000,36000,21000
March,54000,37000,22000
April,56000,38000,23000
May,58000,39000,24000
June,60000,40000,25000
July,62000,41000,26000
August,64000,42000,27000
September,66000,43000,28000
October,68000,44000,29000
November,70000,45000,30000
December,72000,46000,31000
"""

data = pd.read_csv(StringIO(csv_data), index_col='Month')

x = data.index
y = [data['Fruits'], data['Vegetables'], data['Grains']]

fig, ax = plt.subplots(figsize=(16, 10))

ax.stackplot(x, y, labels=['Fruits', 'Vegetables', 'Grains'], colors=['#ff9999', '#66b3ff', '#99ff99'])

ax.set_title('Monthly Food Production by Type (in kg)', fontsize=18, pad=30)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Production (kg)', fontsize=14)
ax.legend(loc='upper left')

for i, (month, values) in enumerate(data.iterrows()):
    ax.annotate(f"{values['Fruits']}", xy=(i, values['Fruits']/2), ha='center', fontsize=10)
    ax.annotate(f"{values['Vegetables']}", xy=(i, values['Fruits'] + values['Vegetables']/2), ha='center', fontsize=10)
    ax.annotate(f"{values['Grains']}", xy=(i, values['Fruits'] + values['Vegetables'] + values['Grains']/2), ha='center', fontsize=10)

plt.tight_layout()
plt.show()