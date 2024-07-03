
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data
data = {
    'Artwork': ["Mona Lisa", "Starry Night", "The Persistence of Memory", "The Scream",
                "Girl with a Pearl Earring", "The Night Watch", "American Gothic", 
                "The Kiss", "Guernica", "Water Lilies", "The Arnolfini Portrait",
                "The Birth of Venus", "The Garden of Earthly Delights",
                "Liberty Leading the People", "Las Meninas", "The Last Supper"],
    'Exhibitions': [2000, 1800, 1500, 1700, 1600, 1900, 1400, 1300, 2100, 1950, 1200, 1650, 1800, 1550, 2000, 2200]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(16, 10))
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf", "#aec7e8", "#ffbb78", "#98df8a", "#ff9896", "#c5b0d5", "#c49c94"]
squarify.plot(sizes=df['Exhibitions'], label=df['Artwork'], alpha=0.8, color=colors)
plt.title('Number of Exhibitions for Famous Artworks', fontsize=18, pad=20)
plt.axis('off')
plt.show()