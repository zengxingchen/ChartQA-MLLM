
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Let's define our dataframe
data = {
    'Brand': ['Apple', 'Samsung', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Sony', 'LG', 'OnePlus', 'Nokia', 'Asus', 'Google', 'Motorola', 'HTC'],
    'Revenue': [280, 220, 150, 130, 120, 110, 90, 70, 60, 50, 40, 30, 20, 10]
}

df = pd.DataFrame(data)

# Define color list
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f', '#76d7c4', '#ff6f61', '#6b5b95', '#88b04b', '#d65076', '#45b8ac', '#e27a3f']

# Plot
plt.figure(figsize=(16, 12))
squarify.plot(sizes=df['Revenue'], label=df['Brand'], color=colors, alpha=0.8)

# If you want to remove the axes, uncomment the next line
plt.axis('off')

plt.title('Revenue of Smartphone Brands in 2023')
plt.show()