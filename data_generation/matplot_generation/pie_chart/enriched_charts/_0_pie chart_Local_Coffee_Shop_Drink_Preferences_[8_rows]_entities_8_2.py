
import matplotlib.pyplot as plt

# Data to plot
labels = 'Buses', 'Taxis', 'Trams', 'Subway Trains', 'Bikes', 'Car Shares', 'Scooters', 'Ferries'
sizes = [340, 165, 100, 75, 45, 25, 10, 5]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6', '#c4e17f', '#76d7c4']

# Change the size of the figure (width, height)
plt.figure(figsize=(10, 6))

# Plot
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Distribution of Vehicles in Public Transportation Fleet')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()