
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data for creating the treemap
data = {
    'Destination': ['Paris', 'New York', 'Tokyo', 'Sydney', 'Rome', 
                    'London', 'Bangkok', 'Dubai', 'Barcelona', 'Istanbul', 
                    'Amsterdam', 'Hong Kong', 'Singapore', 'Los Angeles', 'Cape Town',
                    'Rio de Janeiro', 'Moscow', 'Mexico City', 'Venice', 'Buenos Aires'],
    'Popularity': [5000, 4500, 4200, 4000, 3900, 
                   3800, 3700, 3600, 3500, 3400, 
                   3300, 3200, 3100, 3000, 2900, 
                   2800, 2700, 2600, 2500, 2400]
}

# Convert the data dictionary to a pandas DataFrame
df = pd.DataFrame(data)

# Define size of the figure
plt.figure(figsize=(16,12))

# Define custom colors using specific color codes
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700',
          '#ADFF2F', '#FFB6C1', '#20B2AA', '#FF69B4', '#87CEFA',
          '#32CD32', '#FF4500', '#DA70D6', '#F4A460', '#9ACD32',
          '#8B0000', '#00CED1', '#FF6347', '#7B68EE', '#6A5ACD']

# Create the treemap
squarify.plot(sizes=df['Popularity'], label=df['Destination'], color=colors, alpha=0.8)

# Set the title of the treemap
plt.title('Travel Destination Popularity', fontsize=18, y=1.05)

# Remove the axis lines
plt.axis('off')

# Display the treemap
plt.show()