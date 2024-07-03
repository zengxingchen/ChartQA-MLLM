
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

csv_data = """Month,Historical,Scientific,Technological
January,1500,7000,10000
February,1800,7500,10500
March,2100,7800,10800
April,2500,8200,11000
May,2800,8500,11500
June,3100,9000,12000
July,3400,9500,12500
August,3700,9800,12800
September,4000,10200,13000
October,4300,10700,13500
November,4600,11200,14000
December,4900,11700,14500
"""

data = pd.read_csv(StringIO(csv_data), index_col='Month')

x = data.index
y = [data['Historical'], data['Scientific'], data['Technological']]

fig, ax = plt.subplots(figsize=(16, 10))

ax.stackplot(x, y, labels=['Historical', 'Scientific', 'Technological'], colors=['#FF6347', '#4682B4', '#9ACD32'])

ax.set_title('Monthly Investment in Different Knowledge Areas (in Thousands of Dollars)', fontsize=18, pad=40)
ax.set_xlabel('Month')
ax.set_ylabel('Investment (in $1000)')
ax.legend(loc='upper left')

for i, (month, values) in enumerate(data.iterrows()):
    ax.annotate(f"{values['Historical']}", xy=(i, values['Historical']/2), ha='center')
    ax.annotate(f"{values['Scientific']}", xy=(i, values['Historical']+values['Scientific']/2), ha='center')
    ax.annotate(f"{values['Technological']}", xy=(i, values['Historical']+values['Scientific']+values['Technological']/2), ha='center')

plt.tight_layout()
plt.show()