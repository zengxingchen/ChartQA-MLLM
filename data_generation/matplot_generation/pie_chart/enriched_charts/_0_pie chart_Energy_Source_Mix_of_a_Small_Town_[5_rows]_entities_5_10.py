
import matplotlib.pyplot as plt

# Data to plot
labels = 'Sedan', 'SUV', 'Truck', 'Motorcycle', 'Bus'
sizes = [450, 350, 120, 200, 80]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

# Plot
plt.figure(figsize=(8,6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Vehicle Distribution in Central District')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()