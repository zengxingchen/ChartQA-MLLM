
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Let's define our dataframe
data = {
    'Category': ['Laptops', 'Smartphones', 'Tablets', 'Desktops', 'Wearables', 'Accessories', 'Software', 'Services', 'Gaming Consoles', 'Smart Home Devices', 'Cameras', 'Printers'],
    'Sales': [150, 120, 100, 80, 60, 50, 40, 30, 25, 20, 15, 10]
}

df = pd.DataFrame(data)

# Define color list
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#c5b0d5', '#ff9896']

# Plot
plt.figure(figsize=(14, 10))
squarify.plot(sizes=df['Sales'], label=df['Category'], color=colors, alpha=0.8)

# If you want to remove the axes, uncomment the next line
plt.axis('off')

plt.title('Sales Distribution of Tech Products in 2023', fontsize=20, pad=20)
plt.show()