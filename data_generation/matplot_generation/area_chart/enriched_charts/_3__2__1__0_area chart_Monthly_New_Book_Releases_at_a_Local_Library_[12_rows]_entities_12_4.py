
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    "Day": list(range(1, 31)),
    "Stars": [100, 120, 130, 110, 140, 150, 160, 155, 170, 180,
              175, 190, 195, 200, 210, 220, 215, 230, 240, 235,
              250, 260, 255, 270, 280, 275, 290, 300, 295, 310]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(16, 10))
plt.fill_between(df["Day"], df["Stars"], color="#3498db", alpha=0.6)
plt.plot(df["Day"], df["Stars"], color="#1f618d", linewidth=2)

# Title and labels
plt.title("Monthly Star Count Observations for June 2023", fontsize=20, pad=25)
plt.xlabel("Day", fontsize=16)
plt.ylabel("Stars Observed", fontsize=16)

# Annotation
for i, txt in enumerate(df["Stars"]):
    plt.annotate(txt, (df["Day"][i], df["Stars"][i]), textcoords="offset points", xytext=(0,8), ha='center')

plt.tight_layout()
plt.savefig("monthly_star_count_area_chart.png")
plt.show()