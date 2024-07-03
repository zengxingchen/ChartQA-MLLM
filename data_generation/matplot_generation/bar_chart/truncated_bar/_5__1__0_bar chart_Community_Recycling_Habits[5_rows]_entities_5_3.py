
import matplotlib.pyplot as plt

# Data
fields = ['Artificial Intelligence', 'Quantum Computing', 'Blockchain Technology', 'Genetic Engineering', 'Renewable Energy', 'Augmented Reality', '5G Technology', 'Cybersecurity', 'Biotechnology', 'Nanotechnology']
impact = [88, 75, 60, 65, 90, 70, 85, 80, 78, 72]
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#A633FF', '#33FFF5', '#FF9933', '#99FF33', '#33FF99', '#5733FF']

# Figure size
plt.figure(figsize=(14, 8))

# Horizontal bar chart
plt.barh(fields, impact, color=colors, height=0.5)

# Labeling
plt.xlabel('Impact Score')
plt.title('Impact of Future Technologies on Society')
plt.ylim(50, 100)

# Show and save plot
plt.tight_layout()
plt.show()