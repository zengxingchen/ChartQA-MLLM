
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

data = StringIO("""
Month,Average Monthly Rainfall (mm)
1,78
2,85
3,92
4,105
5,120
6,130
7,140
8,135
9,120
10,110
11,90
12,80
""")

df = pd.read_csv(data)

plt.figure(figsize=(18, 10))
plt.fill_between(df['Month'], df['Average Monthly Rainfall (mm)'], color="#FF6347", alpha=0.6)
plt.plot(df['Month'], df['Average Monthly Rainfall (mm)'], color="#8B0000")

plt.title('Average Monthly Rainfall Over a Year', pad=20)
plt.xlabel('Month')
plt.ylabel('Average Monthly Rainfall (mm)')

max_rainfall_month = df['Average Monthly Rainfall (mm)'].idxmax()
plt.annotate('Highest Rainfall', xy=(df.iloc[max_rainfall_month, 0], df.iloc[max_rainfall_month, 1]), 
             xytext=(df.iloc[max_rainfall_month, 0]+1, df.iloc[max_rainfall_month, 1]+10),
             arrowprops=dict(facecolor='#333333', shrink=0.05))

plt.grid(True)

plt.show()