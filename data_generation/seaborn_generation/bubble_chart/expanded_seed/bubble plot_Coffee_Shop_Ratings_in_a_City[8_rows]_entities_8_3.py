
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data provided in a list of dictionaries
data = [
    {'Coffee Shop Name': 'Bean Flickers', 'Neighborhood': 'Downtown', 'Google Rating': 4.6, 'Number of Reviews': 1250, 'Bubble Size (Visits per Month)': 2100},
    {'Coffee Shop Name': "Cup o' Joe", 'Neighborhood': 'Arts District', 'Google Rating': 4.9, 'Number of Reviews': 850, 'Bubble Size (Visits per Month)': 1200},
    {'Coffee Shop Name': 'Steamy Beans', 'Neighborhood': 'Financial Quarter', 'Google Rating': 4.3, 'Number of Reviews': 1500, 'Bubble Size (Visits per Month)': 2300},
    {'Coffee Shop Name': 'Brewed Awakening', 'Neighborhood': 'North End', 'Google Rating': 4.8, 'Number of Reviews': 670, 'Bubble Size (Visits per Month)': 1000},
    {'Coffee Shop Name': 'The Grind House', 'Neighborhood': 'South End', 'Google Rating': 4.2, 'Number of Reviews': 2000, 'Bubble Size (Visits per Month)': 3300},
    {'Coffee Shop Name': 'Mocha Motion', 'Neighborhood': 'West Side', 'Google Rating': 4.5, 'Number of Reviews': 750, 'Bubble Size (Visits per Month)': 800},
    {'Coffee Shop Name': 'Java Lava', 'Neighborhood': 'East Village', 'Google Rating': 4.7, 'Number of Reviews': 1100, 'Bubble Size (Visits per Month)': 1500},
    {'Coffee Shop Name': 'Perk Up!', 'Neighborhood': 'Midtown', 'Google Rating': 4.4, 'Number of Reviews': 1800, 'Bubble Size (Visits per Month)': 2800}
]

# Convert the list of dictionaries to a Pandas DataFrame
df = pd.DataFrame(data)

# Define the size for the plots, fitting the number of neighborhoods
plt.figure(figsize=(10, 8))

# Create the bubble chart using Seaborn's scatterplot method
# The size of each point is proportional to the 'Bubble Size (Visits per Month)'
# 'hue' parameter is used for coloring points based on the 'Google Rating'
bubble_chart = sns.scatterplot(data=df,
                               x='Number of Reviews',
                               y='Neighborhood',
                               size='Bubble Size (Visits per Month)',
                               hue='Google Rating',
                               sizes=(100, 2000),  # Bubble size range
                               alpha=0.7,  # Transparency of the bubbles
                               palette='coolwarm')  # Color palette

# Add a legend outside the plot
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

# Title and labels for clarity
plt.title('Bubble Chart of Coffee Shops')
plt.xlabel('Number of Reviews')
plt.ylabel('Neighborhood')

# Display the bubble chart
plt.tight_layout()
plt.show()