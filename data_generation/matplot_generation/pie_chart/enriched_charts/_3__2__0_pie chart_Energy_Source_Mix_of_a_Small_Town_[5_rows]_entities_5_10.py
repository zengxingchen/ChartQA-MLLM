
import matplotlib.pyplot as plt

# Data to plot
labels = 'History', 'Geography', 'Mathematics', 'Science', 'Literature'
sizes = [120, 180, 300, 240, 160]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Plot
plt.figure(figsize=(12, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Educational Topics Distribution in 2023', y=1.05)
plt.axis('equal')
plt.show()