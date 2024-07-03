
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import squarify  # You may need to install this package if you haven't already

# Insert the table data here
data = {
    'Category': ['Fruits', 'Vegetables', 'Grains', 'Dairy', 'Meat', 'Fish', 'Nuts', 'Sweets', 'Beverages', 'Spices', 'Condiments', 'Fats'],
    'Emissions': [180, 160, 120, 100, 200, 140, 80, 60, 90, 70, 50, 110]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(14, 7))
colors = ["#3498db", "#e74c3c", "#2ecc71", "#f1c40f", "#9b59b6", "#34495e", "#1abc9c", "#e67e22", "#ecf0f1", "#95a5a6", "#d35400", "#c0392b"]
squarify.plot(sizes=df['Emissions'], label=df['Category'], alpha=0.8, color=colors)
plt.title('Distribution of Food Categories by Emissions', fontsize=18, pad=20)
plt.axis('off')
plt.show()