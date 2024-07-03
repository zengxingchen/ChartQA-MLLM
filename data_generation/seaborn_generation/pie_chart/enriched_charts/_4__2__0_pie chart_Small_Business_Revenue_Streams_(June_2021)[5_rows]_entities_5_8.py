
import matplotlib.pyplot as plt

# Data to plot
labels = ['Fruits', 'Vegetables', 'Dairy', 'Grains', 'Protein', 'Snacks', 'Beverages', 'Condiments', 'Frozen Foods', 'Baked Goods']
sizes = [10, 12, 8, 15, 20, 7, 18, 10, 8, 12]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6','#c2f0c2','#ffccff','#c2c2d6','#ffccb3']

# Plot
fig1, ax1 = plt.subplots(figsize=(10, 6))
ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Draw circle for donut chart
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')

plt.title('Food & Nutrition Distribution', pad=20)
plt.show()