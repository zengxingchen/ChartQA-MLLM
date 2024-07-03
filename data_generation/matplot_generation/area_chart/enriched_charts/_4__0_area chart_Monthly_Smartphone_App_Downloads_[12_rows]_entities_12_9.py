
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

csv_data = """Day,Page Views
1,134
2,145
3,156
4,160
5,155
6,170
7,180
8,165
9,175
10,190
11,185
12,195
13,200
14,210
15,220
16,215
17,225
18,230
19,240
20,235
21,245
22,255
23,250
24,260
25,265
26,275
27,280
28,290
29,285
30,295
31,300"""

data = pd.read_csv(StringIO(csv_data))

fig, ax = plt.subplots(figsize=(10, 5))

ax.fill_between(data['Day'], data['Page Views'], color="#5A9", alpha=0.6)

ax.set_xlabel('Day of the Month', fontsize=12)
ax.set_ylabel('Page Views', fontsize=12)
ax.set_title('Daily Page Views on a Blog Over a Month', fontsize=16)

ax.text(15, 250, 'Mid-Month Spike', fontsize=10, color='blue', ha='center')

plt.show()