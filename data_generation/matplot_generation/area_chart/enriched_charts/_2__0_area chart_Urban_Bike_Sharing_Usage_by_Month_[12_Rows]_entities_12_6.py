
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

data = """Date,Daily Active Users
2024-01-01,150
2024-01-02,200
2024-01-03,180
2024-01-04,220
2024-01-05,240
2024-01-06,230
2024-01-07,250
2024-01-08,270
2024-01-09,300
2024-01-10,320
2024-01-11,310
2024-01-12,330
2024-01-13,340
2024-01-14,350
2024-01-15,360
2024-01-16,370
2024-01-17,380
2024-01-18,390
2024-01-19,400
2024-01-20,410
2024-01-21,420
2024-01-22,430
2024-01-23,440
2024-01-24,450
2024-01-25,460
2024-01-26,470
2024-01-27,480
2024-01-28,490
2024-01-29,500
2024-01-30,510
2024-01-31,520"""

df = pd.read_csv(StringIO(data))

plt.figure(figsize=(14, 7))

plt.fill_between(df['Date'], df['Daily Active Users'], color="#4CAF50", alpha=0.7)

plt.title("Daily Active Users in January 2024", fontsize=16, fontweight='bold', loc='center')
plt.xlabel("Date")
plt.ylabel("Number of Active Users")

plt.xticks(rotation=45)
plt.tight_layout()

for i, row in df.iterrows():
    plt.text(row['Date'], row['Daily Active Users'] + 10, str(row['Daily Active Users']), color='black', fontsize=8, ha='center')

plt.show()