
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "Sales": [2500, 2700, 3000, 3200, 3500, 3800, 4100, 4300, 4000, 3700, 3400, 3200]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(12, 8))
plt.fill_between(df["Month"], df["Sales"], color="#3498db", alpha=0.7)
plt.plot(df["Month"], df["Sales"], color="#2980b9", linewidth=2)

# Title and labels
plt.title("Monthly Sales Data for 2023", fontsize=16, pad=20)
plt.xlabel("Month", fontsize=14)
plt.ylabel("Sales (in USD)", fontsize=14)

# Annotation
for i, txt in enumerate(df["Sales"]):
    plt.annotate(txt, (df["Month"][i], df["Sales"][i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.tight_layout()
plt.savefig("monthly_sales_area_chart.png")
plt.show()