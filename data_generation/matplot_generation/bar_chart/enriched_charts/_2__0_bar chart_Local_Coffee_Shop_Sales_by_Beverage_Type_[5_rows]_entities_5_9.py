
import matplotlib.pyplot as plt

# Data
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
diameters = [4879, 12104, 12742, 6779, 139820, 116460, 50724, 49244]

# Create figure and axis objects
fig, ax = plt.subplots(figsize=(10, 15))  # Changed figure size

# Plotting the vertical bar chart
ax.bar(planets, diameters, color=['#FF6347', '#4682B4', '#FFD700', '#32CD32', '#8A2BE2', '#FF4500', '#00CED1', '#FF69B4'], width=0.5)  # Changed colors and bar width

# Customizing the plot (labels, title, etc.)
ax.set_ylabel('Diameter in km')
ax.set_title('Diameters of Planets in the Solar System', pad=20)
ax.set_ylim([0, 150000])  # Adjusted to accommodate the maximum data point

# Display the plot
plt.tight_layout()
plt.show()