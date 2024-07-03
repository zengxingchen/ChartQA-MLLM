
import matplotlib.pyplot as plt

# Data to plot
labels = ['Ancient History', 'Medieval History', 'Renaissance', 'Industrial Revolution', 'Modern History', 'World Wars', 'Cold War', 'Information Age', 'Globalization', 'Contemporary Era']
sizes = [18, 22, 15, 12, 14, 10, 9, 8, 7, 5]
colors = ['#4B0082', '#8A2BE2', '#5F9EA0', '#7FFF00', '#D2691E', '#FF7F50', '#6495ED', '#DC143C', '#00FFFF', '#FF1493']

# Plot
fig1, ax1 = plt.subplots(figsize=(14, 10))
ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Draw circle for donut chart
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')

plt.title('Historical Periods by Significance', pad=20)
plt.show()