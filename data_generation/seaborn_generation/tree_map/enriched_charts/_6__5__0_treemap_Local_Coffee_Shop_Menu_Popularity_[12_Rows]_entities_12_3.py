
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data
data = {
    'Topic': ['Renewable Energy', 'Electric Vehicles', 'Smart Grids', 'Green Buildings', 'Recycling', 
              'Water Purification', 'Solar Energy', 'Wind Energy', 'Energy Storage', 'Geothermal Energy', 
              'Biomass Energy', 'Wave Energy', 'Carbon Capture', 'Hydrogen Fuel', 'Sustainable Agriculture', 
              'Eco-Tourism', 'Clean Transportation', 'Urban Planning', 'Environmental Monitoring', 'Forest Conservation', 
              'Pollution Control', 'Wildlife Protection', 'Ozone Layer Protection', 'Marine Conservation'],
    'Amount (Billions)': [320.5, 275.3, 190.8, 160.2, 140.6, 
                          125.7, 115.4, 105.8, 95.3, 85.6, 
                          75.2, 65.9, 60.4, 55.8, 50.1, 
                          45.6, 40.8, 35.7, 30.5, 25.3,
                          20.8, 15.6, 10.5, 5.4]
}

df = pd.DataFrame(data)

# Color scheme
colors = ['#4CAF50', '#FF9800', '#2196F3', '#9C27B0', '#FFC107', 
          '#E91E63', '#8BC34A', '#00BCD4', '#FF5722', '#3F51B5', 
          '#CDDC39', '#009688', '#673AB7', '#F44336', '#795548', 
          '#607D8B', '#00E5FF', '#76FF03', '#FF6F00', '#D500F9', 
          '#AA00FF', '#FF4081', '#651FFF', '#00BFA5']

# Plotting the Treemap
plt.figure(figsize=(20, 12))  # Change width and height reasonably
squarify.plot(sizes=df['Amount (Billions)'], label=df['Topic'], color=colors, alpha=0.8)
plt.title('Investment in Environmental Technologies - 2021 (Billions USD)', fontsize=20, fontweight='bold', y=1.05)
plt.axis('off')
plt.show()