
import matplotlib.pyplot as plt
import squarify

# Data
categories = [
    'Astronomy', 'Botany', 'Zoology', 'Geology', 'Meteorology', 'Oceanography', 'Paleontology', 
    'Ecology', 'Genetics', 'Microbiology', 'Neuroscience', 'Physics', 'Chemistry', 
    'Environmental Science', 'Biochemistry', 'Space Exploration', 'Quantum Mechanics', 
    'Astrophysics', 'Climatology', 'Marine Biology', 'Evolutionary Biology', 'Horticulture', 
    'Entomology', 'Hydrology'
]
values = [
    15000, 13000, 10000, 17000, 12000, 8000, 11000, 14000, 9000, 9500, 7000, 6000, 
    5000, 4000, 3000, 16000, 18000, 20000, 7500, 5500, 10500, 7200, 6900, 9800
]

# Colors
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#A633FF', '#33FFA6', '#FF8C33', 
    '#8C33FF', '#33FF8C', '#8CFF33', '#5733FF', '#33A6FF', '#FF338C', '#A6FF33', 
    '#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#A633FF', '#33FFA6', '#FF8C33', 
    '#8C33FF', '#33FF8C', '#8CFF33'
]

plt.figure(figsize=(24, 14))

# Treemap
squarify.plot(sizes=values, label=categories, color=colors, alpha=0.8)

plt.title('Science & Nature Insights', fontsize=24, pad=30)

# Removing axes
plt.axis('off')

# Display the plot
plt.show()