
import matplotlib.pyplot as plt

# Data to plot
labels = 'Beaches', 'Mountains', 'Cities', 'Countryside', 'Historical Sites', 'Adventure Sports', 'Wildlife'
sizes = [20, 25, 15, 18, 12, 10, 15]
colors = ['#FFA07A','#20B2AA','#778899','#DDA0DD','#4682B4','#FF4500','#32CD32']

# Change the size of the figure (width, height)
plt.figure(figsize=(10, 7))

# Plot
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Travel & Adventure Preferences', pad=20)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()