
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Define the dataset
data = {
    'Category': ['Solar Energy', 'Wind Energy', 'Hydropower', 'Geothermal', 'Biomass', 
                 'Nuclear', 'Fossil Fuels', 'Hydrogen', 'Tidal Energy', 'Wave Energy', 
                 'Algal Biofuel', 'Waste-to-Energy', 'Ocean Thermal', 'Fuel Cells', 'Compressed Air'],
    'Percentage': [25.45, 18.23, 15.67, 11.12, 8.95, 7.88, 4.76, 3.56, 2.89, 1.89, 
                   1.23, 1.09, 0.88, 0.69, 0.61]
}

df = pd.DataFrame(data)

# Define the color scheme
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#ffcccb', '#ffdab9',
          '#e9967a', '#da70d6', '#b0e0e6', '#afeeee', '#dda0dd', '#db7093', '#ff4500']

# Create the figure with specified figure size
fig = plt.figure(figsize=(16, 12))
ax = fig.add_subplot(111, aspect="auto")

# Create a treemap
squarify.plot(sizes=df['Percentage'], label=df['Category'], color=colors, alpha=0.8)

# Set the title of the plot
plt.title('Renewable Energy Sources by Percentage', fontsize=24, pad=30)

# Remove the axes
plt.axis('off')

# Show the plot
plt.show()