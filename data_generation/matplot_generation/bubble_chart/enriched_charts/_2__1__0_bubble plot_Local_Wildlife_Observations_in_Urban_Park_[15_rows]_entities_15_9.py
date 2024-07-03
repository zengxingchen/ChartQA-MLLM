
import matplotlib.pyplot as plt

topics = ['Quantum Computing', 'AI Ethics', 'Bioengineering', 'Renewable Energy', 'Nanotechnology', 
          'Robotics', 'Space Exploration', '3D Printing', 'Genomics', 'Cybersecurity', 
          'Autonomous Vehicles', 'VR/AR', 'Blockchain', 'Neuroscience', 'Wearable Tech']
year = [2024] * len(topics)
values = [18000, 17500, 17000, 16000, 15500, 15000, 14500, 14000, 13500, 13000, 12500, 12000, 11500, 11000, 10500]
count = [90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20]

size = [x * 2 for x in count]
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FF8C33', '#57FF33', '#5733FF', '#A133FF', '#FF33F4', 
          '#33FFF8', '#F4FF33', '#FF3388', '#88FF33', '#33FFBB', '#FF5733']

fig, ax = plt.subplots(figsize=(16, 10))

sc = ax.scatter(topics, year, s=size, c=colors, alpha=0.6, edgecolors='w')

ax.set_title('Future Technologies & Society - Popularity and Research Intensity (2024)')
ax.set_xlabel('Technology Topics')
ax.set_ylabel('Year')
ax.set_yticks([2024])
ax.grid(True)

value_tick_vals = range(10500, 18500, 1000)
value_tick_labels = ['$' + str(val) for val in value_tick_vals]
sm = plt.cm.ScalarMappable(cmap=plt.cm.jet, norm=plt.Normalize(vmin=min(values), vmax=max(values)))
sm._A = []
cbar = plt.colorbar(sm, ticks=value_tick_vals)
cbar.ax.set_yticklabels(value_tick_labels)
cbar.set_label('Research Funding ($)')

plt.show()