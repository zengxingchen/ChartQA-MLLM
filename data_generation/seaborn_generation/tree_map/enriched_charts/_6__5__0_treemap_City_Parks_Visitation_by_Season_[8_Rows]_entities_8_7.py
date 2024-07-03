
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Let's define our dataframe
data = {
    'Brand': ['Google', 'Microsoft', 'Apple', 'Amazon', 'Facebook', 'Samsung', 'IBM', 'Intel', 'Cisco', 'Oracle', 'Tesla', 'Netflix'],
    'Market Share': [30, 25, 20, 15, 10, 5, 4, 3, 2, 1, 2, 3]
}

df = pd.DataFrame(data)

# Define color list
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f', '#76d7c4', '#ffdf80', '#ffb380', '#94b8b8', '#bfbfbf']

# Plot
plt.figure(figsize=(16, 12))
squarify.plot(sizes=df['Market Share'], label=df['Brand'], color=colors, alpha=0.8)

# If you want to remove the axes, uncomment the next line
plt.axis('off')

plt.title('Market Share of Leading Tech Companies in 2023', fontsize=18)
plt.show()