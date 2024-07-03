
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    "Day": list(range(1, 31)),
    "Steps": [3000, 4000, 5000, 5500, 4800, 6200, 7000, 7500, 8000, 7800, 8200, 8600, 9000, 9500, 10000, 10200, 10500, 10800, 11000, 11500, 12000, 12500, 13000, 13500, 14000, 14500, 15000, 15500, 16000, 16500]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plot
fig, ax = plt.subplots(figsize=(12, 8))
ax.fill_between(df["Day"], df["Steps"], color="#1f77b4", alpha=0.7)

# Customizations
ax.set_title("Daily Steps Count Over a Month", fontsize=18, pad=20)
ax.set_xlabel("Day", fontsize=14)
ax.set_ylabel("Steps", fontsize=14)
ax.grid(True, linestyle='--', alpha=0.5)

# Annotations
for i, txt in enumerate(df["Steps"]):
    ax.annotate(txt, (df["Day"][i], df["Steps"][i]), textcoords="offset points", xytext=(0,5), ha='center')

plt.show()