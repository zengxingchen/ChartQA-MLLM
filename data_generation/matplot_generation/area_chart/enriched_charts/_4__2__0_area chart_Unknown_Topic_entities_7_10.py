
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Date": pd.date_range(start="2023-01-01", end="2023-01-31"),
    "Daily_Steps": [
        5000, 4800, 5500, 6000, 6500, 7000, 7200, 6800, 6900, 7100, 7300, 7400, 7500, 
        7800, 8000, 8200, 8500, 8700, 9000, 9200, 9400, 9600, 9800, 10000, 10200, 
        10500, 10700, 11000, 11200, 11500, 11700
    ]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 8))
plt.fill_between(df["Date"], df["Daily_Steps"], color='#FF5733')

plt.title('Daily Step Count in January', fontsize=20, pad=20)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Daily Steps', fontsize=14)

for i, steps in enumerate(df["Daily_Steps"]):
    plt.text(df["Date"][i], steps + 200, str(steps), ha='center', va='bottom', fontsize=9)

plt.grid(True, color='#e6e6e6', linestyle='-', linewidth=0.7, which='both')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()