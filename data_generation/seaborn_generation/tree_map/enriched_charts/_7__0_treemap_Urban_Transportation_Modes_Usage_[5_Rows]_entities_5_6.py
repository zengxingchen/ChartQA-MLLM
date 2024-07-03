
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Create the dataframe
df = pd.DataFrame({
    'Field': ['The Louvre', 'The British Museum', 'The Metropolitan Museum of Art', 'The Vatican Museums', 
              'The Smithsonian Institution', 'The State Hermitage Museum', 'The National Gallery', 'The Tate Modern',
              'The Natural History Museum', 'The American Museum of Natural History', 'The Centre Pompidou', 
              'The National Museum of China', 'The Museum of Modern Art', 'The Rijksmuseum', 'The Uffizi Gallery'],
    'Visitors': [10400000, 5900000, 6700000, 6060000, 7060000, 4770000, 6170000, 5610000, 5240000, 5030000, 3300000, 8000000, 3100000, 2900000, 2200000]
})

# Custom colors for the treemap
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A5', '#33FFA5', '#FFA533', '#A533FF', '#33A5FF', '#FF5733', '#57FF33', '#A5FF33', '#FF3357', '#33FFA5', '#5733FF', '#FFA533']

# Create a figure and a set of subplots
plt.figure(figsize=(18, 10))

# Using squarify to plot the treemap
squarify.plot(sizes=df['Visitors'], label=df['Field'], color=colors, alpha=0.8)

plt.title("Annual Visitors to Top Museums Around the World", fontsize=24, fontweight='bold', y=1.05)
plt.axis('off')  # Disable the axis

plt.show()