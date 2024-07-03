
import matplotlib.pyplot as plt

# Data
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
visitors = [420, 480, 450, 500, 540, 600, 580, 620, 590, 630, 700, 750]

# Plot
fig, ax = plt.subplots(figsize=(14, 10))

ax.fill_between(months, visitors, color="#87CEEB", alpha=0.7)
ax.plot(months, visitors, color="#4682B4", alpha=0.9)

# Title and labels
plt.title("Monthly Visitor Statistics for 2023", fontsize=18)
plt.xlabel("Month", fontsize=15)
plt.ylabel("Number of Visitors", fontsize=15)

# Annotations
for i, value in enumerate(visitors):
    ax.text(i, value + 10, str(value), ha='center', fontsize=12)

# Display
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()