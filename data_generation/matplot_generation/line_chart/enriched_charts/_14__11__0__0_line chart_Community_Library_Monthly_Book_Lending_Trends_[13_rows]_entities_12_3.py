
import matplotlib.pyplot as plt
import pandas as pd

# Data
dates = [
    "2024-01", "2024-02", "2024-03", "2024-04", "2024-05", "2024-06", "2024-07", "2024-08",
    "2024-09", "2024-10", "2024-11", "2024-12", "2025-01", "2025-02", "2025-03", "2025-04",
    "2025-05", "2025-06", "2025-07", "2025-08", "2025-09", "2025-10"
]
artistry = [
    1, 3, 7, 12, 19, 26, 30, 34, 38, 42, 41, 38, 35, 31, 27, 23, 19, 15, 10, 6, 3, 1
]

# Create the plot
plt.figure(figsize=(14, 7))
plt.plot(dates, artistry, marker='s', color="#8A2BE2", linewidth=2)

# Annotations
for i, value in enumerate(artistry):
    plt.annotate(f"{value}%", (dates[i], value), textcoords="offset points", xytext=(0, 5),
                 ha='center', color="#228B22")

# Improve the visual appeal with labels, title, and grid
plt.xlabel('Date')
plt.ylabel('Artistry (%)')
plt.title('Bi-Monthly Artistry in 2024-2025', pad=20)
plt.grid(True)
plt.gca().invert_yaxis()  # Invert the y-axis

# Show the plot
plt.show()