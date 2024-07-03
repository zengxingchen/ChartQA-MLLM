
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Define the dataframe
data = {
    'Service': ['Netflix', 'Amazon Prime', 'Disney+', 'Hulu', 'HBO Max', 'Apple TV+', 'Peacock', 'Paramount+', 'Discovery+', 'YouTube Premium', 'Sling TV', 'Crunchyroll'],
    'Market Share': [25, 20, 18, 10, 8, 7, 5, 3, 2, 1, 0.5, 0.5]
}

df = pd.DataFrame(data)

# Define color list
colors = ['#ff6347', '#4682b4', '#32cd32', '#8a2be2', '#ff4500', '#da70d6', '#ff1493', '#00ced1', '#ffd700', '#adff2f', '#ffa07a', '#87ceeb']

# Plot
plt.figure(figsize=(16, 12))
squarify.plot(sizes=df['Market Share'], label=df['Service'], color=colors, alpha=0.8)

# Remove axes
plt.axis('off')

plt.title('Market Share of Leading Streaming Services in 2023', fontsize=18, fontweight='bold', pad=20)
plt.show()