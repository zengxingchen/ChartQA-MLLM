
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    'Item': ['Planets', 'Stars', 'Galaxies', 'Nebulae', 'Comets', 'Asteroids', 'Moons', 
             'Black Holes', 'Quasars', 'Supernovae', 'Pulsars', 'Clusters', 'Exoplanets', 
             'Dwarf Planets', 'Star Systems', 'Dark Matter', 'Dark Energy'],
    'Quantity': [8, 1000000, 2000000000, 3000, 5000, 1000000, 175, 10000, 2000, 500, 1500, 
                 50000, 4000, 5, 250000000, 10000000000, 20000000000]
}

df = pd.DataFrame(data)

colors = ['#FF4500', '#32CD32', '#1E90FF', '#FFD700', '#6A5ACD', '#00FF7F', '#FF6347', 
          '#4682B4', '#9ACD32', '#FFA07A', '#40E0D0', '#FF69B4', '#CD5C5C', '#4B0082', 
          '#BDB76B', '#8FBC8F', '#DA70D6']

fig = plt.figure(figsize=(18, 14))
ax = fig.add_subplot(111, aspect="auto")

squarify.plot(sizes=df['Quantity'], label=df['Item'], color=colors, alpha=0.8)

plt.title('Astronomical Entities Quantities', fontsize=22, pad=20)

plt.axis('off')

plt.show()