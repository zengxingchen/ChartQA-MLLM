
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

data = StringIO("""
Month,Average Monthly Rainfall (mm)
1,78
2,85
3,90
4,120
5,150
6,200
7,180
8,170
9,160
10,130
11,100
12,90
""")

df = pd.read_csv(data)

plt.figure(figsize=(14, 7))
plt.fill_between(df['Month'], df['Average Monthly Rainfall (mm)'], color="#1abc9c", alpha=0.6)
plt.plot(df['Month'], df['Average Monthly Rainfall (mm)'], color="#16a085")

plt.title('Average Monthly Rainfall Over a Year', pad=20)
plt.xlabel('Month')
plt.ylabel('Average Monthly Rainfall (mm)')

max_rainfall_month = df['Average Monthly Rainfall (mm)'].idxmax()
plt.annotate('Highest Rainfall', xy=(df.iloc[max_rainfall_month, 0], df.iloc[max_rainfall_month, 1]), 
             xytext=(df.iloc[max_rainfall_month, 0]+1, df.iloc[max_rainfall_month, 1]+10),
             arrowprops=dict(facecolor='#333333', shrink=0.05))

plt.grid(True)

plt.show()