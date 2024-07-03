
import matplotlib.pyplot as plt

# Data
dates = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
revenue = [5000, 5200, 4800, 5300, 6000, 6300, 6100, 6500, 6200, 6700, 7000, 7300]

# Plot
fig, ax = plt.subplots(figsize=(14, 9))

ax.fill_between(dates, revenue, color="#1E90FF", alpha=0.6)
ax.plot(dates, revenue, color="#4169E1", alpha=0.8)

# Title and labels
plt.title("Monthly Revenue for 2023", fontsize=18)
plt.xlabel("Month", fontsize=14)
plt.ylabel("Revenue (USD)", fontsize=14)

# Annotations
for i, value in enumerate(revenue):
    ax.text(i, value + 100, str(value), ha='center', fontsize=10)

# Display
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()