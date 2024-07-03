
import matplotlib.pyplot as plt

# Data
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
popularity_scores = [35, 40, 45, 50, 55, 60, 70, 75, 80, 85, 60, 50]

# Plot
fig, ax = plt.subplots(figsize=(16, 10))

ax.fill_between(months, popularity_scores, color="#FFA07A", alpha=0.6)
ax.plot(months, popularity_scores, color="#FF4500", alpha=0.8)

# Title and labels
plt.title("Monthly Popularity Scores of a Music Genre in 2023", fontsize=20, pad=25)
plt.xlabel("Month", fontsize=16)
plt.ylabel("Popularity Score", fontsize=16)

# Annotations
for i, score in enumerate(popularity_scores):
    ax.text(i, score + 1, str(score), ha='center', fontsize=12)

# Display
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()