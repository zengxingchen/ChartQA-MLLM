
import matplotlib.pyplot as plt

# Data
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
diameters = [4879, 12104, 12742, 6779, 139820, 116460, 50724, 49244]
colors = ['#ffa07a', '#fa8072', '#ff6347', '#ff4500', '#db7093', '#ffc0cb', '#ff69b4', '#ff1493']

# Plotting the pie chart
fig, ax = plt.subplots(figsize=(10, 8))
ax.pie(diameters, labels=planets, autopct='%1.1f%%', startangle=140, colors=colors)
ax.axis('equal')

# Setting the title
plt.title("Planetary Diameters in the Solar System", pad=20)

# Display the chart
plt.show()