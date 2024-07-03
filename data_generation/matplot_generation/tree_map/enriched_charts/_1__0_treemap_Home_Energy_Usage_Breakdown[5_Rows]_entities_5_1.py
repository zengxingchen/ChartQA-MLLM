
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Define the dataset
data = {
    'Genre': ['Pop', 'Rock', 'Hip-Hop', 'Jazz', 'Classical', 'Electronic',
              'Reggae', 'Country', 'Blues', 'Soul', 'Folk', 'R&B', 'Latin', 'Metal', 'Disco'],
    'Popularity': [27.35, 21.88, 19.67, 9.54, 7.45, 5.82, 
                   3.95, 2.78, 1.89, 1.55, 1.29, 1.03, 0.9, 0.7, 0.56]
}

df = pd.DataFrame(data)

# Define the color scheme
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', 
          '#c2c2f0', '#ffb3e6', '#c4e17f', '#76a5af', 
          '#ffb380', '#aaffc3', '#ffd700', '#bcf60c', 
          '#fabebe', '#008080', '#e6beff']

# Create the figure with specified figure size
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, aspect="auto")

# Create a treemap
squarify.plot(sizes=df['Popularity'], label=df['Genre'], color=colors, alpha=0.8)

# Set the title of the plot
plt.title('Popularity of Music Genres', fontsize=22, pad=20)

# Remove the axes
plt.axis('off')

# Show the plot
plt.show()