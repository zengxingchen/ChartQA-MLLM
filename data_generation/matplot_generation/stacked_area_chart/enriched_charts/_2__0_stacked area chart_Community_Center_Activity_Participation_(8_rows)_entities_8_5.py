
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

data_str = """Month,Cardio,Yoga,Strength Training
January,5000,3000,2000
February,5200,3200,2200
March,5400,3400,2400
April,5600,3600,2600
May,5800,3800,2800
June,6000,4000,3000
July,6200,4200,3200
August,6400,4400,3400
September,6600,4600,3600
October,6800,4800,3800
November,7000,5000,4000
December,7200,5200,4200
January,7400,5400,4400
February,7600,5600,4600
March,7800,5800,4800
April,8000,6000,5000
May,8200,6200,5200
June,8400,6400,5400
July,8600,6600,5600
August,8800,6800,5800
September,9000,7000,6000
October,9200,7200,6200
November,9400,7400,6400
December,9600,7600,6600"""

data = pd.read_csv(StringIO(data_str), index_col='Month')

x = data.index
y = [data['Cardio'], data['Yoga'], data['Strength Training']]

fig, ax = plt.subplots(figsize=(12, 8))

ax.stackplot(x, y, labels=['Cardio', 'Yoga', 'Strength Training'], colors=['#FF6347', '#4682B4', '#32CD32'])

ax.set_title('Monthly Fitness Activity Participation (in Hours)', pad=20)
ax.set_xlabel('Month')
ax.set_ylabel('Hours')
ax.legend(loc='upper right')

for i, (month, values) in enumerate(data.iterrows()):
    ax.annotate(f"{values['Cardio']}", xy=(i, values['Cardio']/2), ha='center')
    ax.annotate(f"{values['Yoga']}", xy=(i, values['Cardio']+values['Yoga']/2), ha='center')
    ax.annotate(f"{values['Strength Training']}", xy=(i, values['Cardio']+values['Yoga']+values['Strength Training']/2), ha='center')

plt.tight_layout()
plt.show()