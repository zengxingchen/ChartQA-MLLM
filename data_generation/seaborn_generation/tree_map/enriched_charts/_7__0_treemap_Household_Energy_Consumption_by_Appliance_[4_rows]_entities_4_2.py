
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    "Destination": ["Great Wall of China", "Eiffel Tower", "Machu Picchu", "Grand Canyon", "Louvre Museum",
                    "Great Barrier Reef", "Christ the Redeemer", "Taj Mahal", "Yellowstone National Park",
                    "Disneyland", "Times Square", "Colosseum", "Mount Everest", "Stonehenge", "Niagara Falls"],
    "Category": ["Historical", "Landmark", "Historical", "Natural", "Museum",
                 "Natural", "Landmark", "Historical", "Natural",
                 "Amusement Park", "Landmark", "Historical", "Adventure", "Historical", "Natural"],
    "Visitors": [10, 7, 2, 6, 9, 3, 2, 8, 4, 18, 50, 7, 1, 1, 12]
}

df = pd.DataFrame(data)

color_mapper = {
    'Historical': '#F39C12',  # Orange
    'Landmark': '#2980B9',    # Blue
    'Natural': '#27AE60',     # Green
    'Museum': '#8E44AD',      # Purple
    'Amusement Park': '#E74C3C',  # Red
    'Adventure': '#16A085'   # Teal
}

colors = [color_mapper[category] for category in df['Category']]

fig, ax = plt.subplots(1, figsize=(14, 10))

squarify.plot(sizes=df['Visitors'], label=df['Destination'], color=colors, alpha=0.8, text_kwargs={'fontsize':9})

plt.title('Number of Visitors to Famous Tourist Destinations (in millions)', fontsize=15)
plt.axis('off')
plt.show()