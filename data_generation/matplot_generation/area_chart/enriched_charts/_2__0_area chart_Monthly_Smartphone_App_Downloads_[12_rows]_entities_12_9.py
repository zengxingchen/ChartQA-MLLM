import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

data = """Day,Temperature
1,16
2,18
3,17
4,21
5,22
6,23
7,24
8,26
9,27
10,28
11,30
12,29
13,31
14,30
15,32
16,33
17,34
18,33
19,35
20,34
21,36
22,37
23,36
24,38
25,37
26,39
27,38
28,40
29,41
30,40
31,42"""

data = pd.read_csv(StringIO(data))

fig, ax = plt.subplots(figsize=(14, 8))

ax.fill_between(data['Day'], data['Temperature'], color="#FFAA33", alpha=0.7)

ax.set_xlabel('Day of the Month', fontsize=12)
ax.set_ylabel('Daily High Temperature (°C)', fontsize=12)
ax.set_title('Daily High Temperatures in June', fontsize=16, pad=20)

for i in range(len(data)):
    ax.text(data['Day'][i], data['Temperature'][i], str(data['Temperature'][i]), ha='center', va='bottom', fontsize=8)

plt.show()