
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    'Item': ['Rock', 'Pop', 'Jazz', 'Classical', 'Hip-Hop', 'Country', 'Reggae', 
             'Electronic', 'Blues', 'Soul', 'Metal', 'Folk', 'Disco', 'Latin', 'Opera'],
    'Quantity': [60, 55, 50, 45, 40, 35, 30, 25, 20, 18, 15, 12, 10, 8, 5]
}

df = pd.DataFrame(data)

colors = ['#FF5733', '#33FF57', '#3357FF', '#F0A500', '#800080', '#00FFFF', 
          '#FF00FF', '#008080', '#FFC0CB', '#0000FF', '#FFD700', '#FF4500', 
          '#7CFC00', '#8A2BE2', '#FF1493']

fig = plt.figure(figsize=(18, 14))
ax = fig.add_subplot(111, aspect="auto")

squarify.plot(sizes=df['Quantity'], label=df['Item'], color=colors, alpha=0.8)

plt.title('Music Album Sales', fontsize=24, pad=30)

plt.axis('off')

plt.show()