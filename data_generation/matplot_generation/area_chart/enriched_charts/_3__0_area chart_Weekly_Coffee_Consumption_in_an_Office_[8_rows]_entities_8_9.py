
import matplotlib.pyplot as plt

# Generate data points
days = list(range(1, 31))
page_views = [
    100, 120, 140, 160, 180, 200, 220, 240, 260, 280,
    300, 320, 340, 360, 380, 400, 420, 440, 460, 480,
    500, 520, 540, 560, 580, 600, 620, 640, 660, 680
]

# Create an area chart
plt.figure(figsize=(14, 7))  # Changed width and height
plt.fill_between(days, page_views, color="#FF5733")  # Modified color scheme

# Customize axes and labels
plt.title("Daily Page Views for a Popular Blog", pad=20)
plt.xlabel("Day of the Month")
plt.ylabel("Page Views")
plt.xticks(range(1, 31, 2))  # Show every second day for clarity
plt.yticks(range(100, 701, 50))  # Adjust the y-ticks to cover the data range

# Annotate a specific data point
plt.annotate('Peak Traffic', xy=(30, 680), xytext=(20, 700),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Display the plot
plt.show()