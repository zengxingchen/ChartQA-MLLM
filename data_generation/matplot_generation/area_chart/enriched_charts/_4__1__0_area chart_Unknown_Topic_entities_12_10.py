
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Revenue': [1020, 1250, 1430, 1690, 1840, 2070, 2300, 2150, 1990, 1760, 1580, 1350]
}

df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(14, 8))
plt.fill_between(df['Month'], df['Revenue'], color='#FFA07A', alpha=0.7)
plt.plot(df['Month'], df['Revenue'], color='#FF4500', marker='o', markersize=6)

# Titles and labels
plt.title('Monthly Revenue for the Year', fontsize=18, pad=20)
plt.xlabel('Month', fontsize=15)
plt.ylabel('Revenue (USD)', fontsize=15)

# Annotations
for i, txt in enumerate(df['Revenue']):
    plt.annotate(f"${txt}", (df['Month'][i], df['Revenue'][i]), textcoords="offset points", xytext=(0,5), ha='center')

plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("monthly_revenue.png")
plt.show()