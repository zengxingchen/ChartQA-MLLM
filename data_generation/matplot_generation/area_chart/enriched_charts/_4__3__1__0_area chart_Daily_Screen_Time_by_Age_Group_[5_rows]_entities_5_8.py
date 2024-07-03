
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    "Day": list(range(1, 31)),
    "Profit": [10.5, 11.2, 12.3, 13.1, 13.5, 14.8, 15.0, 16.3, 17.1, 18.4, 19.0, 19.7, 20.2, 21.5, 22.1, 23.0, 24.3, 25.1, 26.4, 27.0, 28.1, 29.0, 30.2, 31.1, 32.0, 33.3, 34.0, 35.1, 36.4, 37.0]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plot
fig, ax = plt.subplots(figsize=(16, 10))
ax.fill_between(df["Day"], df["Profit"], color="#3498db", alpha=0.8)

# Customizations
ax.set_title("Monthly Profit Analysis", fontsize=22, pad=25)
ax.set_xlabel("Day", fontsize=18)
ax.set_ylabel("Profit ($)", fontsize=18)
ax.grid(True, linestyle='--', alpha=0.6)

# Annotations
for i, txt in enumerate(df["Profit"]):
    ax.annotate(txt, (df["Day"][i], df["Profit"][i]), textcoords="offset points", xytext=(0,5), ha='center')

plt.show()