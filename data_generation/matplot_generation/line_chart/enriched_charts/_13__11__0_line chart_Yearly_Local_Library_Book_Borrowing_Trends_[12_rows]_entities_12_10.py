
import matplotlib.pyplot as plt

# Data points
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
ev_sales = [20000, 22000, 25000, 30000, 35000, 40000, 38000, 36000, 33000, 28000, 24000, 21000]

# Creating the line chart
plt.figure(figsize=(14, 7))

plt.plot(months, ev_sales, color="#8A2BE2", marker='o')  # Using a specific color code

# Annotating the highest and lowest EV sales
plt.annotate('Highest\n40000', xy=("June", 40000), xytext=("June", 42000),
             arrowprops=dict(facecolor='#FF6347', shrink=0.05), ha='center')
plt.annotate('Lowest\n20000', xy=("January", 20000), xytext=("January", 18000),
             arrowprops=dict(facecolor='#3CB371', shrink=0.05), ha='center')

# Title and labels
plt.title("Monthly EV Sales", fontsize=16, pad=20)
plt.xlabel("Month", fontsize=14)
plt.ylabel("Number of EV Sales", fontsize=14)

# Customizing the grid
plt.grid(True, which='major', linestyle='--', linewidth=0.6, color='grey')

# Show the plot
plt.show()