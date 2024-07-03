
import matplotlib.pyplot as plt
import pandas as pd
import squarify  # treemap library

# Prepare the data
data = {
    'Region': ['North America', 'North America', 'North America', 'Europe', 'Europe', 
               'Europe', 'Asia', 'Asia', 'Asia', 'South America', 'South America', 'South America',
               'Africa', 'Africa', 'Africa', 'Oceania', 'Oceania', 'Oceania'],
    'Mental_Health_Issue': ['Anxiety', 'Depression', 'PTSD', 'Anxiety', 'Depression', 'OCD', 
                            'Anxiety', 'Depression', 'PTSD', 'Depression', 'PTSD', 'OCD', 
                            'Anxiety', 'Depression', 'OCD', 'Anxiety', 'PTSD', 'OCD'],
    'Incidents': [1200, 1100, 950, 1500, 900, 800, 2000, 1300, 1200, 1400, 1250, 1150, 
                  1000, 1200, 1100, 700, 800, 750]
}

df = pd.DataFrame(data)

# Create a color list
colors = ['#FF6347', '#FFD700', '#ADFF2F', '#4B0082', '#FF1493', '#20B2AA', 
          '#FF4500', '#DA70D6', '#7CFC00', '#4682B4', '#D2691E', '#9ACD32', 
          '#8A2BE2', '#FF69B4', '#2E8B57', '#BA55D3', '#FF8C00', '#00CED1']

# Create a figure with a defined size
plt.figure(figsize=(20, 12))

# Plot
squarify.plot(sizes=df['Incidents'], label=df['Mental_Health_Issue'], color=colors, alpha=0.85)
plt.title('Mental Health Awareness by Region', fontsize=26, y=1.05)

# Remove axes
plt.axis('off')

# Show the plot
plt.show()