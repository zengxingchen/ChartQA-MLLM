
import matplotlib.pyplot as plt

# Data
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
apples = [350, 400, 370, 450, 520, 580, 560, 610, 590, 650, 700, 760]

# Plot
fig, ax = plt.subplots(figsize=(12, 8))

ax.fill_between(months, apples, color="#FFA07A", alpha=0.7)
ax.plot(months, apples, color="#FF4500", alpha=0.9)

# Title and labels
plt.title("Monthly Apple Sales for 2023", fontsize=20)
plt.xlabel("Month", fontsize=15)
plt.ylabel("Number of Apples Sold", fontsize=15)

# Annotations
for i, value in enumerate(apples):
    ax.text(i, value + 10, str(value), ha='center', fontsize=12)

# Display
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()