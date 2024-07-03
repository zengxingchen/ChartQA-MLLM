
import matplotlib.pyplot as plt
import squarify

# Data
topic = ['AI and Robotics', 'Quantum Computing', '3D Printing', 'AR & VR', 'Blockchain', 'Biotechnology', 'Internet of Things', 'Cybersecurity', 'Edge Computing', 'Nanotechnology', 'Genetic Editing', 'Smart Cities']
percentage = [20.5, 15.2, 12.8, 10.4, 8.9, 8.2, 7.6, 6.8, 5.5, 4.1, 3.0, 2.5]
color_code = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#A833FF', '#FFA833', '#33FFA8', '#FF5733', '#5733FF', '#A8FF33', '#33A8FF', '#FF8333']

# Plot
plt.figure(figsize=(18, 12))
squarify.plot(sizes=percentage, label=topic, color=color_code, alpha=0.8)
plt.title('Future Technologies & Society: Emerging Trends in 2022', fontsize=24, y=1.05)
plt.axis('off')
plt.show()