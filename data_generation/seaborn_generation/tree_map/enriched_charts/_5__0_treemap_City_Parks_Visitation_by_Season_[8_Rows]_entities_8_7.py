
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Let's define our dataframe
data = {
    'Brand': ['Nike', 'Adidas', 'Under Armour', 'Puma', 'Reebok', 'Asics', 'New Balance', 'Sketchers', 'Converse', 'Fila', 'Lululemon', 'Columbia'],
    'Market Share': [20, 18, 15, 12, 10, 8, 7, 5, 3, 2, 10, 6]
}

df = pd.DataFrame(data)

# Define color list
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#aec7e8', '#ffbb78']

# Plot
plt.figure(figsize=(14, 10))
squarify.plot(sizes=df['Market Share'], label=df['Brand'], color=colors, alpha=0.8)

# If you want to remove the axes, uncomment the next line
plt.axis('off')

plt.title('Market Share of Fitness Brands in 2023')
plt.show()