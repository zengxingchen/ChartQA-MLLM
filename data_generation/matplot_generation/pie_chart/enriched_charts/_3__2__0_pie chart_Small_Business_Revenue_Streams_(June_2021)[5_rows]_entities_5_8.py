
import matplotlib.pyplot as plt

# Data to plot
labels = ['Satellite Development', 'Crewed Missions', 'Space Research', 'Launch Vehicles', 'Space Stations', 'Rovers & Landers', 'Deep Space Probes', 'Earth Observation', 'Space Tourism', 'Astrobiology']
sizes = [20, 15, 10, 18, 12, 8, 7, 5, 3, 2]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c2f0c2', '#ffcc66', '#b3e6ff', '#e6b3ff']

# Plot
fig1, ax1 = plt.subplots(figsize=(10, 6))
ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

# Draw circle for donut chart
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')

plt.title('Space Mission Budget Allocation', pad=20)
plt.show()