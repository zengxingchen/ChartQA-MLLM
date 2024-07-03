
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Prepare the data
data = {
    'Region': ['North America', 'Europe', 'Asia Pacific', 'Latin America', 'Middle East & Africa', 'Australia', 'China', 'Japan', 'India', 'Other Regions'],
    'Market Share Percentage': [25.6, 20.1, 18.7, 12.4, 8.3, 5.9, 4.5, 3.7, 3.1, 10.7]
}
df = pd.DataFrame(data)

# Create a color palette, mapped to these values
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

# Plot
plt.figure(figsize=(18, 12))
squarify.plot(sizes=df['Market Share Percentage'], label=df['Region'], color=colors, alpha=0.8)
plt.title('Future Technologies Market Share by Region', fontsize=24, fontweight='bold', y=1.05)
plt.axis('off')  # Removes the axes to create a treemap
plt.show()