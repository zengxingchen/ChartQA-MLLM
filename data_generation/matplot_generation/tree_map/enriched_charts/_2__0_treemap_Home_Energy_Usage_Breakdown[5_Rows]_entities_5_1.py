
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Define the dataset
data = {
    'Type': ['Solar', 'Wind', 'Hydropower', 'Biomass', 'Geothermal', 
             'Ocean', 'Nuclear', 'Hydrogen', 'Tidal', 'Wave', 'Other'],
    'Contribution': [22.5, 20.3, 17.8, 11.2, 7.9, 
                     6.4, 5.1, 3.5, 2.6, 2.1, 1.6]
}

df = pd.DataFrame(data)

# Define the color scheme
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', 
          '#92A8D1', '#955251', '#B565A7', '#009B77', 
          '#DD4124', '#45B8AC', '#EFC050']

# Create the figure with specified figure size
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, aspect="auto")

# Create a treemap
squarify.plot(sizes=df['Contribution'], label=df['Type'], color=colors, alpha=0.7)

# Set the title of the plot
plt.title('Renewable Energy Sources Contribution to Global Energy Production', fontsize=22)

# Remove the axes
plt.axis('off')

# Show the plot
plt.show()