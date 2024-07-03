
import matplotlib.pyplot as plt
import pandas as pd

# Data
dates = [
    "2024-01", "2024-02", "2024-03", "2024-04", "2024-05", "2024-06", "2024-07", "2024-08",
    "2024-09", "2024-10", "2024-11", "2024-12", "2025-01", "2025-02", "2025-03", "2025-04",
    "2025-05", "2025-06", "2025-07", "2025-08", "2025-09", "2025-10"
]
tech_advances = [
    1, 3, 6, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 52, 48, 42, 35, 28, 20, 15, 10, 6
]

# Create the plot
plt.figure(figsize=(14, 7))  # Change the size of the chart
plt.plot(dates, tech_advances, marker='o', color="#2E8B57", linewidth=2)  # Change color and add markers

# Annotations
for i, advance in enumerate(tech_advances):
    plt.annotate(f"{advance}%", (dates[i], advance), textcoords="offset points", xytext=(0, 5),
                 ha='center', color="#FF4500")

# Improve the visual appeal with labels, title, and grid
plt.xlabel('Date')
plt.ylabel('Technological Advances (%)')
plt.title('Bi-Monthly Technological Advances in 2024-2025', pad=20)
plt.grid(True)

# Show the plot
plt.show()