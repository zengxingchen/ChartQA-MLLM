
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

data = StringIO("""
Day,Books Read
1,1
2,1
3,2
4,3
5,2
6,4
7,5
8,6
9,5
10,7
11,6
12,8
13,7
14,9
15,8
16,10
17,9
18,11
19,10
20,12
21,11
22,13
23,12
24,14
25,13
26,15
27,14
28,16
29,15
30,17
31,16
""")

df = pd.read_csv(data)

plt.figure(figsize=(16, 10))
plt.fill_between(df['Day'], df['Books Read'], color="#3498DB", alpha=0.6)
plt.plot(df['Day'], df['Books Read'], color="#1A5276")

plt.title('Books Read Over a Month', pad=20)
plt.xlabel('Day of the Month')
plt.ylabel('Books Read')

max_books_day = df['Books Read'].idxmax()
plt.annotate('Most Books Read', xy=(df.iloc[max_books_day, 0], df.iloc[max_books_day, 1]), 
             xytext=(df.iloc[max_books_day, 0]+2, df.iloc[max_books_day, 1]+1),
             arrowprops=dict(facecolor='#000000', shrink=0.05))

plt.grid(True)
plt.show()