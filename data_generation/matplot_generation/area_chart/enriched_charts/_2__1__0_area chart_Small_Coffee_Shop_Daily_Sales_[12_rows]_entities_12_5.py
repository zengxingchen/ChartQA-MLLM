
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Date": pd.date_range(start="2023-01-01", end="2023-01-31"),
    "Calories": [
        1200, 1250, 1300, 1400, 1350, 1500, 1550, 1600, 1580, 1650, 
        1700, 1750, 1800, 1850, 1900, 1950, 2000, 2050, 2100, 2150, 
        2200, 2250, 2300, 2350, 2400, 2450, 2500, 2550, 2600, 2650, 
        2700
    ]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 7))
plt.fill_between(df["Date"], df["Calories"], color="#FF6347", alpha=0.6)

plt.title("Daily Caloric Intake in January 2023", fontsize=18, pad=20)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Calories (kcal)", fontsize=14)

max_calories = df["Calories"].max()
max_date = df.loc[df["Calories"].idxmax(), "Date"]
plt.annotate(f"Peak: {max_calories} kcal", xy=(max_date, max_calories), xytext=(max_date, max_calories+300),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

plt.show()