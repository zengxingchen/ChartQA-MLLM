
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Art Exhibition': [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310],
    'Theatre Performance': [150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260],
    'Music Concert': [180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290],
    'Dance Show': [130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240]
}

df = pd.DataFrame(data)
df.set_index('Month', inplace=True)

cumulative = df.cumsum(axis=1)

plt.figure(figsize=(14, 9))
pal = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8']
plt.stackplot(cumulative.index, cumulative['Art Exhibition'], cumulative['Theatre Performance'],
              cumulative['Music Concert'], cumulative['Dance Show'], labels=cumulative.columns, colors=pal)
plt.legend(loc='upper left')
plt.title('Monthly Attendance at Art Events')
plt.xlabel('Month')
plt.ylabel('Number of Attendees')
plt.annotate('Peak for Art Exhibition', xy=(10.5, cumulative.loc['November', 'Art Exhibition']-50),
             xytext=(9.5, cumulative.loc['November', 'Art Exhibition']+150),
             arrowprops=dict(facecolor='black', arrowstyle="->", connectionstyle="arc3"))
plt.annotate('Peak for Music Concert', xy=(11.5, cumulative.loc['December', 'Music Concert']),
             xytext=(10.5, cumulative.loc['December', 'Music Concert']+150),
             arrowprops=dict(facecolor='black', arrowstyle="->", connectionstyle="arc3"))
plt.annotate('Peak for Dance Show', xy=(11.5, cumulative.loc['December', 'Dance Show']),
             xytext=(10.5, cumulative.loc['December', 'Dance Show'] + cumulative.loc['December', 'Music Concert'] + 100),
             arrowprops=dict(facecolor='black', arrowstyle="->", connectionstyle="arc3"))
plt.tight_layout()
plt.show()