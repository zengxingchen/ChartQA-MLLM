
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

data_str = """Month,Research & Development,Marketing,Sales
January,8000,5000,3000
February,8500,5300,3200
March,8700,5600,3500
April,8900,5800,3700
May,9200,6000,4000
June,9400,6200,4200
July,9600,6400,4400
August,9800,6600,4600
September,10000,6800,4800
October,10200,7000,5000
November,10500,7200,5200
December,10800,7400,5400
January,11000,7600,5600
February,11200,7800,5800
March,11500,8000,6000
April,11700,8200,6200
May,12000,8400,6400
June,12200,8600,6600
July,12500,8800,6800
August,12800,9000,7000
September,13000,9200,7200
October,13300,9400,7400
November,13600,9600,7600
December,14000,9800,7800"""

data = pd.read_csv(StringIO(data_str), index_col='Month')

x = data.index
y = [data['Research & Development'], data['Marketing'], data['Sales']]

fig, ax = plt.subplots(figsize=(14, 10))

ax.stackplot(x, y, labels=['Research & Development', 'Marketing', 'Sales'], colors=['#8A2BE2', '#5F9EA0', '#FFD700'])

ax.set_title('Annual Department Budget Allocation (in Thousands)', pad=20)
ax.set_xlabel('Month')
ax.set_ylabel('Budget (in Thousands)')
ax.legend(loc='upper left')

for i, (month, values) in enumerate(data.iterrows()):
    ax.annotate(f"{values['Research & Development']}", xy=(i, values['Research & Development']/2), ha='center', fontsize=8)
    ax.annotate(f"{values['Marketing']}", xy=(i, values['Research & Development']+values['Marketing']/2), ha='center', fontsize=8)
    ax.annotate(f"{values['Sales']}", xy=(i, values['Research & Development']+values['Marketing']+values['Sales']/2), ha='center', fontsize=8)

plt.tight_layout()
plt.show()