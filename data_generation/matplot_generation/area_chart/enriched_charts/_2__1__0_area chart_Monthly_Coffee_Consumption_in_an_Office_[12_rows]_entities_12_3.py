
import matplotlib.pyplot as plt

# Data
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
temperatures = [2, 4, 8, 12, 16, 20, 22, 21, 17, 12, 6, 3]

# Plot
fig, ax = plt.subplots(figsize=(14, 9))

ax.fill_between(months, temperatures, color="#4682B4", alpha=0.6)
ax.plot(months, temperatures, color="#00008B", alpha=0.8)

# Title and labels
plt.title("Average Monthly Temperatures in 2023", fontsize=18, pad=20)
plt.xlabel("Month", fontsize=14)
plt.ylabel("Temperature (°C)", fontsize=14)

# Annotations
for i, temperature in enumerate(temperatures):
    ax.text(i, temperature + 0.5, str(temperature), ha='center', fontsize=10)

# Display
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()