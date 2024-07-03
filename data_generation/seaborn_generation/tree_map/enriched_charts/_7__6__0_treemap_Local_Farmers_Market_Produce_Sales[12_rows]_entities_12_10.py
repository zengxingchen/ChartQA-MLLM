
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    'Field': [
        'Marine Biology', 'Astrophysics', 'Climate Science', 
        'Geology', 'Ecology', 'Oceanography', 'Botany', 'Zoology', 
        'Meteorology', 'Paleontology', 'Environmental Science', 
        'Evolutionary Biology', 'Genetics', 'Microbiology', 'Physics', 
        'Chemistry', 'Astronomy', 'Entomology', 'Ornithology', 'Herpetology'
    ],
    'Funding (Millions)': [
        4500, 4300, 4000, 3700, 3600, 3300, 3100, 2900, 
        2700, 2500, 2400, 2200, 2100, 1900, 1800, 1700, 
        1600, 1500, 1400, 1300
    ]
}

df = pd.DataFrame(data)

colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF', 
    '#33FFA1', '#FF8C33', '#8C33FF', '#33FFF3', '#FF3333', 
    '#57FF33', '#5733FF', '#A1FF33', '#33A1FF', '#FFA133', 
    '#FF338C', '#FF3357', '#33FF8C', '#FF5733', '#FF33A1'
]

plt.figure(figsize=(20, 12))

squarify.plot(sizes=df['Funding (Millions)'], label=df['Field'], color=colors, alpha=0.8)

plt.title('Funding Allocation in Science & Nature Research Fields (in Millions)', fontsize=22, pad=20)
plt.axis('off')
plt.show()