import matplotlib.pyplot as plt

# Table data
category = ['Blockchain Technology', 'Artificial Intelligence', 'Renewable Energy', 'Virtual Reality', 'Quantum Computing', 'Biotechnology']
percentage = [22.4, 27.8, 18.5, 14.2, 10.1, 7.0]
colors = ['#FF6347', '#4682B4', '#9ACD32', '#FF69B4', '#BA55D3', '#FFD700']

# Plot
fig, ax = plt.subplots(figsize=(10, 6))  # Change width and height of the chart
ax.pie(percentage, labels=category, autopct='%1.1f%%', startangle=140, colors=colors)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('Distribution of Investment in Future Technologies (2024)', pad=20)
plt.show()