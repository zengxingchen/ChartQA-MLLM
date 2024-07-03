
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

csv_data = """Month,Novels,Short Stories,Poems
January,5000,3000,2000
February,5500,3200,2200
March,6000,3400,2400
April,6500,3600,2600
May,7000,3800,2800
June,7500,4000,3000
July,8000,4200,3200
August,8500,4400,3400
September,9000,4600,3600
October,9500,4800,3800
November,10000,5000,4000
December,10500,5200,4200
"""

data = pd.read_csv(StringIO(csv_data), index_col='Month')

x = data.index
y = [data['Novels'], data['Short Stories'], data['Poems']]

fig, ax = plt.subplots(figsize=(16, 10))

ax.stackplot(x, y, labels=['Novels', 'Short Stories', 'Poems'], colors=['#FF4500', '#1E90FF', '#32CD32'])

ax.set_title('Monthly Literature Production (in Units)', fontsize=18, pad=20)
ax.set_xlabel('Month')
ax.set_ylabel('Production Volume')
ax.legend(loc='upper left')

for i, (month, values) in enumerate(data.iterrows()):
    ax.annotate(f"{values['Novels']}", xy=(i, values['Novels']/2), ha='center', fontsize=9, color='white')
    ax.annotate(f"{values['Short Stories']}", xy=(i, values['Novels']+values['Short Stories']/2), ha='center', fontsize=9, color='white')
    ax.annotate(f"{values['Poems']}", xy=(i, values['Novels']+values['Short Stories']+values['Poems']/2), ha='center', fontsize=9, color='white')

plt.tight_layout()
plt.show()