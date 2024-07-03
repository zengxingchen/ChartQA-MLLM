
import matplotlib.pyplot as plt

labels = 'Solar Power', 'Wind Energy', 'Hydropower', 'Geothermal', 'Biomass'
sizes = [320, 240, 180, 140, 110]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

plt.figure(figsize=(10,8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Renewable Energy Sources Distribution', pad=20)
plt.axis('equal')  
plt.show()