
import matplotlib.pyplot as plt

# Data to plot
labels = ['Movie Production', 'Streaming Services', 'Music Industry', 'Video Games', 'Live Concerts', 'Theater and Drama', 'Publishing Industry']
sizes = [30.0, 25.0, 20.0, 10.0, 8.0, 5.0, 2.0]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f']

# Plot
fig1, ax1 = plt.subplots(figsize=(10, 8))
ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Entertainment Industry Distribution in 2023', pad=20)
plt.show()