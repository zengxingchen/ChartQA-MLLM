import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

data = """Date,Daily Downloads
2024-01-01,180
2024-01-02,210
2024-01-03,200
2024-01-04,240
2024-01-05,260
2024-01-06,250
2024-01-07,270
2024-01-08,300
2024-01-09,320
2024-01-10,310
2024-01-11,330
2024-01-12,350
2024-01-13,360
2024-01-14,370
2024-01-15,390
2024-01-16,410
2024-01-17,420
2024-01-18,430
2024-01-19,440
2024-01-20,460
2024-01-21,470
2024-01-22,480
2024-01-23,490
2024-01-24,500
2024-01-25,510
2024-01-26,520
2024-01-27,530
2024-01-28,540
2024-01-29,550
2024-01-30,560
2024-01-31,570"""

df = pd.read_csv(StringIO(data))

plt.figure(figsize=(16, 8))

plt.fill_between(df['Date'], df['Daily Downloads'], color="#FF5733", alpha=0.7)

plt.title("Daily App Downloads in January 2024", fontsize=18, fontweight='bold', loc='center')
plt.xlabel("Date", fontsize=12)
plt.ylabel("Number of Downloads", fontsize=12)

plt.xticks(rotation=45)
plt.tight_layout()

for i, row in df.iterrows():
    plt.text(row['Date'], row['Daily Downloads'] + 10, str(row['Daily Downloads']), color='black', fontsize=8, ha='center')

plt.show()