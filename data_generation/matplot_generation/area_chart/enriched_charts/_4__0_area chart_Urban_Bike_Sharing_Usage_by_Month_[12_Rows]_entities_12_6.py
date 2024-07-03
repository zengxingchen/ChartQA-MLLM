
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

data = """Date,Daily Active Users
2024-01-01,500
2024-01-02,450
2024-01-03,470
2024-01-04,530
2024-01-05,510
2024-01-06,520
2024-01-07,480
2024-01-08,495
2024-01-09,505
2024-01-10,515
2024-01-11,525
2024-01-12,535
2024-01-13,540
2024-01-14,550
2024-01-15,560
2024-01-16,570
2024-01-17,580
2024-01-18,590
2024-01-19,600
2024-01-20,610
2024-01-21,620
2024-01-22,630
2024-01-23,640
2024-01-24,650
2024-01-25,660
2024-01-26,670
2024-01-27,680
2024-01-28,690
2024-01-29,700
2024-01-30,710
2024-01-31,720"""

df = pd.read_csv(StringIO(data))

plt.figure(figsize=(14, 7))

plt.fill_between(df['Date'], df['Daily Active Users'], color="#1f77b4", alpha=0.6)

plt.title("Daily Active Users in January 2024", fontsize=16, fontweight='bold', loc='left')
plt.xlabel("Date")
plt.ylabel("Daily Active Users")

for i, row in df.iterrows():
    plt.text(row['Date'], row['Daily Active Users'] + 10, str(row['Daily Active Users']), ha='center')

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()