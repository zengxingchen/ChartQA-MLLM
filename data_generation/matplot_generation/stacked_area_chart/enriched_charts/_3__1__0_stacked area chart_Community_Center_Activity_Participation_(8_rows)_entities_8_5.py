
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

csv_data = """Month,Carbohydrates,Proteins,Fats
January,200,150,100
February,210,160,110
March,220,170,120
April,230,180,130
May,240,190,140
June,250,200,150
July,260,210,160
August,270,220,170
September,280,230,180
October,290,240,190
November,300,250,200
December,310,260,210
"""

data = pd.read_csv(StringIO(csv_data), index_col='Month')

x = data.index
y = [data['Carbohydrates'], data['Proteins'], data['Fats']]

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(x, y, labels=['Carbohydrates', 'Proteins', 'Fats'], colors=['#FF6347', '#4682B4', '#32CD32'])

ax.set_title('Monthly Nutrient Intake (in Grams)', fontsize=18, pad=20)
ax.set_xlabel('Month')
ax.set_ylabel('Intake (g)')
ax.legend(loc='upper right')

for i, (month, values) in enumerate(data.iterrows()):
    ax.annotate(f"{values['Carbohydrates']}", xy=(i, values['Carbohydrates']/2), ha='center', fontsize=8, color='white')
    ax.annotate(f"{values['Proteins']}", xy=(i, values['Carbohydrates']+values['Proteins']/2), ha='center', fontsize=8, color='white')
    ax.annotate(f"{values['Fats']}", xy=(i, values['Carbohydrates']+values['Proteins']+values['Fats']/2), ha='center', fontsize=8, color='white')

plt.tight_layout()
plt.show()