
import matplotlib.pyplot as plt

labels = ['Europe', 'Asia', 'North America', 'South America', 'Africa', 'Australia', 'Antarctica', 'Oceania']
sizes = [200, 180, 160, 140, 120, 100, 60, 40]
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FFD700', '#FF69B4', '#FF6347', '#40E0D0']

plt.figure(figsize=(10, 10))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Popular Travel Destinations in 2023', pad=20)
plt.axis('equal')
plt.show()