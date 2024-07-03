
import matplotlib.pyplot as plt

# Data
operating_systems = ['Android', 'iOS', 'HarmonyOS', 'Other']
market_share = [70, 27, 2, 1]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# Plotting the pie chart
fig, ax = plt.subplots(figsize=(8, 6))  # Change width and height
ax.pie(market_share, labels=operating_systems, autopct='%1.1f%%', startangle=140, colors=colors)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Setting the title
plt.title("Smartphone Operating System Market Share in 2022")

# Display the chart
plt.show()