
import matplotlib.pyplot as plt

# Data to plot
labels = 'Hotels', 'Hostels', 'Airbnbs', 'Camping', 'Resorts'
sizes = [300, 150, 200, 100, 250]
colors = ['#ff5733','#33ffbd','#335cff','#ff33a6','#ffdd33']

# Plot
plt.figure(figsize=(10,8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Accommodation Preferences of Travelers', pad=20)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()