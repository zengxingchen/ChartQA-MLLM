
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Revenue': [50, 45, 60, 75, 85, 90, 95, 85, 70, 60, 55, 50]
}

df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(14, 7))
plt.fill_between(df['Month'], df['Revenue'], color='#FF5733', alpha=0.7)
plt.plot(df['Month'], df['Revenue'], color='#C70039', marker='o', markersize=6)

# Titles and labels
plt.title('Monthly Revenue for the Year', fontsize=18, pad=30)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Revenue (in thousands)', fontsize=14)

# Annotations
for i, txt in enumerate(df['Revenue']):
    plt.annotate(f"${txt}k", (df['Month'][i], df['Revenue'][i]), textcoords="offset points", xytext=(0,5), ha='center')

plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("monthly_revenue.png")
plt.show()