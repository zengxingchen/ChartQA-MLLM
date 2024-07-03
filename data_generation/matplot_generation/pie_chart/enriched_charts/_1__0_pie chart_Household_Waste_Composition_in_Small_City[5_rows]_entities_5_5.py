
import matplotlib.pyplot as plt

# Data to plot
labels = ['Future Technology', 'Renewable Energy', 'Healthcare Innovation', 'Artificial Intelligence', 'Blockchain', 'Quantum Computing', 'Other']
sizes = [40.5, 25.3, 15.2, 10.8, 5.4, 2.8, 0.0]
colors = ['#3498db', '#e74c3c', '#2ecc71', '#9b59b6', '#f1c40f', '#34495e', '#95a5a6']

# Plot
fig1, ax1 = plt.subplots(figsize=(10, 7))
ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Market Share of Emerging Technologies in 2023', pad=20)
plt.show()