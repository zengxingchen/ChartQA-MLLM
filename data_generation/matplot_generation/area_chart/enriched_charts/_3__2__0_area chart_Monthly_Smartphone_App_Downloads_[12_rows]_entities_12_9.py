
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

data = """Day,Revenue
1,500
2,520
3,530
4,550
5,600
6,610
7,620
8,650
9,680
10,700
11,720
12,740
13,750
14,760
15,770
16,800
17,820
18,830
19,850
20,860
21,870
22,880
23,900
24,920
25,930
26,940
27,950
28,960
29,980
30,990
31,1000"""

data = pd.read_csv(StringIO(data))

fig, ax = plt.subplots(figsize=(16, 10))

ax.fill_between(data['Day'], data['Revenue'], color="#33A1FF", alpha=0.7)

ax.set_xlabel('Day of the Month', fontsize=14)
ax.set_ylabel('Daily Revenue (USD)', fontsize=14)
ax.set_title('Daily Revenue in May', fontsize=18, pad=30)

for i in range(len(data)):
    ax.text(data['Day'][i], data['Revenue'][i], str(data['Revenue'][i]), ha='center', va='bottom', fontsize=10)

plt.show()