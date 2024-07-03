
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Prepare the data
data = {
    'Country': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 
                'San Diego', 'Dallas', 'San Jose', 'Austin', 'Jacksonville', 'San Francisco', 'Columbus', 
                'Indianapolis', 'Fort Worth', 'Charlotte', 'Seattle', 'Denver', 'Washington D.C.', 'Boston', 
                'El Paso', 'Nashville', 'Detroit', 'Memphis', 'Portland', 'Oklahoma City', 'Las Vegas', 
                'Louisville', 'Baltimore', 'Milwaukee', 'Albuquerque', 'Tucson', 'Fresno', 'Mesa', 
                'Sacramento', 'Atlanta', 'Kansas City', 'Colorado Springs', 'Miami'],
    'Average Monthly Temperature (°C)': [12.3, 17.5, 10.0, 20.9, 24.6, 12.9, 21.7, 18.5, 19.3, 15.5, 20.2, 
                                         22.1, 14.1, 11.2, 11.1, 19.6, 16.8, 11.0, 10.8, 14.5, 11.1, 19.0, 
                                         16.2, 10.0, 17.8, 11.9, 17.1, 21.4, 13.6, 14.0, 9.1, 16.8, 22.4, 
                                         19.0, 23.1, 16.7, 16.0, 13.2, 10.6, 25.1]
}

df = pd.DataFrame(data)

# Create a color palette, mapped to these values
colors = ['#FFA500', '#FF4500', '#1E90FF', '#32CD32', '#FFD700', 
          '#FF69B4', '#8A2BE2', '#00FF7F', '#DC143C', '#00CED1', 
          '#FF6347', '#20B2AA', '#7B68EE', '#8B0000', '#ADFF2F', 
          '#4682B4', '#5F9EA0', '#D2691E', '#4B0082', '#9400D3', 
          '#FF1493', '#FFD700', '#ADFF2F', '#8A2BE2', '#5F9EA0', 
          '#FF4500', '#1E90FF', '#32CD32', '#FFD700', '#FF69B4', 
          '#8A2BE2', '#00FF7F', '#DC143C', '#00CED1', '#FF6347', 
          '#20B2AA', '#7B68EE', '#8B0000', '#ADFF2F', '#4682B4']

# Plot
plt.figure(figsize=(30, 15))
squarify.plot(sizes=df['Average Monthly Temperature (°C)'], label=df['Country'], color=colors, alpha=0.8)
plt.title('Average Monthly Temperature by City', fontsize=24, fontweight='bold', pad=20)
plt.axis('off')  # Removes the axes to create a treemap
plt.show()