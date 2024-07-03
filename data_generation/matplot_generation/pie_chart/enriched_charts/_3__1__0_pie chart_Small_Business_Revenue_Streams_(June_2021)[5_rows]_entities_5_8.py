
import matplotlib.pyplot as plt

# Data to plot
labels = ['Air Quality', 'Water Conservation', 'Renewable Energy', 'Waste Management', 'Biodiversity', 'Climate Education', 'Carbon Footprint', 'Sustainable Agriculture', 'Green Transportation', 'Eco-Friendly Products']
sizes = [15, 18, 20, 12, 10, 8, 7, 5, 3, 2]
colors = ['#4CAF50', '#FFEB3B', '#FF9800', '#03A9F4', '#E91E63', '#9C27B0', '#FFC107', '#8BC34A', '#00BCD4', '#673AB7']

# Plot
fig1, ax1 = plt.subplots(figsize=(14, 10))
ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Draw circle for donut chart
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')

plt.title('Environmental Focus Areas by Category', pad=20)
plt.show()