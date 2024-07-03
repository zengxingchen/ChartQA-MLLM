
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    'Item': ['Athletics', 'Swimming', 'Cycling', 'Basketball', 'Football', 'Tennis', 
             'Golf', 'Boxing', 'Gymnastics', 'Hockey', 'Martial Arts', 'Rugby', 
             'Skating', 'Skiing', 'Surfing'],
    'Quantity': [75, 68, 60, 55, 50, 45, 40, 35, 30, 28, 25, 22, 20, 18, 15]
}

df = pd.DataFrame(data)

colors = ['#FF5733', '#33FF57', '#3357FF', '#F0A500', '#800080', '#00FFFF', 
          '#FF00FF', '#008080', '#FFC0CB', '#0000FF', '#FFD700', '#FF4500', 
          '#7CFC00', '#8A2BE2', '#FF1493']

fig = plt.figure(figsize=(20, 16))
ax = fig.add_subplot(111, aspect="auto")

squarify.plot(sizes=df['Quantity'], label=df['Item'], color=colors, alpha=0.8)

plt.title('Popular Sports Participation Rates', fontsize=28, pad=40)

plt.axis('off')

plt.show()