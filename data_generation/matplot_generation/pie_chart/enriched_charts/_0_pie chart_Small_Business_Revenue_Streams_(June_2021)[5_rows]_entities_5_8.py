
import matplotlib.pyplot as plt

# Data to plot
labels = ['Books', 'Art Supplies', 'Movies', 'Video Games', 'Music', 'Electronics', 'Groceries', 'Clothing', 'Home & Kitchen', 'Sports Equipment']
sizes = [13, 7, 8, 15, 5, 12, 17, 8, 10, 5]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6', '#c4e17f', '#76d7c4', '#ffcccc', '#65a620']

# Plot
fig1, ax1 = plt.subplots(figsize=(10, 6))
ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Draw circle for donut chart
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')

plt.title('Expenditure Distribution by Category')
plt.show()