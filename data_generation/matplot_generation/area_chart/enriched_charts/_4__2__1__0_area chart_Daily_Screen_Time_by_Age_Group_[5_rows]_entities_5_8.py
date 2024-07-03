
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Day": list(range(1, 32)),
    "Caloric_Intake": [
        2200, 2250, 2150, 2300, 2350, 2400, 2450, 2500, 2600, 2550,
        2700, 2750, 2800, 2850, 2900, 2950, 3000, 3050, 3100, 3150,
        3200, 3250, 3300, 3350, 3400, 3450, 3500, 3550, 3600, 3650,
        3700
    ]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(16, 10))
ax.fill_between(df["Day"], df["Caloric_Intake"], color="#4682B4", alpha=0.7)

ax.set_title("Daily Caloric Intake Over a Month", fontsize=18, pad=20, loc='left')
ax.set_xlabel("Day", fontsize=14)
ax.set_ylabel("Caloric Intake (kcal)", fontsize=14)
ax.grid(True, linestyle='--', alpha=0.5)

for i, txt in enumerate(df["Caloric_Intake"]):
    ax.annotate(txt, (df["Day"][i], df["Caloric_Intake"][i]), textcoords="offset points", xytext=(0,5), ha='center')

plt.show()