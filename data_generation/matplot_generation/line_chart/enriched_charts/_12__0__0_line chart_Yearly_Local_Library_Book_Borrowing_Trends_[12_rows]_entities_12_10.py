
import matplotlib.pyplot as plt

# Data points
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
downloads = [100, 120, 110, 140, 130, 150, 170, 160, 155, 145, 135, 125]

# Creating the line chart
plt.figure(figsize=(14, 7))

plt.plot(months, downloads, color="#8B0000", marker='o')

# Annotating the highest and lowest downloads
plt.annotate('Highest\n170 downloads', xy=("July", 170), xytext=("July", 180),
             arrowprops=dict(facecolor='#FF4500', shrink=0.05), ha='center')
plt.annotate('Lowest\n100 downloads', xy=("January", 100), xytext=("January", 90),
             arrowprops=dict(facecolor='#1E90FF', shrink=0.05), ha='center')

# Title and labels
plt.title("Monthly Downloads for a Mobile App", fontsize=18, pad=25)
plt.xlabel("Month", fontsize=14)
plt.ylabel("Number of Downloads", fontsize=14)

# Customizing the grid
plt.grid(True, which='major', linestyle='--', linewidth=0.7, color='#A9A9A9')

# Show the plot
plt.show()