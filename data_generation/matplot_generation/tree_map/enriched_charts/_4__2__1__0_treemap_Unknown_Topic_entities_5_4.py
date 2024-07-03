
import matplotlib.pyplot as plt
import squarify

# Data
landmarks = ['Great Wall of China', 'Eiffel Tower', 'Statue of Liberty', 'Machu Picchu', 'Christ the Redeemer', 'Colosseum', 'Taj Mahal', 'Louvre Museum', 'Grand Canyon', 'Great Barrier Reef', 'Stonehenge', 'Sydney Opera House', 'Pyramids of Giza', 'Mount Everest', 'Niagara Falls', 'Times Square', 'Disneyland', 'Universal Studios', 'Golden Gate Bridge', 'Santorini']
visitors = [10000000, 7000000, 4200000, 1500000, 2000000, 7500000, 8000000, 9000000, 6000000, 2000000, 1200000, 8000000, 1400000, 500000, 12000000, 50000000, 18000000, 11000000, 13000000, 2000000]

# Colors
colors = ['#FF6347', '#FFD700', '#8A2BE2', '#7FFF00', '#FF4500', '#6495ED', '#FF69B4', '#1E90FF', '#DC143C', '#00CED1', '#FF1493', '#7B68EE', '#D2691E', '#00FA9A', '#9400D3', '#FFB6C1', '#9370DB', '#48D1CC', '#ADFF2F', '#FF7F50']

plt.figure(figsize=(18, 14))

# Treemap
squarify.plot(sizes=visitors, label=landmarks, color=colors, alpha=0.85)

plt.title('Annual Visitors to Famous Landmarks', fontsize=24, pad=20)

# Removing axes
plt.axis('off')

# Display the plot
plt.show()