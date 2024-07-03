
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Let's define our dataframe
data = {
    'Category': ['Pop Music', 'Classical Music', 'Jazz', 'Rock', 'Hip-Hop', 'Country', 'Reggae', 'Electronic', 'Blues', 'Folk', 'Latin', 'Soul', 'Funk', 'Disco', 'Gospel', 'Opera'],
    'Sales': [300, 250, 200, 150, 120, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 5]
}

df = pd.DataFrame(data)

# Define color list
colors = ['#FF6347', '#FFD700', '#ADFF2F', '#40E0D0', '#1E90FF', '#FF69B4', '#BA55D3', '#8A2BE2', '#FF4500', '#32CD32', '#F0E68C', '#EE82EE', '#8B0000', '#00CED1', '#FF1493', '#7FFF00']

# Plot
plt.figure(figsize=(16, 12))
squarify.plot(sizes=df['Sales'], label=df['Category'], color=colors, alpha=0.8)

# If you want to remove the axes, uncomment the next line
plt.axis('off')

plt.title('Music Genre Popularity in 2023', fontsize=24, pad=30)
plt.show()