
import matplotlib.pyplot as plt

# Data to plot
labels = 'Drama', 'Comedy', 'Documentary', 'Action', 'Horror'
sizes = [300, 200, 150, 250, 100]
colors = ['#ff6666', '#66ff66', '#6666ff', '#ffcc66', '#66cccc']

# Plot
plt.figure(figsize=(10, 7))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Film Genre Distribution in 2023', y=1.05)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()