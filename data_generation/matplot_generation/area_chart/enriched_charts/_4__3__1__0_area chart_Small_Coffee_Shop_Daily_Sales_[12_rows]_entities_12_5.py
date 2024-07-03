
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Date": pd.date_range(start="2023-01-01", end="2023-01-31"),
    "Stress Level": [40, 42, 45, 44, 47, 50, 48, 53, 55, 57, 54, 60, 63, 65, 67, 69, 72, 70, 75, 78, 80, 82, 85, 88, 90, 92, 94, 97, 99, 100, 102]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 8))
plt.fill_between(df["Date"], df["Stress Level"], color="#1E90FF", alpha=0.7)

plt.title("Daily Stress Levels in January 2023", fontsize=20, pad=25)
plt.xlabel("Date", fontsize=15)
plt.ylabel("Stress Level", fontsize=15)

max_value = df["Stress Level"].max()
max_date = df.loc[df["Stress Level"].idxmax(), "Date"]
plt.annotate(f"Peak: {max_value}", xy=(max_date, max_value), xytext=(max_date, max_value+5),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

plt.show()