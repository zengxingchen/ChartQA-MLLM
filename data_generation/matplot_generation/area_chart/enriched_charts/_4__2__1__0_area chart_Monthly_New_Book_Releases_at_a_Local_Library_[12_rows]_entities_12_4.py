
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "Page Views": [1500, 1700, 1800, 2100, 2400, 2000, 2600, 2700, 3000, 3100, 3300, 3500]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(16, 10))
plt.fill_between(df["Month"], df["Page Views"], color="#1f77b4", alpha=0.7)
plt.plot(df["Month"], df["Page Views"], color="#ff7f0e", linewidth=2)

# Title and labels
plt.title("Monthly Page Views for 2023", fontsize=20, pad=25)
plt.xlabel("Month", fontsize=15)
plt.ylabel("Page Views", fontsize=15)

# Annotation
for i, txt in enumerate(df["Page Views"]):
    plt.annotate(txt, (df["Month"][i], df["Page Views"][i]), textcoords="offset points", xytext=(0,8), ha='center')

plt.tight_layout()
plt.savefig("monthly_page_views_area_chart.png")
plt.show()