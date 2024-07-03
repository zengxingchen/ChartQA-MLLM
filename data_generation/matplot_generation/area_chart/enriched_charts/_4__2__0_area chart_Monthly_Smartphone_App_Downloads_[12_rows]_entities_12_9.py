import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

data = """Day,Calories Burned
1,500
2,520
3,515
4,530
5,540
6,550
7,560
8,580
9,590
10,600
11,610
12,605
13,615
14,620
15,630
16,640
17,645
18,655
19,660
20,670
21,680
22,690
23,700
24,710
25,720
26,725
27,730
28,735
29,740
30,750
31,760"""

data = pd.read_csv(StringIO(data))

fig, ax = plt.subplots(figsize=(16, 10))

ax.fill_between(data['Day'], data['Calories Burned'], color="#33A2FF", alpha=0.7)

ax.set_xlabel('Day of the Month', fontsize=14)
ax.set_ylabel('Calories Burned', fontsize=14)
ax.set_title('Daily Calories Burned in Fitness Regime', fontsize=18, pad=20)

for i in range(len(data)):
    ax.text(data['Day'][i], data['Calories Burned'][i], str(data['Calories Burned'][i]), ha='center', va='bottom', fontsize=9)

plt.show()