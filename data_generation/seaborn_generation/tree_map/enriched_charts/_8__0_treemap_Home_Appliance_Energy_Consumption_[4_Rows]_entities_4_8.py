
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data for creating the treemap
data = {
    'Region': ['Northland', 'Southland', 'Eastville', 'Westburg', 'Central City',
               'Laketon', 'Riverside', 'Mountainview', 'Forestown', 'Coastal Area',
               'Sunnyvale', 'Hillside', 'Greenville', 'Lakeside', 'Highlands'],
    'Mental Health Services': [120, 80, 50, 30, 200, 
                               60, 70, 25, 15, 55,
                               95, 40, 65, 45, 35]
}

# Convert the data dictionary to a pandas DataFrame
df = pd.DataFrame(data)

# Define size of the figure
plt.figure(figsize=(14,10))

# Define custom colors using specific color codes
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33FB', '#581845',
          '#DAF7A6', '#FFC300', '#C70039', '#900C3F', '#FF5733',
          '#75FF33', '#33FFA6', '#FF3389', '#5733FF', '#FF335B']

# Create the treemap
squarify.plot(sizes=df['Mental Health Services'], label=df['Region'], color=colors, alpha=0.8)

# Set the title of the treemap
plt.title('Availability of Mental Health Services Across Regions', fontsize=16)

# Remove the axis lines
plt.axis('off')

# Display the treemap
plt.show()