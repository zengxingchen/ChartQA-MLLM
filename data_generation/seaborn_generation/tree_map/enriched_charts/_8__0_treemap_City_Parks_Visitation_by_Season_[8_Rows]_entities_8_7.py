
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    'Service': ['Spotify', 'Apple Music', 'Amazon Music', 'YouTube Music', 'Deezer', 'Pandora', 'Tidal', 'SoundCloud', 'iHeartRadio', 'Napster', 'Audiomack', 'Qobuz'],
    'Market Share': [32, 21, 15, 10, 7, 5, 3, 3, 2, 1, 1, 1]
}

df = pd.DataFrame(data)

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#98df8a', '#ffbb78']

plt.figure(figsize=(18, 9))
squarify.plot(sizes=df['Market Share'], label=df['Service'], color=colors, alpha=0.8)
plt.title('Music Streaming Service Market Share in 2023', fontsize=20)
plt.axis('off')
plt.show()