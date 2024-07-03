
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Technology': ['AI', 'Blockchain', 'Quantum Computing', '5G', 'IoT', 'Robotics', 'VR/AR', '3D Printing', 'Biotech', 'Nanotechnology', 'Drones', 'Space Tourism', 'Electric Vehicles', 'Smart Homes', 'Wearable Tech'],
    'Adopters': [85, 60, 45, 80, 70, 55, 65, 50, 75, 40, 55, 35, 90, 75, 68]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 10))
sns.barplot(y='Adopters', x='Technology', data=df, palette=["#FF5733", "#33FF57", "#3357FF", "#F033FF", "#33FFF3", "#FFC733", "#FF3333", "#3FFF33", "#FF33FF", "#335FFF", "#33FFC7", "#FFF333", "#FF3399", "#C7FF33", "#5733FF"], linewidth=2.5)

plt.title('Adoption of Future Technologies', fontsize=18, pad=20)
plt.xlabel('Technology', fontsize=14)
plt.ylabel('Adopters', fontsize=14)
plt.grid(axis='y')

plt.show()