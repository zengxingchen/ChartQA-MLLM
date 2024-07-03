
import matplotlib.pyplot as plt
import squarify

# Data
categories = [
    'Cardiovascular Health', 'Mental Health', 'Nutrition & Dietetics', 'Exercise & Fitness', 
    'Sleep & Wellness', 'Alternative Medicine', 'Medical Technology', 'Public Health', 
    'Genetics & Genomics', 'Immunology', 'Pharmacology', 'Epidemiology', 'Occupational Health', 
    'Environmental Health', 'Health Policy', 'Biotechnology', 'Health Psychology', 
    'Global Health', 'Preventive Medicine', 'Palliative Care'
]
values = [
    15000, 13000, 10000, 17000, 12000, 8000, 11000, 14000, 9000, 9500, 
    7000, 6000, 5000, 4000, 3000, 16000, 18000, 20000, 7500, 5500
]

# Colors
colors = [
    '#FF6347', '#FFD700', '#ADFF2F', '#4682B4', '#FF69B4', '#8A2BE2', '#5F9EA0', '#D2691E', 
    '#FF7F50', '#6495ED', '#DC143C', '#00FFFF', '#00008B', '#008B8B', '#B8860B', '#A9A9A9', 
    '#006400', '#BDB76B', '#8B008B', '#556B2F'
]

plt.figure(figsize=(20, 12))

# Treemap
squarify.plot(sizes=values, label=categories, color=colors, alpha=0.8)

plt.title('Health & Psychology Insights', fontsize=24, pad=30)

# Removing axes
plt.axis('off')

# Display the plot
plt.show()