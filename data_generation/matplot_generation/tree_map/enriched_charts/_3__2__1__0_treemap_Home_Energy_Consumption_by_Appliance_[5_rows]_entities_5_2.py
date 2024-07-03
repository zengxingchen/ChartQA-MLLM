
import matplotlib.pyplot as plt
import squarify

# Data
labels = [
    'United States', 'China', 'Japan', 'Germany', 'India', 'United Kingdom', 
    'France', 'Brazil', 'Italy', 'Canada', 'South Korea', 'Russia', 
    'Australia', 'Spain', 'Mexico', 'Indonesia', 'Netherlands', 'Saudi Arabia', 
    'Turkey', 'Switzerland', 'Argentina', 'Sweden', 'Poland', 'Belgium', 
    'Thailand', 'Nigeria', 'Austria', 'Norway', 'Iran', 'South Africa'
]
sizes = [
    21433, 14343, 5082, 3846, 2875, 2827, 2716, 1839, 2001, 1643, 1646, 1634, 
    1392, 1400, 1250, 1119, 902, 792, 743, 707, 449, 531, 595, 529, 501, 448, 
    459, 418, 470, 351
]
colors = [
    "#FF5733", "#33FF57", "#3357FF", "#FF33A6", "#57FF33", "#A633FF", 
    "#FF9633", "#33FF96", "#9633FF", "#FFC233", "#33C2FF", "#C233FF", 
    "#FF33C2", "#33FFC2", "#C2FF33", "#FF6F33", "#336FFF", "#FF336F", 
    "#6FFF33", "#336F6F", "#FF3333", "#3333FF", "#33FF33", "#FF5733", 
    "#5733FF", "#FF33A6", "#33A6FF", "#A6FF33", "#FFA633", "#33FFA6"
]

# Plot
plt.figure(figsize=(14, 8))
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=.8)
plt.title('Top 30 Countries by GDP in Billion USD')
plt.axis('off')
plt.show()