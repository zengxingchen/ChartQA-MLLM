
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

data = StringIO("""
Month,Average Monthly Temperature (°C)
1,5
2,7
3,10
4,15
5,20
6,25
7,30
8,28
9,24
10,18
11,10
12,6
""")

df = pd.read_csv(data)

plt.figure(figsize=(16, 8))
plt.fill_between(df['Month'], df['Average Monthly Temperature (°C)'], color="#3498db", alpha=0.6)
plt.plot(df['Month'], df['Average Monthly Temperature (°C)'], color="#2980b9")

plt.title('Average Monthly Temperatures Over a Year', pad=20)
plt.xlabel('Month')
plt.ylabel('Average Monthly Temperature (°C)')

max_temp_month = df['Average Monthly Temperature (°C)'].idxmax()
plt.annotate('Highest Temperature', xy=(df.iloc[max_temp_month, 0], df.iloc[max_temp_month, 1]), 
             xytext=(df.iloc[max_temp_month, 0]+1, df.iloc[max_temp_month, 1]+2),
             arrowprops=dict(facecolor='#333333', shrink=0.05))

plt.grid(True)

plt.show()