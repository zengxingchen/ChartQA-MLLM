
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Date": pd.date_range(start="2023-01-01", end="2023-01-31"),
    "Happiness Index": [68, 70, 72, 71, 74, 77, 75, 80, 78, 82, 85, 83, 88, 90, 92, 91, 95, 97, 96, 99, 100, 102, 105, 104, 108, 110, 112, 114, 115, 118, 120]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 7))
plt.fill_between(df["Date"], df["Happiness Index"], color="#FF5733", alpha=0.8)

plt.title("Daily Happiness Index in January 2023", fontsize=18, pad=20)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Happiness Index", fontsize=14)

max_value = df["Happiness Index"].max()
max_date = df.loc[df["Happiness Index"].idxmax(), "Date"]
plt.annotate(f"Peak: {max_value}", xy=(max_date, max_value), xytext=(max_date, max_value+5),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

plt.show()