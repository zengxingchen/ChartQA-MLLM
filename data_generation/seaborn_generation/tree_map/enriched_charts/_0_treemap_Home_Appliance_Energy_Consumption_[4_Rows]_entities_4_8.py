
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data for creating the treemap
data = {
    'Region': ['Northland', 'Southland', 'Eastville', 'Westburg', 'Central City',
               'Laketon', 'Riverside', 'Mountainview', 'Forestown', 'Coastal Area'],
    'Population': [1200000, 800000, 500000, 300000, 2000000, 
                   600000, 700000, 250000, 150000, 550000]
}

# Convert the data dictionary to a pandas DataFrame
df = pd.DataFrame(data)

# Define size of the figure
plt.figure(figsize=(12,8))

# Define custom colors using specific color codes
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33FB', '#581845',
          '#DAF7A6', '#FFC300', '#C70039', '#900C3F', '#FF5733']

# Create the treemap
squarify.plot(sizes=df['Population'], label=df['Region'], color=colors, alpha=0.7)

# Set the title of the treemap
plt.title('Population Distribution Across Imaginary Regions')

# Remove the axis lines
plt.axis('off')

# Display the treemap
plt.show()