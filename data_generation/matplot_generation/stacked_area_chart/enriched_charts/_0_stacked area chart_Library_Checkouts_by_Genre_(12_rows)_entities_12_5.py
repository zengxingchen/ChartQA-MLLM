
import matplotlib.pyplot as plt

# Data
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
sedans = [120, 135, 150, 165, 180, 200, 220, 240, 260, 280, 300, 320]
suvs = [150, 160, 170, 180, 190, 210, 230, 250, 270, 290, 310, 330]
trucks = [130, 145, 160, 175, 190, 205, 220, 235, 250, 265, 280, 295]

# Stacked Area Chart
fig, ax = plt.subplots(figsize=(10, 6))
ax.stackplot(months, sedans, suvs, trucks, colors=['#1f77b4', '#ff7f0e', '#2ca02c'])

# Customizing the plot
ax.set_title('Monthly EV Sales by Type in 2023')
ax.set_ylabel('Number of Vehicles Sold')
ax.set_xlabel('Month')
ax.margins(0, 0)  # Removes the default margins to use the entire space for plotting

# Adding annotation
ax.annotate('Trucks peak', xy=('June', 405), xytext=('July', 450),
            arrowprops=dict(facecolor='black', shrink=0.05))

# Displaying the plot
plt.show()