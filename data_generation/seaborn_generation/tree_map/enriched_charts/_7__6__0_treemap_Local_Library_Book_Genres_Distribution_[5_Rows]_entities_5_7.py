
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Prepare the data
data = {
    'Region': ['North America', 'Europe', 'Asia Pacific', 'Latin America', 'Middle East & Africa', 'Australia', 'Other Regions'],
    'Reach Percentage': [28.7, 22.4, 20.3, 8.9, 6.7, 3.1, 9.9]
}
df = pd.DataFrame(data)

# Create a color palette, mapped to these values
colors = ['#4B0082', '#800080', '#FF1493', '#00BFFF', '#228B22', '#FFD700', '#FF4500']

# Plot
plt.figure(figsize=(16, 10))
squarify.plot(sizes=df['Reach Percentage'], label=df['Region'], color=colors, alpha=0.8)
plt.title('Global Mental Health Awareness Campaign Reach by Region', fontsize=22, fontweight='bold', y=1.05)
plt.axis('off')  # Removes the axes to create a treemap
plt.show()