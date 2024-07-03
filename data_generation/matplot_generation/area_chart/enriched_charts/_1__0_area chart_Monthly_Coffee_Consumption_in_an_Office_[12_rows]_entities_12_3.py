
import matplotlib.pyplot as plt

# Data
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
values = [80, 95, 78, 85, 110, 120, 105, 115, 90, 95, 130, 140]

# Plot
fig, ax = plt.subplots(figsize=(12, 8))

ax.fill_between(months, values, color="#FF6347", alpha=0.7)
ax.plot(months, values, color="#FF4500", alpha=0.9)

# Title and labels
plt.title("Monthly Health Index in 2023", fontsize=16)
plt.xlabel("Month", fontsize=14)
plt.ylabel("Health Index", fontsize=14)

# Annotations
for i, value in enumerate(values):
    ax.text(i, value + 2, str(value), ha='center', fontsize=10)

# Display
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()