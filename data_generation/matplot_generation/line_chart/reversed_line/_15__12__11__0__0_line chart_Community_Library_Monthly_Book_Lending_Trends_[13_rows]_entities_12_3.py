
import matplotlib.pyplot as plt

# Data
dates = [
    "2024-01", "2024-02", "2024-03", "2024-04", "2024-05", "2024-06", "2024-07", "2024-08",
    "2024-09", "2024-10", "2024-11", "2024-12", "2025-01", "2025-02", "2025-03", "2025-04",
    "2025-05", "2025-06", "2025-07", "2025-08", "2025-09", "2025-10"
]
pollution_level = [
    42, 40, 38, 36, 35, 33, 34, 32, 30, 29, 27, 26, 25, 24, 22, 21, 20, 19, 18, 17, 16, 15
]

# Create the plot
plt.figure(figsize=(16, 8))  # Change the size of the chart
plt.plot(dates, pollution_level, marker='s', color="#228B22", linewidth=2)  # Change color and add markers

# Annotations
for i, level in enumerate(pollution_level):
    plt.annotate(f"{level}", (dates[i], level), textcoords="offset points", xytext=(0, 5),
                 ha='center', color="#8B0000")

# Improve the visual appeal with labels, title, and grid
plt.xlabel('Date')
plt.ylabel('Pollution Level (AQI)')
plt.title('Bi-Monthly Pollution Level in 2024-2025', pad=20)
plt.grid(True)
plt.gca().invert_yaxis()

# Show the plot
plt.show()