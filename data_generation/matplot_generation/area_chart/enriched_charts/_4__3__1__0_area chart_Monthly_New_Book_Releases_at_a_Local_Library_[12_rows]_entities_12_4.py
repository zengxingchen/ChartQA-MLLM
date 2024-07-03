
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "Books_Read": [5, 7, 12, 10, 15, 18, 22, 19, 17, 14, 10, 8]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(16, 10))
plt.fill_between(df["Month"], df["Books_Read"], color="#3498db", alpha=0.7)
plt.plot(df["Month"], df["Books_Read"], color="#2980b9", linewidth=2)

# Title and labels
plt.title("Monthly Books Read in 2023", fontsize=20, pad=20, loc='center')
plt.xlabel("Month", fontsize=14)
plt.ylabel("Books Read", fontsize=14)

# Annotation
for i, txt in enumerate(df["Books_Read"]):
    plt.annotate(txt, (df["Month"][i], df["Books_Read"][i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.tight_layout()
plt.savefig("monthly_books_read_area_chart.png")
plt.show()