
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

csv_data = """Month,Solar,Wind,Hydro
January,3000,8000,12000
February,3200,8500,12500
March,3500,9000,13000
April,3700,9500,13500
May,4000,10000,14000
June,4200,10500,14500
July,4500,11000,15000
August,4700,11500,15500
September,5000,12000,16000
October,5200,12500,16500
November,5500,13000,17000
December,5800,13500,17500
"""

data = pd.read_csv(StringIO(csv_data), index_col='Month')

x = data.index
y = [data['Solar'], data['Wind'], data['Hydro']]

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(x, y, labels=['Solar', 'Wind', 'Hydro'], colors=['#FFD700', '#1E90FF', '#32CD32'])

ax.set_title('Monthly Renewable Energy Production (in Megawatts)', fontsize=18, pad=20)
ax.set_xlabel('Month')
ax.set_ylabel('Energy Production (MW)')
ax.legend(loc='upper left')

for i, (month, values) in enumerate(data.iterrows()):
    ax.annotate(f"{values['Solar']}", xy=(i, values['Solar']/2), ha='center')
    ax.annotate(f"{values['Wind']}", xy=(i, values['Solar']+values['Wind']/2), ha='center')
    ax.annotate(f"{values['Hydro']}", xy=(i, values['Solar']+values['Wind']+values['Hydro']/2), ha='center')

plt.tight_layout()
plt.show()