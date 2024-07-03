
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Define the dataset
data = {
    'Category': ['Stars', 'Planets', 'Moons', 'Asteroids', 'Comets', 'Galaxies', 'Nebulae', 
                 'Dwarf Planets', 'Exoplanets', 'Black Holes', 'Pulsars', 'Quasars', 
                 'Meteors', 'Supernovae', 'Brown Dwarfs'],
    'Percentage': [35.12, 20.54, 15.67, 8.95, 7.88, 5.76, 3.56, 1.89, 1.23, 0.88, 0.69, 
                   0.61, 0.55, 0.44, 0.33]
}

df = pd.DataFrame(data)

# Define the color scheme
colors = ['#4e79a7', '#f28e2b', '#e15759', '#76b7b2', '#59a14f', '#edc949', '#af7aa1', 
          '#ff9da7', '#9c755f', '#bab0ab', '#d62728', '#9467bd', '#8c564b', '#bcbd22', 
          '#17becf']

# Create the figure with specified figure size
fig = plt.figure(figsize=(18, 14))
ax = fig.add_subplot(111, aspect="auto")

# Create a treemap
squarify.plot(sizes=df['Percentage'], label=df['Category'], color=colors, alpha=0.8)

# Set the title of the plot
plt.title('Observation of Celestial Objects by Percentage', fontsize=24, pad=40)

# Remove the axes
plt.axis('off')

# Show the plot
plt.show()