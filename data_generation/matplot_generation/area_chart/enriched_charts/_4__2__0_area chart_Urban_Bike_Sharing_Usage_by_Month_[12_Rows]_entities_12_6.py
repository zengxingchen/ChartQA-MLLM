
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

data = """Date,Books Sold
2024-01-01,150
2024-01-02,210
2024-01-03,190
2024-01-04,230
2024-01-05,250
2024-01-06,240
2024-01-07,260
2024-01-08,280
2024-01-09,310
2024-01-10,330
2024-01-11,320
2024-01-12,340
2024-01-13,350
2024-01-14,360
2024-01-15,370
2024-01-16,380
2024-01-17,390
2024-01-18,400
2024-01-19,410
2024-01-20,420
2024-01-21,430
2024-01-22,440
2024-01-23,450
2024-01-24,460
2024-01-25,470
2024-01-26,480
2024-01-27,490
2024-01-28,500
2024-01-29,510
2024-01-30,520
2024-01-31,530"""

df = pd.read_csv(StringIO(data))

plt.figure(figsize=(16, 8))

plt.fill_between(df['Date'], df['Books Sold'], color="#FF5733", alpha=0.7)

plt.title("Books Sold in January 2024", fontsize=18, fontweight='bold', loc='left')
plt.xlabel("Date")
plt.ylabel("Number of Books Sold")

plt.xticks(rotation=45)
plt.tight_layout()

for i, row in df.iterrows():
    plt.text(row['Date'], row['Books Sold'] + 10, str(row['Books Sold']), color='black', fontsize=8, ha='center')

plt.show()