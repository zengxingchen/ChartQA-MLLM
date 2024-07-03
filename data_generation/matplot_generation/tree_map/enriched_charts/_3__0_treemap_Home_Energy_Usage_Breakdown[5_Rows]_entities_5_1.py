
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Define the dataset
data = {
    'Category': ['Renewable Energy', 'Water Conservation', 'Recycling', 'Air Quality', 'Wildlife Protection', 
                 'Deforestation', 'Climate Change', 'Sustainable Agriculture', 'Green Technology', 
                 'Ocean Conservation', 'Urban Planning', 'Pollution Control'],
    'Importance': [25.3, 19.8, 15.7, 12.5, 10.2, 8.3, 6.5, 5.4, 4.6, 3.7, 2.8, 2.1]
}

df = pd.DataFrame(data)

# Define the color scheme
colors = ['#e6194B', '#3cb44b', '#ffe119', '#4363d8', 
          '#f58231', '#911eb4', '#42d4f4', '#f032e6', 
          '#bfef45', '#fabebe', '#469990', '#e6beff']

# Create the figure with specified figure size
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, aspect="auto")

# Create a treemap
squarify.plot(sizes=df['Importance'], label=df['Category'], color=colors, alpha=0.7)

# Set the title of the plot
plt.title('Environmental Issues Importance Treemap', fontsize=22)

# Remove the axes
plt.axis('off')

# Show the plot
plt.show()