
import matplotlib.pyplot as plt

# Data
days = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7", "Day 8", "Day 9", "Day 10",
        "Day 11", "Day 12", "Day 13", "Day 14", "Day 15", "Day 16", "Day 17", "Day 18", "Day 19", "Day 20",
        "Day 21", "Day 22", "Day 23", "Day 24", "Day 25", "Day 26", "Day 27", "Day 28", "Day 29", "Day 30", "Day 31"]
visitors = [120, 130, 140, 145, 150, 160, 170, 175, 180, 185, 190, 200, 210, 220, 225, 230, 235, 240, 245, 250,
            260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360]

# Plot
fig, ax = plt.subplots(figsize=(16, 10))

ax.fill_between(days, visitors, color="#FF6347", alpha=0.6)
ax.plot(days, visitors, color="#8B0000", alpha=0.8)

# Title and labels
plt.title("Daily Visitors in June 2024", fontsize=18, pad=20)
plt.xlabel("Day", fontsize=14)
plt.ylabel("Number of Visitors", fontsize=14)

# Annotations
for i, visitor in enumerate(visitors):
    ax.text(i, visitor + 5, str(visitor), ha='center', fontsize=10)

# Display
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()