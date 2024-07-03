
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Prepare the data
data = {
    'Region': ['North America', 'Europe', 'Asia Pacific', 'Latin America', 'Middle East & Africa', 'Australia', 'Scandinavia', 'Eastern Europe', 'South Asia', 'Sub-Saharan Africa'],
    'Market Share': [33.2, 28.5, 20.1, 8.4, 4.6, 2.3, 1.5, 1.4, 0.8, 0.2]
}
df = pd.DataFrame(data)

# Create a color palette, mapped to these values
colors = ['#FF6347', '#FFA07A', '#FFD700', '#ADFF2F', '#20B2AA', '#1E90FF', '#9370DB', '#FF69B4', '#FF4500', '#708090']

# Plot
plt.figure(figsize=(20, 10))
squarify.plot(sizes=df['Market Share'], label=df['Region'], color=colors, alpha=0.8)
plt.title('Global Art & Design Market Share by Region', fontsize=22, fontweight='bold', pad=20)
plt.axis('off')  # Removes the axes to create a treemap
plt.show()