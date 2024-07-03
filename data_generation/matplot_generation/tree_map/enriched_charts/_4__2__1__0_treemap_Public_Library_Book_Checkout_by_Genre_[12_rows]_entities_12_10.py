
import matplotlib.pyplot as plt
import squarify

data = {
    'Category': [
        'Artificial Intelligence', 'Quantum Computing', 'Nanotechnology', 
        'Blockchain', 'Biotechnology', 'Robotic Automation', 
        'Virtual Reality', 'Augmented Reality', 'Internet of Things', 
        '3D Printing', 'Cybersecurity', 'Big Data', 
        'Renewable Energy', 'Gene Editing', 'Space Travel', 
        'Smart Cities', 'Autonomous Vehicles', 'Digital Health', 
        'Wearable Technology', 'Immersive Media'
    ],
    'Value': [
        58, 27, 18, 12, 36, 25, 
        22, 15, 31, 20, 17, 30, 
        28, 14, 13, 11, 19, 22, 
        16, 23
    ]
}

fig, ax = plt.subplots(figsize=(12, 8))
colors = [
    "#FF9999", "#66B2FF", "#99FF99", "#FFCC99",
    "#FFD700", "#FF6347", "#4682B4", "#8A2BE2",
    "#A52A2A", "#DEB887", "#5F9EA0", "#7FFF00",
    "#D2691E", "#FF7F50", "#6495ED", "#FFF8DC",
    "#DC143C", "#00008B", "#008B8B", "#B8860B"
]

squarify.plot(sizes=data['Value'], label=data['Category'], color=colors, alpha=.8)
plt.title('Future Technologies & Society', fontsize=16, fontweight='bold', pad=20)
plt.axis('off')
plt.show()