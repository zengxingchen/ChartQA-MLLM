
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Date": pd.date_range(start="2023-01-01", end="2023-01-31"),
    "Value": [50, 53, 58, 54, 60, 65, 62, 68, 70, 75, 73, 78, 80, 85, 88, 82, 90, 95, 93, 98, 100, 105, 103, 108, 110, 115, 113, 118, 120, 125, 128]
}

df = pd.DataFrame(data)

plt.figure(figsize=(12, 6))
plt.fill_between(df["Date"], df["Value"], color="#4CAF50", alpha=0.7)

plt.title("Daily Energy Consumption in January 2023", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Energy Consumption (kWh)", fontsize=12)

# Adding an annotation
max_value = df["Value"].max()
max_date = df.loc[df["Value"].idxmax(), "Date"]
plt.annotate(f"Peak: {max_value} kWh", xy=(max_date, max_value), xytext=(max_date, max_value+10),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

plt.show()