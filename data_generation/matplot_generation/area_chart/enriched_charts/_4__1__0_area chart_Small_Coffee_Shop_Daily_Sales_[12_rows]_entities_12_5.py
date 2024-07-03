
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Date": pd.date_range(start="2023-01-01", end="2023-01-31"),
    "Value": [70, 72, 75, 78, 80, 85, 90, 88, 92, 95, 100, 105, 110, 115, 118, 120, 125, 128, 130, 135, 140, 145, 150, 148, 153, 155, 160, 165, 168, 170, 175]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 8))
plt.fill_between(df["Date"], df["Value"], color="#FF5733", alpha=0.7)

plt.title("Daily Water Consumption in January 2023", fontsize=18)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Water Consumption (Liters)", fontsize=14)

max_value = df["Value"].max()
max_date = df.loc[df["Value"].idxmax(), "Date"]
plt.annotate(f"Peak: {max_value} Liters", xy=(max_date, max_value), xytext=(max_date, max_value+10),
             arrowprops=dict(facecolor='blue', shrink=0.05))

plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

plt.show()