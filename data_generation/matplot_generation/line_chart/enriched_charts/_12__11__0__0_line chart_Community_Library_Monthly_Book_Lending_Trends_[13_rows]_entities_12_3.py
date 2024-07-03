
import matplotlib.pyplot as plt

# Data
dates = [
    "2024-01", "2024-02", "2024-03", "2024-04", "2024-05", "2024-06", "2024-07", "2024-08",
    "2024-09", "2024-10", "2024-11", "2024-12", "2025-01", "2025-02", "2025-03", "2025-04",
    "2025-05", "2025-06", "2025-07", "2025-08", "2025-09", "2025-10"
]
unemployment_rate = [
    3.2, 3.4, 3.1, 3.5, 3.8, 3.7, 3.6, 3.9, 4.1, 4.3, 4.0, 3.8, 3.5, 3.4, 3.2, 3.3, 3.5, 3.7, 3.8, 3.9, 4.0, 4.2
]

# Create the plot
plt.figure(figsize=(18, 9))  # Change the size of the chart
plt.plot(dates, unemployment_rate, marker='o', color="#1E90FF", linewidth=2)  # Change color and add markers

# Annotations
for i, rate in enumerate(unemployment_rate):
    plt.annotate(f"{rate}%", (dates[i], rate), textcoords="offset points", xytext=(0, 5),
                 ha='center', color="#FF4500")

# Improve the visual appeal with labels, title, and grid
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.title('Bi-Monthly Unemployment Rate in 2024-2025', pad=20)
plt.grid(True)

# Show the plot
plt.show()