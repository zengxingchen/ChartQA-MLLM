
import matplotlib.pyplot as plt

# Data for plotting
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
active_users = [100, 120, 130, 150, 170, 190, 210, 230, 250, 270, 290, 310, 330, 350, 370, 390, 410, 430, 450, 470, 490, 510, 530, 550, 570, 590, 610, 630, 650, 670]
new_signups = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155]

# Create a scatterplot
plt.figure(figsize=(14, 10))
plt.scatter(days, active_users, c="#1F77B4", label="Active Users")
plt.scatter(days, new_signups, c="#FF7F0E", label="New Signups")

# Customize the chart
plt.title("User Engagement Over a Month")
plt.xlabel("Day of the Month")
plt.ylabel("Count")
plt.legend(loc='upper left')
plt.grid(True)

# Show the scatterplot
plt.show()