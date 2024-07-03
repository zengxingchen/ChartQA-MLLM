
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

csv_data = """Month,Proteins,Fats,Carbohydrates
January,60,30,210
February,62,32,215
March,65,33,220
April,68,35,225
May,70,36,230
June,72,38,235
July,75,40,240
August,78,42,245
September,80,43,250
October,82,45,255
November,85,47,260
December,88,50,265
"""

data = pd.read_csv(StringIO(csv_data), index_col='Month')

x = data.index
y = [data['Proteins'], data['Fats'], data['Carbohydrates']]

fig, ax = plt.subplots(figsize=(18, 12))

ax.stackplot(x, y, labels=['Proteins', 'Fats', 'Carbohydrates'], colors=['#8A2BE2', '#5F9EA0', '#FFD700'])

ax.set_title('Monthly Nutrient Intake (in Grams)', fontsize=20, pad=30)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Intake Volume (g)', fontsize=14)
ax.legend(loc='upper right')

for i, (month, values) in enumerate(data.iterrows()):
    ax.annotate(f"{values['Proteins']}", xy=(i, values['Proteins']/2), ha='center', fontsize=10, color='white')
    ax.annotate(f"{values['Fats']}", xy=(i, values['Proteins']+values['Fats']/2), ha='center', fontsize=10, color='white')
    ax.annotate(f"{values['Carbohydrates']}", xy=(i, values['Proteins']+values['Fats']+values['Carbohydrates']/2), ha='center', fontsize=10, color='white')

plt.tight_layout()
plt.show()