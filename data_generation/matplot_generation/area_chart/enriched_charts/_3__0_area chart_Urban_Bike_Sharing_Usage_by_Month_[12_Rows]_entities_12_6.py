
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

data = """Month,Daily Revenue ($)
January,5000
February,5200
March,5300
April,5400
May,5600
June,5800
July,6000
August,6200
September,6100
October,5900
November,5700
December,5500"""

df = pd.read_csv(StringIO(data))

plt.figure(figsize=(14, 8))

plt.fill_between(df['Month'], df['Daily Revenue ($)'], color="#4CAF50", alpha=0.7)

plt.title("Monthly Average Daily Revenue of Company Y", fontsize=16, fontweight='bold', y=1.05)
plt.xlabel("Month")
plt.ylabel("Daily Revenue ($)")

for idx, row in df.iterrows():
    plt.text(idx, row['Daily Revenue ($)'], f"{row['Daily Revenue ($)']}", ha='center', va='bottom')

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()