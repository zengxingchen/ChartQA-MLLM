
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Define the dataset
data = {
    'Topic': ['Fiction', 'Mystery', 'Romance', 'Science Fiction', 'Fantasy', 'Biography', 
              'History', 'Self-help', 'Travel', 'Science', 'Health', 'Philosophy'],
    'Percentage': [20.5, 15.0, 12.5, 10.0, 8.5, 7.0, 6.0, 5.5, 4.5, 3.5, 2.5, 2.0]
}

df = pd.DataFrame(data)

# Define the color scheme
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', 
          '#c2c2f0', '#ffb3e6', '#c4e17f', '#ff6666', 
          '#f0e68c', '#ffd700', '#f08080', '#cd5c5c']

# Create the figure with specified figure size
fig = plt.figure(figsize=(16, 12))
ax = fig.add_subplot(111, aspect="auto")

# Create a treemap
squarify.plot(sizes=df['Percentage'], label=df['Topic'], color=colors, alpha=0.8)

# Set the title of the plot
plt.title('Popular Book Genres by Percentage', fontsize=24)

# Remove the axes
plt.axis('off')

# Show the plot
plt.show()