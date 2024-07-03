
import matplotlib.pyplot as plt

# Data to plot
labels = 'Android', 'iOS', 'KaiOS', 'Windows', 'Others'
sizes = [72.6, 26.2, 0.8, 0.2, 0.2]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

# Create pie chart
plt.figure(figsize=(10, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Market Share of Smartphone Operating Systems in 2023')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()