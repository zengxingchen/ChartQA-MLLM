import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Date": pd.date_range(start="2023-01-01", end="2023-01-31"),
    "Temperature": [
        15, 14, 16, 13, 17, 18, 20, 19, 21, 22, 23, 20, 18, 19, 20, 21, 23, 24, 22, 21, 
        20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10
    ]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 7))
plt.fill_between(df["Date"], df["Temperature"], color='#1f77b4')

plt.title('Daily Temperature Variation in January', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)

for i, temp in enumerate(df["Temperature"]):
    plt.text(df["Date"][i], temp + 0.5, str(temp), ha='center', va='bottom', fontsize=8)

plt.grid(True, color='#e6e6e6', linestyle='-', linewidth=0.7, which='both')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()