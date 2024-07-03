
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "Exercise_Hours": [10, 15, 20, 25, 30, 35, 40, 42, 38, 33, 28, 22]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(14, 9))
plt.fill_between(df["Month"], df["Exercise_Hours"], color="#2ecc71", alpha=0.7)
plt.plot(df["Month"], df["Exercise_Hours"], color="#27ae60", linewidth=2)

# Title and labels
plt.title("Monthly Exercise Hours in 2023", fontsize=18, pad=20)
plt.xlabel("Month", fontsize=14)
plt.ylabel("Exercise Hours", fontsize=14)

# Annotation
for i, txt in enumerate(df["Exercise_Hours"]):
    plt.annotate(txt, (df["Month"][i], df["Exercise_Hours"][i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.tight_layout()
plt.savefig("monthly_exercise_hours_area_chart.png")
plt.show()