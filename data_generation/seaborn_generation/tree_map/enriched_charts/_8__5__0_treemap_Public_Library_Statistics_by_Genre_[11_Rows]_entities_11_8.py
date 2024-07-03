
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Create a data frame with diversified data
df = pd.DataFrame({
    'category': ['Planets', 'Planets', 'Planets', 'Planets', 'Stars', 'Stars', 'Stars', 'Stars', 
                 'Galaxies', 'Galaxies', 'Galaxies', 'Galaxies', 'Missions', 'Missions', 'Missions', 'Missions', 
                 'Theories', 'Theories', 'Theories', 'Theories', 'Telescopes', 'Telescopes', 'Telescopes', 'Telescopes'],
    'sub_category': ['Earth', 'Mars', 'Jupiter', 'Saturn', 'Sun', 'Alpha Centauri', 'Sirius', 'Betelgeuse', 
                     'Milky Way', 'Andromeda', 'Whirlpool', 'Sombrero', 'Apollo 11', 'Voyager 1', 
                     'Curiosity Rover', 'Hubble Telescope', 'Big Bang', 'String Theory', 'Relativity', 
                     'Multiverse', 'James Webb', 'Kepler', 'Spitzer', 'Chandra'],
    'value': [1200, 950, 800, 750, 1500, 1100, 900, 850, 1600, 1400, 1200, 1000, 1300, 1150, 1050, 900, 
              1450, 1300, 1200, 1100, 1000, 950, 900, 850]
})

# Create a new color list
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1', '#955251', '#B565A7', '#009B77', 
          '#DD4124', '#D65076', '#45B8AC', '#EFC050', '#5B5EA6', '#9B2335', '#DFCFBE', '#55B4B0', 
          '#E15D44', '#7FCDCD', '#BC243C', '#C3447A', '#98B4D4', '#C39BD3', '#F4A460', '#CD5C5C']

# Plot
plt.figure(figsize=(30, 15))
squarify.plot(sizes=df['value'], label=df['sub_category'], color=colors, alpha=.8)
plt.title('Astronomy & Space Exploration Key Areas', fontsize=30, pad=20)
plt.axis('off')
plt.show()