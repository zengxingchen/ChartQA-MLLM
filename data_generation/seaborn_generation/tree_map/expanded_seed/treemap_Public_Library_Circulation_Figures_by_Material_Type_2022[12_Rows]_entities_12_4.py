
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Seaborn for color palettes
import seaborn as sns

# Your data
data = [
    {'Material Type': 'Adult Fiction', 'Circulation (in millions)': 34},
    {'Material Type': 'Adult Non-Fiction', 'Circulation (in millions)': 28},
    {'Material Type': "Children's Fiction", 'Circulation (in millions)': 44},
    {'Material Type': "Children's Picture Books", 'Circulation (in millions)': 31},
    {'Material Type': 'Young Adult Fiction', 'Circulation (in millions)': 17},
    {'Material Type': 'Young Adult Non-Fiction', 'Circulation (in millions)': 9},
    {'Material Type': 'DVD/Blu-ray', 'Circulation (in millions)': 25},
    {'Material Type': 'Audiobooks', 'Circulation (in millions)': 14},
    {'Material Type': 'eBooks', 'Circulation (in millions)': 40},
    {'Material Type': 'eAudiobooks', 'Circulation (in millions)': 22},
    {'Material Type': 'Magazines', 'Circulation (in millions)': 12},
    {'Material Type': 'Digital Magazines', 'Circulation (in millions)': 8},
]

# Create a DataFrame
df = pd.DataFrame(data)

# Use a seaborn color palette with as many colors as categories
cmap = sns.color_palette("Spectral", n_colors=len(df['Material Type']))
plt.figure(figsize=(12, 8))

# Create a squarify treemap
squarify.plot(sizes=df['Circulation (in millions)'],
              label=df['Material Type'],
              color=cmap,
              alpha=0.8,
              text_kwargs={'fontsize': 9})

plt.title('Circulation of Library Material Types (in millions)')
plt.axis('off')
plt.show()