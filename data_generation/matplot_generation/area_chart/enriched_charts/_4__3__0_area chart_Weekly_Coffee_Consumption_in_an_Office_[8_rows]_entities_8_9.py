
import matplotlib.pyplot as plt

# Generate data points
days = list(range(1, 31))
active_users = [
    50, 55, 60, 70, 80, 90, 100, 110, 130, 140,
    150, 160, 180, 190, 200, 210, 220, 240, 250, 260,
    280, 290, 300, 310, 330, 340, 350, 360, 370, 380
]

# Create an area chart
plt.figure(figsize=(16, 8))  # Changed width and height
plt.fill_between(days, active_users, color="#4682B4")  # Modified color scheme

# Customize axes and labels
plt.title("Monthly Active Users on a Social Media Platform", pad=20)
plt.xlabel("Day of the Month")
plt.ylabel("Active Users")
plt.xticks(range(1, 31, 2))  # Show every second day for clarity
plt.yticks(range(50, 401, 25))  # Adjust the y-ticks to cover the data range

# Annotate a specific data point
plt.annotate('Highest Activity', xy=(30, 380), xytext=(20, 400),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Display the plot
plt.show()