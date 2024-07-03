
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

data = """Month,Weekly Workout Hours
January,10
February,12
March,14
April,16
May,18
June,20
July,22
August,24
September,21
October,19
November,17
December,15"""

df = pd.read_csv(StringIO(data))

plt.figure(figsize=(16, 10))

plt.fill_between(df['Month'], df['Weekly Workout Hours'], color="#1E90FF", alpha=0.8)

plt.title("Monthly Average Weekly Workout Hours in 2023", fontsize=18, fontweight='bold', y=1.03)
plt.xlabel("Month", fontsize=14)
plt.ylabel("Weekly Workout Hours", fontsize=14)

for idx, row in df.iterrows():
    plt.text(idx, row['Weekly Workout Hours'], f"{row['Weekly Workout Hours']}", ha='center', va='bottom')

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()