
import matplotlib.pyplot as plt
import squarify

# Data
labels = [
    'France', 'Spain', 'United States', 'China', 'Italy', 'Turkey', 
    'Mexico', 'Germany', 'Thailand', 'United Kingdom', 'Japan', 'Greece', 
    'Canada', 'Russia', 'Portugal', 'Netherlands', 'Saudi Arabia', 
    'Malaysia', 'Switzerland', 'Australia', 'Austria', 'United Arab Emirates', 
    'South Korea', 'Singapore', 'Indonesia', 'Hungary', 'Morocco', 'Brazil', 
    'Argentina', 'Egypt'
]
sizes = [
    89.4, 83.7, 79.3, 65.7, 64.5, 51.2, 45.0, 39.6, 39.8, 36.3, 31.2, 31.3, 
    30.1, 24.6, 22.8, 21.2, 20.0, 19.0, 17.4, 17.3, 15.6, 15.3, 14.2, 14.1, 
    13.5, 13.1, 12.9, 11.6, 7.5, 7.3
]
colors = [
    "#FF5733", "#33FF57", "#3357FF", "#FF33A6", "#57FF33", "#A633FF", 
    "#FF9633", "#33FF96", "#9633FF", "#FFC233", "#33C2FF", "#C233FF", 
    "#FF33C2", "#33FFC2", "#C2FF33", "#FF6F33", "#336FFF", "#FF336F", 
    "#6FFF33", "#336F6F", "#FF3333", "#3333FF", "#33FF33", "#FF5733", 
    "#5733FF", "#FF33A6", "#33A6FF", "#A6FF33", "#FFA633", "#33FFA6"
]

# Plot
plt.figure(figsize=(16, 10))
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=.8)
plt.title('Top Travel Destinations by Visitor Numbers (Millions)', fontsize=18)
plt.axis('off')
plt.show()