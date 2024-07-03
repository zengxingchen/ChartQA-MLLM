
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Prepare the data
data = {
    'Category': ['Vegetables', 'Fruits', 'Grains', 'Proteins', 'Dairy', 'Fats and Oils',
                 'Sugars and Sweets', 'Beverages', 'Spices and Herbs', 'Condiments', 'Other'],
    'Market Share': [30.5, 20.0, 15.0, 10.0, 8.0, 7.0, 5.0, 2.5, 1.5, 0.5, 5.0]
}
df = pd.DataFrame(data)

# Create a color palette, mapped to these values
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF', 
          '#FF8C33', '#33FFF0', '#8CFF33', '#5733FF', '#FF3333', '#33FF8C']

# Plot
plt.figure(figsize=(18, 9))
squarify.plot(sizes=df['Market Share'], label=df['Category'], color=colors, alpha=0.8)
plt.title('Market Share of Different Food Categories', fontsize=18, fontweight='bold', pad=30)
plt.axis('off')  # Removes the axes to create a treemap
plt.show()