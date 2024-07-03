
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

data = StringIO("""
Day,Average Temperature (°C)
1,15.2
2,15.5
3,15.9
4,16.1
5,16.4
6,16.8
7,17.0
8,17.2
9,17.5
10,17.8
11,18.0
12,18.2
13,18.5
14,18.9
15,19.1
16,19.3
17,19.7
18,20.0
19,20.2
20,20.5
21,20.9
22,21.1
23,21.4
24,21.8
25,22.0
26,22.3
27,22.7
28,22.9
29,23.2
30,23.5
31,23.7
""")

df = pd.read_csv(data)

plt.figure(figsize=(12, 6))
plt.fill_between(df['Day'], df['Average Temperature (°C)'], color="#3498db", alpha=0.5)
plt.plot(df['Day'], df['Average Temperature (°C)'], color="#2980b9")

plt.title('Average Daily Temperature Over a Month')
plt.xlabel('Day of the Month')
plt.ylabel('Average Temperature (°C)')

max_temp_day = df['Average Temperature (°C)'].idxmax()  # find the day with max temp
plt.annotate('Highest', xy=(df.iloc[max_temp_day, 0], df.iloc[max_temp_day, 1]), 
             xytext=(df.iloc[max_temp_day, 0]+1, df.iloc[max_temp_day, 1]),
             arrowprops=dict(facecolor='#333333', shrink=0.05))

plt.grid(True)

plt.show()