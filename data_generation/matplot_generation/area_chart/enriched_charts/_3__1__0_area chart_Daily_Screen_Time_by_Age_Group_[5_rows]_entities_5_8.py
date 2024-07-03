
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    "Day": list(range(1, 31)),
    "Distance": [5.2, 6.0, 6.8, 7.1, 6.9, 7.5, 8.0, 8.3, 8.7, 8.5, 9.0, 9.2, 9.6, 9.9, 10.1, 10.5, 10.8, 11.0, 11.3, 11.7, 12.0, 12.3, 12.8, 13.0, 13.5, 13.7, 14.0, 14.5, 14.8, 15.0]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plot
fig, ax = plt.subplots(figsize=(14, 9))
ax.fill_between(df["Day"], df["Distance"], color="#ff5733", alpha=0.7)

# Customizations
ax.set_title("Daily Distance Covered Over a Month", fontsize=20, pad=20)
ax.set_xlabel("Day", fontsize=16)
ax.set_ylabel("Distance (km)", fontsize=16)
ax.grid(True, linestyle='--', alpha=0.5)

# Annotations
for i, txt in enumerate(df["Distance"]):
    ax.annotate(txt, (df["Day"][i], df["Distance"][i]), textcoords="offset points", xytext=(0,5), ha='center')

plt.show()