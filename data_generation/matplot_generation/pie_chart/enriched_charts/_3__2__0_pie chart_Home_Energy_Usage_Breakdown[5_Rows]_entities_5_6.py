
import matplotlib.pyplot as plt

# Data
fields = ['Mountaineering', 'Scuba Diving', 'Safari Adventures', 'Skiing', 'Bungee Jumping',
          'Paragliding', 'Cave Exploring', 'Rock Climbing', 'White Water Rafting', 'Skydiving',
          'Zip Lining', 'Hot Air Ballooning', 'Glacier Hiking', 'Surfing', 'Sandboarding']
values = [300, 250, 200, 180, 160, 140, 120, 100, 90, 80, 70, 60, 50, 40, 30]

# Colors
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0',
          '#ffb3e6','#c4e17f','#76d7c4','#ff9966','#ff6666',
          '#ffcc99','#ffb3e6','#c4e17f','#76d7c4','#ff9966']

# Pie chart
fig, ax = plt.subplots(figsize=(16, 12))  # Width, Height of the chart
ax.pie(values, labels=fields, colors=colors, autopct='%1.1f%%', startangle=140)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('Popularity of Adventure Activities', pad=20)
plt.show()