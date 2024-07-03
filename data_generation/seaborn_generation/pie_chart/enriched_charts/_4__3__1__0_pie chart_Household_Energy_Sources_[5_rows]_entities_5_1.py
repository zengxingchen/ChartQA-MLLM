
import matplotlib.pyplot as plt

# Table data
category = ["Astronomy & Space Exploration", "Politics & Governance", "Economics & Finance", "Environment & Climate Change", "Science & Nature", "Art & Design"]
percentage = [23.0, 18.0, 16.5, 14.0, 13.5, 15.0]
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF', '#33FFA1']

# Plot
fig, ax = plt.subplots(figsize=(12, 8))  # Change width and height of the chart
ax.pie(percentage, labels=category, autopct='%1.1f%%', startangle=140, colors=colors)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('Distribution of Interest in Various Fields (2024)', pad=20)
plt.show()