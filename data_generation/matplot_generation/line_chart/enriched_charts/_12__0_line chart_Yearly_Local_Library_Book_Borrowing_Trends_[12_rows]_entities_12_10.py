
import matplotlib.pyplot as plt

# Data points
dates = ["2024-01-01", "2024-02-01", "2024-03-01", "2024-04-01", "2024-05-01",
         "2024-06-01", "2024-07-01", "2024-08-01", "2024-09-01", "2024-10-01",
         "2024-11-01", "2024-12-01"]
views = [500, 600, 650, 700, 750, 900, 1100, 1150, 950, 800, 700, 600]

# Creating the line chart
plt.figure(figsize=(12, 6))

plt.plot(dates, views, color="#4682B4", marker='o')

# Annotating the highest and lowest views
plt.annotate('Highest\n1150 Views', xy=("2024-08-01", 1150), xytext=("2024-08-01", 1200),
             arrowprops=dict(facecolor='#FF4500', shrink=0.05), ha='center')
plt.annotate('Lowest\n500 Views', xy=("2024-01-01", 500), xytext=("2024-01-01", 450),
             arrowprops=dict(facecolor='#32CD32', shrink=0.05), ha='center')

# Title and labels
plt.title("Monthly Website Views in 2024", fontsize=16, pad=20)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Number of Views", fontsize=14)

# Customizing the grid
plt.grid(True, which='major', linestyle='--', linewidth=0.5, color='grey')

# Show the plot
plt.show()