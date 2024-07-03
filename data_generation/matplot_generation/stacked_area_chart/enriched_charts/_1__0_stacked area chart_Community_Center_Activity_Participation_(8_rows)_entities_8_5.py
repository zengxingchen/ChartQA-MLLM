
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

csv_data = """Month,Pop,Rock,Jazz
January,15000,10000,5000
February,16000,12000,5500
March,17000,13000,6000
April,18000,14000,6500
May,19000,15000,7000
June,20000,16000,7500
July,21000,17000,8000
August,22000,18000,8500
September,23000,19000,9000
October,24000,20000,9500
November,25000,21000,10000
December,26000,22000,10500
"""

data = pd.read_csv(StringIO(csv_data), index_col='Month')

x = data.index
y = [data['Pop'], data['Rock'], data['Jazz']]

fig, ax = plt.subplots(figsize=(12, 7))

ax.stackplot(x, y, labels=['Pop', 'Rock', 'Jazz'], colors=['#FFA07A', '#20B2AA', '#778899'])

ax.set_title('Monthly Music Streaming Trends (in Thousands)', fontsize=16, pad=20)
ax.set_xlabel('Month')
ax.set_ylabel('Streams')
ax.legend(loc='upper left')

for i, (month, values) in enumerate(data.iterrows()):
    ax.annotate(f"{values['Pop']}", xy=(i, values['Pop']/2), ha='center')
    ax.annotate(f"{values['Rock']}", xy=(i, values['Pop']+values['Rock']/2), ha='center')
    ax.annotate(f"{values['Jazz']}", xy=(i, values['Pop']+values['Rock']+values['Jazz']/2), ha='center')

plt.tight_layout()
plt.show()