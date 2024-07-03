
import matplotlib.pyplot as plt

categories = ['Quantum Computing', 'Artificial Intelligence', 'Blockchain', 'Virtual Reality', 
              'Augmented Reality', '5G Networks', 'Internet of Things', 'Robotics', 'Cybersecurity', 
              'Autonomous Vehicles', 'Nanotechnology', 'Biotechnology', 'Wearable Technology', 
              'Cloud Computing', '3D Printing', 'Edge Computing', 'Smart Home Technology', 'Drones', 
              'Renewable Energy', 'Genomics', 'Brain-Computer Interface', 'Advanced Materials', 
              'Space Tourism', 'Smart Cities', 'Holography', 'Digital Twins']

impact = [90, 88, 85, 82, 79, 77, 74, 72, 70, 68, 65, 63, 60, 58, 55, 53, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32]
support = [85, 83, 80, 78, 75, 73, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32]
respondents = [600, 580, 560, 540, 520, 500, 480, 460, 440, 420, 400, 380, 360, 340, 320, 300, 280, 260, 240, 220, 200, 180, 160, 140, 120, 100]

size = [respondent / 2 for respondent in respondents]

fig, ax = plt.subplots(figsize=(16, 12))

colors = ['#FF6347', '#FFD700', '#ADFF2F', '#20B2AA', '#FF69B4', '#8A2BE2', '#5F9EA0', '#D2691E', '#FF7F50', '#6495ED', 
          '#DC143C', '#00FFFF', '#00008B', '#008B8B', '#B8860B', '#A9A9A9', '#006400', '#BDB76B', '#8B008B', '#556B2F',
          '#FF8C00', '#9932CC', '#8B0000', '#E9967A', '#8FBC8F', '#483D8B']

for i in range(len(categories)):
    ax.scatter(impact[i], support[i], s=size[i], alpha=0.6, color=colors[i])

for i, txt in enumerate(categories):
    ax.annotate(txt, (impact[i], support[i]), ha='center', va='center', fontsize=8)

ax.set_title('Popularity and Interest in Future Technologies', fontsize=20, pad=20)
ax.set_xlabel('Impact on Society', fontsize=16)
ax.set_ylabel('Public Interest', fontsize=16)

ax.set_xlim(30, 95)
ax.set_ylim(30, 90)

plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

plt.show()