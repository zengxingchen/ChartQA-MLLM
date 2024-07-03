
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    'Category': [
        'Digital Media', 'E-commerce', 'Software Development', 'Cloud Computing', 
        'Artificial Intelligence', 'Cybersecurity', 'Mobile Apps', 'Big Data', 
        'Blockchain', 'Internet of Things', 'FinTech', 'Augmented Reality', 
        'Virtual Reality', 'Gaming', 'EdTech', 'HealthTech', 'Biotechnology', 
        'Green Technology', 'Robotics', 'Quantum Computing', 'Space Exploration'
    ],
    'Revenue (Millions)': [
        7200, 6800, 6600, 6400, 6200, 6000, 5800, 5600, 
        5400, 5200, 5000, 4800, 4600, 4400, 4200, 4000, 
        3800, 3600, 3400, 3200, 3000
    ]
}

df = pd.DataFrame(data)

colors = [
    '#4B0082', '#6A5ACD', '#7B68EE', '#8470FF', '#9370DB', 
    '#8A2BE2', '#9400D3', '#9932CC', '#BA55D3', '#FF00FF', 
    '#EE82EE', '#DDA0DD', '#DA70D6', '#FF1493', '#C71585', 
    '#DB7093', '#FF69B4', '#FFB6C1', '#FFC0CB', '#FF6347', 
    '#FF4500'
]

plt.figure(figsize=(22, 14))

squarify.plot(sizes=df['Revenue (Millions)'], label=df['Category'], color=colors, alpha=0.85)

plt.title('Revenue Distribution in Future Technologies & Society Sectors (in Millions)', fontsize=24, pad=30)
plt.axis('off')
plt.show()