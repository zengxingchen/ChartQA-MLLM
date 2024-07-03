
import matplotlib.pyplot as plt

# Data to plot
labels = 'Reading', 'Watching TV', 'Exercising', 'Socializing', 'Gaming', 'Others'
sizes = [25, 20, 15, 18, 12, 10]
colors = ['#ff6666', '#ffcc66', '#66b3ff', '#99ff99', '#ffb3e6', '#c2c2f0']

# Plot
plt.figure(figsize=(10,7))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

plt.title('Leisure Activities Distribution', pad=20)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()