
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    "Category": ["Film Industry"] * 15,
    "Subcategory": ["Action", "Drama", "Comedy", "Thriller", "Romance",
                    "Documentary", "Horror", "Animation", "Sci-Fi", "Fantasy",
                    "Adventure", "Musical", "Biography", "Crime", "War"],
    "Value": [350000, 280000, 250000, 300000, 240000,
              220000, 180000, 260000, 310000, 230000,
              270000, 200000, 190000, 210000, 220000]
}

df = pd.DataFrame(data)

color_mapper = {
    'Film Industry': ['#FF4500', '#FFD700', '#00FF00', '#00FFFF', '#0000FF', 
                      '#8A2BE2', '#A52A2A', '#DEB887', '#5F9EA0', '#7FFF00', 
                      '#D2691E', '#FF7F50', '#6495ED', '#DC143C', '#00CED1']
}

colors = color_mapper['Film Industry']

fig, ax = plt.subplots(1, figsize=(20, 16))

squarify.plot(sizes=df['Value'], label=df['Subcategory'], color=colors, alpha=0.8, text_kwargs={'fontsize':10})

plt.title('Investment Distribution in Film Industry', fontsize=22)
plt.axis('off')
plt.show()