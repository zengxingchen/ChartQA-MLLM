
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

data = StringIO("""
Month,Global Population Growth Rate (%)
1,1.05
2,1.08
3,1.10
4,1.15
5,1.20
6,1.25
7,1.22
8,1.18
9,1.15
10,1.12
11,1.10
12,1.08
""")

df = pd.read_csv(data)

plt.figure(figsize=(16, 8))
plt.fill_between(df['Month'], df['Global Population Growth Rate (%)'], color="#ff5733", alpha=0.6)
plt.plot(df['Month'], df['Global Population Growth Rate (%)'], color="#c70039")

plt.title('Monthly Global Population Growth Rate Over a Year', pad=20)
plt.xlabel('Month')
plt.ylabel('Global Population Growth Rate (%)')

max_growth_month = df['Global Population Growth Rate (%)'].idxmax()
plt.annotate('Peak Growth', xy=(df.iloc[max_growth_month, 0], df.iloc[max_growth_month, 1]), 
             xytext=(df.iloc[max_growth_month, 0]+1, df.iloc[max_growth_month, 1]+0.02),
             arrowprops=dict(facecolor='#333333', shrink=0.05))

plt.grid(True)

plt.show()