
import matplotlib.pyplot as plt

# Data for plotting
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
active_users = [110, 130, 125, 160, 150, 200, 180, 220, 210, 240, 230, 260, 250, 270, 290, 300, 310, 330, 320, 350, 340, 360, 370, 380, 390, 400, 410, 420, 430, 440]
new_articles = [5, 10, 12, 8, 15, 18, 22, 25, 28, 30, 35, 38, 40, 45, 48, 50, 52, 55, 58, 60, 62, 65, 68, 70, 72, 75, 78, 80, 82, 85]

# Create a scatterplot
plt.figure(figsize=(12, 8))
plt.scatter(days, active_users, c="#2E8B57", label="Active Users")
plt.scatter(days, new_articles, c="#D2691E", label="New Articles")

# Customize the chart
plt.title("Active Users and New Articles Over a Month", pad=20)
plt.xlabel("Day of the Month")
plt.ylabel("Count")
plt.legend(loc='upper right')
plt.grid(True)

# Show the scatterplot
plt.show()