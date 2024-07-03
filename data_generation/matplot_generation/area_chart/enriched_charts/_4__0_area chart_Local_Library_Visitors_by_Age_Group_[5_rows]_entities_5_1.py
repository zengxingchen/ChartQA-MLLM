import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

data = StringIO("""
Day,Average Steps
1,4000
2,4200
3,4100
4,4300
5,4400
6,4500
7,4600
8,4700
9,4800
10,5000
11,5200
12,5400
13,5600
14,5800
15,6000
16,6200
17,6400
18,6600
19,6800
20,7000
21,7200
22,7400
23,7600
24,7800
25,8000
26,8200
27,8400
28,8600
29,8800
30,9000
31,9200
""")

df = pd.read_csv(data)

plt.figure(figsize=(14, 7))
plt.fill_between(df['Day'], df['Average Steps'], color="#FF5733", alpha=0.6)
plt.plot(df['Day'], df['Average Steps'], color="#C70039")

plt.title('Average Daily Steps Over a Month', fontsize=16)
plt.xlabel('Day of the Month')
plt.ylabel('Average Steps')

max_steps_day = df['Average Steps'].idxmax()
plt.annotate('Peak Activity', xy=(df.iloc[max_steps_day, 0], df.iloc[max_steps_day, 1]), 
             xytext=(df.iloc[max_steps_day, 0]-2, df.iloc[max_steps_day, 1]+500),
             arrowprops=dict(facecolor='#900C3F', shrink=0.05))

plt.grid(True)

plt.show()