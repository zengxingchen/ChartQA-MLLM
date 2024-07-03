
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

csv_data = """Month,North America,Europe,Asia
January,40000,35000,30000
February,42000,36000,31000
March,44000,37000,32000
April,46000,38000,33000
May,48000,39000,34000
June,50000,40000,35000
July,52000,41000,36000
August,54000,42000,37000
September,56000,43000,38000
October,58000,44000,39000
November,60000,45000,40000
December,62000,46000,41000
"""

data = pd.read_csv(StringIO(csv_data), index_col='Month')

x = data.index
y = [data['North America'], data['Europe'], data['Asia']]

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(x, y, labels=['North America', 'Europe', 'Asia'], colors=['#1f77b4', '#ff7f0e', '#2ca02c'])

ax.set_title('Monthly Sales Data by Region (in USD)', fontsize=16, pad=25)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Sales', fontsize=12)
ax.legend(loc='upper left')

for i, (month, values) in enumerate(data.iterrows()):
    ax.annotate(f"{values['North America']}", xy=(i, values['North America']/2), ha='center', fontsize=10)
    ax.annotate(f"{values['Europe']}", xy=(i, values['North America'] + values['Europe']/2), ha='center', fontsize=10)
    ax.annotate(f"{values['Asia']}", xy=(i, values['North America'] + values['Europe'] + values['Asia']/2), ha='center', fontsize=10)

plt.tight_layout()
plt.show()