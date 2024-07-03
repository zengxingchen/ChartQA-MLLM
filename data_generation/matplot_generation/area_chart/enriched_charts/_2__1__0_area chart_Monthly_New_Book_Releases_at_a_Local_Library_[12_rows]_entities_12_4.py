
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    "Day": list(range(1, 31)),
    "Steps": [3000, 3500, 4000, 3700, 4200, 4500, 4800, 5000, 4700, 4900, 
              5300, 5500, 5200, 5400, 5800, 6000, 5900, 6200, 6400, 6300, 
              6500, 6700, 6800, 6600, 6900, 7100, 7000, 7200, 7500, 7700]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(14, 9))
plt.fill_between(df["Day"], df["Steps"], color="#FF5733", alpha=0.6)
plt.plot(df["Day"], df["Steps"], color="#C70039", linewidth=2)

# Title and labels
plt.title("Daily Steps Count for June 2023", fontsize=18, pad=20)
plt.xlabel("Day", fontsize=15)
plt.ylabel("Steps", fontsize=15)

# Annotation
for i, txt in enumerate(df["Steps"]):
    plt.annotate(txt, (df["Day"][i], df["Steps"][i]), textcoords="offset points", xytext=(0,8), ha='center')

plt.tight_layout()
plt.savefig("daily_steps_area_chart.png")
plt.show()