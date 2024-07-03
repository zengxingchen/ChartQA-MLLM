
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Date": pd.date_range(start="2023-01-01", end="2023-01-31"),
    "Water Intake (liters)": [
        2.0, 2.1, 2.2, 2.4, 2.3, 2.5, 2.7, 2.6, 2.8, 2.9,
        3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9,
        4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9,
        5.0
    ]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 8))
plt.fill_between(df["Date"], df["Water Intake (liters)"], color="#1E90FF", alpha=0.6)

plt.title("Daily Water Intake in January 2023", fontsize=20, pad=25)
plt.xlabel("Date", fontsize=15)
plt.ylabel("Water Intake (liters)", fontsize=15)

max_intake = df["Water Intake (liters)"].max()
max_date = df.loc[df["Water Intake (liters)"].idxmax(), "Date"]
plt.annotate(f"Peak: {max_intake} liters", xy=(max_date, max_intake), xytext=(max_date, max_intake + 1),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

plt.show()