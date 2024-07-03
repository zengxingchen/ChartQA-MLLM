
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Define the dataset
data = {
    'Genre': ['Pop', 'Rock', 'Hip-Hop', 'Country', 'Jazz', 'Classical', 
              'Electronic', 'Reggae', 'Blues', 'Folk', 'Other'],
    'Market Share': [25.4, 20.1, 15.7, 12.3, 7.8, 6.9, 4.5, 3.8, 2.6, 1.9, 2.0]
}

df = pd.DataFrame(data)

# Define the color scheme
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', 
          '#33FFF3', '#FFA833', '#FF3333', '#33FFA8', 
          '#A833FF', '#5733FF', '#FF33F6']

# Create the figure with specified figure size
fig = plt.figure(figsize=(16, 12))
ax = fig.add_subplot(111, aspect="auto")

# Create a treemap
squarify.plot(sizes=df['Market Share'], label=df['Genre'], color=colors, alpha=0.8)

# Set the title of the plot
plt.title('Popular Music Genres by Market Share', fontsize=24)

# Remove the axes
plt.axis('off')

# Show the plot
plt.show()