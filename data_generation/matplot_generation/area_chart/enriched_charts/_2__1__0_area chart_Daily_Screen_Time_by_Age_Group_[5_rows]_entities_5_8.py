
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Day": list(range(1, 31)),
    "Temperature": [15, 17, 14, 19, 21, 22, 20, 18, 25, 27, 23, 21, 24, 26, 29, 31, 30, 28, 32, 33, 35, 36, 34, 37, 39, 40, 38, 35, 37, 39]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(14, 9))
ax.fill_between(df["Day"], df["Temperature"], color="#FF5733", alpha=0.7)

ax.set_title("Daily Temperature Variation Over a Month", fontsize=18, pad=20, loc='left')
ax.set_xlabel("Day", fontsize=14)
ax.set_ylabel("Temperature (°C)", fontsize=14)
ax.grid(True, linestyle='--', alpha=0.5)

for i, txt in enumerate(df["Temperature"]):
    ax.annotate(txt, (df["Day"][i], df["Temperature"][i]), textcoords="offset points", xytext=(0,5), ha='center')

plt.show()