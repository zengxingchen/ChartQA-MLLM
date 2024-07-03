
import matplotlib.pyplot as plt

# Data to plot
labels = ['Awareness Campaigns', 'Counseling Services', 'Community Workshops', 'Online Resources', 'Employee Assistance Programs', 'School Programs', 'Research and Development']
sizes = [35.0, 25.0, 15.0, 12.0, 8.0, 5.0, 0.0]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

# Plot
fig1, ax1 = plt.subplots(figsize=(8, 6))
ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Mental Health Awareness Programs in 2023', pad=20)
plt.show()