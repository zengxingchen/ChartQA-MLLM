
import matplotlib.pyplot as plt

# Define the data
stars = ["Sirius", "Canopus", "Alpha Centauri", "Arcturus", "Vega", "Capella", 
         "Rigel", "Procyon", "Achernar", "Betelgeuse", "Hadar", "Altair", 
         "Aldebaran", "Antares", "Spica", "Pollux", "Fomalhaut", "Deneb", 
         "Regulus", "Adhara"]
distance = [8.6, 310, 4.37, 36.7, 25, 42.9, 863, 11.4, 139, 642.5, 391, 16.7, 
            65.3, 550, 262, 34, 25, 1400, 79, 430] # in light years
brightness = [1.42, 0.72, 1.33, 1.08, 0.58, 0.91, 0.18, 0.40, 0.46, 0.45, 0.61, 
              0.76, 0.75, 0.60, 0.92, 1.16, 1.16, 1.25, 1.35, 0.70] # relative to sun
age = [0.242, 10.0, 5.0, 7.1, 0.455, 0.79, 8.0, 1.87, 0.24, 8.0, 12.0, 1.2, 6.6, 
       11.4, 12.5, 0.72, 0.44, 10.0, 0.125, 5.1] # in billion years
colors = ["#FF6F61", "#FF9A8B", "#FFDDC1", "#FFA07A", "#FFD700", "#FFC0CB", 
          "#B0E0E6", "#ADD8E6", "#87CEFA", "#4682B4", "#4169E1", "#191970", 
          "#6495ED", "#1E90FF", "#00BFFF", "#87CEEB", "#4682B4", "#4169E1", 
          "#1E90FF", "#191970"]

# Size corresponds to the brightness
sizes = [brightness_value * 100 for brightness_value in brightness]

# Create the plot
plt.figure(figsize=(18, 12))

for i in range(len(stars)):
    plt.scatter(distance[i], age[i], s=sizes[i], c=colors[i], alpha=0.6, edgecolors="w", linewidth=2)

# Customizations
plt.title('Distances, Ages, and Brightness of Various Stars in the Galaxy', pad=20)
plt.xlabel('Distance in Light Years')
plt.ylabel('Age in Billion Years')
plt.grid(True)

# Add a legend for star colors
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=colors[i], label=stars[i]) for i in range(len(stars))]
plt.legend(handles=legend_elements, title="Stars", bbox_to_anchor=(1.05, 1), loc='upper left')

plt.show()