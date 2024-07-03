
import matplotlib.pyplot as plt

# Data points
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
planets_discovered = [5, 8, 4, 11, 9, 7, 15, 12, 6, 10, 3, 13]

# Creating the line chart
plt.figure(figsize=(14, 8))

plt.plot(months, planets_discovered, color="#FF6347", marker='o')

# Annotating the highest and lowest planets discovered
plt.annotate('Highest\n15 planets', xy=("July", 15), xytext=("July", 17),
             arrowprops=dict(facecolor='#32CD32', shrink=0.05), ha='center')
plt.annotate('Lowest\n3 planets', xy=("November", 3), xytext=("November", 1),
             arrowprops=dict(facecolor='#1E90FF', shrink=0.05), ha='center')

# Title and labels
plt.title("Monthly Planets Discovered", fontsize=16, pad=20)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Number of Planets Discovered", fontsize=12)

# Customizing the grid
plt.grid(True, which='major', linestyle='--', linewidth=0.7, color='grey')

# Show the plot
plt.show()