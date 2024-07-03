
import matplotlib.pyplot as plt

# Data
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
passenger_traffic = [20000, 22000, 25000, 30000, 35000, 40000, 45000, 47000, 43000, 41000, 39000, 38000]
cargo_traffic = [4000, 4200, 4500, 4700, 5000, 5500, 6000, 6200, 5800, 5600, 5400, 5200]
flights = [150, 160, 180, 200, 220, 250, 270, 280, 260, 240, 230, 220]

# Stacked Area Chart
fig, ax = plt.subplots(figsize=(14, 9))
ax.stackplot(months, passenger_traffic, cargo_traffic, flights, colors=['#1f77b4', '#ff7f0e', '#2ca02c'])

# Customizing the plot
ax.set_title('Monthly Airport Traffic in 2023', pad=20)
ax.set_ylabel('Count/Traffic')
ax.set_xlabel('Month')
ax.margins(0, 0)

# Adding annotation
ax.annotate('Peak Passenger Traffic', xy=('August', 47000), xytext=('June', 48000),
            arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('Increase in Cargo Traffic', xy=('July', 6000), xytext=('May', 6500),
            arrowprops=dict(facecolor='black', shrink=0.05))

# Adding legend
ax.legend(['Passenger Traffic', 'Cargo Traffic', 'Flights'], loc='upper left')

# Displaying the plot
plt.show()