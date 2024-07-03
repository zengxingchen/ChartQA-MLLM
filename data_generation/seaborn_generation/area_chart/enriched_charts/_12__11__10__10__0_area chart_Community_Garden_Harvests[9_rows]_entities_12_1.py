
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    "Date": ["2024-01-01", "2024-02-01", "2024-03-01", "2024-04-01", "2024-05-01", 
             "2024-06-01", "2024-07-01", "2024-08-01", "2024-09-01", "2024-10-01",
             "2024-11-01", "2024-12-01"],
    "Sales": [150, 200, 250, 300, 350, 320, 370, 390, 420, 460, 480, 500]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(12, 6))
sns.set(style="whitegrid")
area_chart = sns.lineplot(x="Date", y="Sales", data=df, color="#1f77b4", linewidth=2.5)
area_chart.fill_between(df["Date"], df["Sales"], color="#1f77b4", alpha=0.3)

# Title and labels
plt.title("Monthly Sales Over 2024", fontsize=18, pad=20)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Sales", fontsize=14)

# Annotations
for i in range(df.shape[0]):
    plt.text(df["Date"][i], df["Sales"][i], df["Sales"][i], ha='center', va='bottom')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()