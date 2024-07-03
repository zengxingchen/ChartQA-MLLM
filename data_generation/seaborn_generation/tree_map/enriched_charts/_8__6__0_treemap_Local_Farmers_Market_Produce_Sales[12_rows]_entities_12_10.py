
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import squarify

data = {
    'Field': [
        'Astrophysics', 'Planetary Science', 'Exoplanet Research', 
        'Cosmology', 'Spacecraft Engineering', 'Space Medicine', 
        'Astronomy Education', 'Astronomical Instrumentation', 'Space Weather', 
        'Radio Astronomy', 'Observational Astronomy', 'Theoretical Astronomy', 
        'Gravitational Wave Research', 'Dark Matter Studies', 'Astrobiology', 
        'Solar Physics', 'Stellar Astrophysics', 'Galactic Astronomy', 
        'Interstellar Medium', 'Space Policy'
    ],
    'Funding (Millions)': [
        6200, 5800, 5400, 5200, 5000, 4800, 4600, 4400, 
        4200, 4000, 3800, 3600, 3400, 3200, 3000, 2800, 
        2600, 2400, 2200, 2000
    ]
}

df = pd.DataFrame(data)

colors = [
    '#FF5733', '#FFC300', '#FF0000', '#C70039', '#900C3F', 
    '#DAF7A6', '#FFC0CB', '#9B59B6', '#3498DB', '#85C1E9', 
    '#16A085', '#138D75', '#7D3C98', '#F39C12', '#2E4053', 
    '#34495E', '#1ABC9C', '#E74C3C', '#8E44AD', '#2980B9'
]

plt.figure(figsize=(20, 12))

squarify.plot(sizes=df['Funding (Millions)'], label=df['Field'], color=colors, alpha=0.8)

plt.title('Funding Allocation in Astronomy & Space Exploration (in Millions)', fontsize=24, pad=20)
plt.axis('off')
plt.show()