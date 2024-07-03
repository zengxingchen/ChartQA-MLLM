
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Date": pd.date_range(start="2023-01-01", end="2023-01-31"),
    "Steps": [
        5000, 5200, 4800, 5300, 5500, 6000, 6200, 6100, 6300, 6400,
        6500, 6600, 6700, 6800, 6900, 7000, 7100, 7200, 7300, 7400,
        7500, 7600, 7700, 7800, 7900, 8000, 8100, 8200, 8300, 8400, 
        8500
    ]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 8))
plt.fill_between(df["Date"], df["Steps"], color="#4682B4", alpha=0.6)

plt.title("Daily Steps in January 2023", fontsize=20, pad=30)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Steps", fontsize=14)

max_steps = df["Steps"].max()
max_date = df.loc[df["Steps"].idxmax(), "Date"]
plt.annotate(f"Peak: {max_steps} steps", xy=(max_date, max_steps), xytext=(max_date, max_steps+500),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

plt.show()