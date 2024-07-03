
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "Subscribers": [1200, 1500, 1700, 2000, 2400, 2800, 3000, 3200, 3100, 3500, 3700, 4000]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(14, 9))
plt.fill_between(df["Month"], df["Subscribers"], color="#e74c3c", alpha=0.7)
plt.plot(df["Month"], df["Subscribers"], color="#c0392b", linewidth=2)

# Title and labels
plt.title("Monthly YouTube Channel Subscribers for 2023", fontsize=18, pad=20)
plt.xlabel("Month", fontsize=14)
plt.ylabel("Subscribers", fontsize=14)

# Annotation
for i, txt in enumerate(df["Subscribers"]):
    plt.annotate(txt, (df["Month"][i], df["Subscribers"][i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.tight_layout()
plt.savefig("monthly_subscribers_area_chart.png")
plt.show()