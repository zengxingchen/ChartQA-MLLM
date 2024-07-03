
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

data = '''
Date,Rainfall,Temperature
2024-01-01,5,22
2024-01-02,7,24
2024-01-03,6,23
2024-01-04,10,27
2024-01-05,8,25
2024-01-06,9,26
2024-01-07,12,29
2024-01-08,8,25
2024-01-09,15,31
2024-01-10,14,30
2024-01-11,16,32
2024-01-12,8,25
2024-01-13,18,34
2024-01-14,8,25
2024-01-15,20,36
2024-01-16,21,37
2024-01-17,19,35
2024-01-18,22,38
2024-01-19,20,36
2024-01-20,23,39
2024-01-21,25,40
2024-01-22,26,41
2024-01-23,24,39
2024-01-24,27,42
2024-01-25,28,43
2024-01-26,29,44
2024-01-27,27,42
2024-01-28,30,45
2024-01-29,32,47
2024-01-30,33,48
2024-01-31,35,50
'''

df = pd.read_csv(StringIO(data), parse_dates=['Date'])

plt.figure(figsize=(16, 10))

sns.scatterplot(data=df, x='Date', y='Temperature', size='Rainfall',
                sizes=(50, 500), hue='Rainfall', 
                palette=["#FF5733", "#33FF57", "#3357FF", "#F333FF", "#FF33A1", "#33FFD7", "#FFA833"])

plt.title('Daily Rainfall and Temperature', fontsize=20, y=1.02)
plt.xlabel('Date', fontsize=16)
plt.ylabel('Temperature (°C)', fontsize=16)

plt.show()