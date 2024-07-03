
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data for the treemap
data = {
    'Genre': ['Mystery', 'Romance', 'Science Fiction', 'Fantasy', 'Thriller', 'Horror', 'Historical', 'Young Adult', 'Literary Fiction', 'Dystopian'],
    'Market_Share': [0.15, 0.18, 0.12, 0.14, 0.10, 0.07, 0.09, 0.11, 0.04, 0.05]
}

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Define color list
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#ff6666', '#c4e17f', '#6e6e6e', '#b3b3b3']

# Plot the Treemap
plt.figure(figsize=(14, 10))
squarify.plot(sizes=df['Market_Share'], label=df['Genre'], color=colors, alpha=0.8)
plt.title('Popular Fiction Genres and Their Market Share', fontsize=20, y=1.05)
plt.axis('off')
plt.show()