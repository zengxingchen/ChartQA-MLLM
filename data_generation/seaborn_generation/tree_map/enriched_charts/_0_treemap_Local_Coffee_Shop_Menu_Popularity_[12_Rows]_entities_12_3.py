
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data
data = {
    'Manufacturer': ['Apple', 'Samsung', 'Xiaomi', 'Oppo', 'Vivo', 
                     'Huawei', 'Realme', 'Lenovo', 'Others'],
    'Units Sold': [80.8, 69, 44.3, 34.7, 32.1, 9.8, 15.7, 12.1, 45.6]
}

df = pd.DataFrame(data)

# Color scheme picked to be distinct and colorblind accessible
colors = ['#5A9', '#E58606', '#5D69B1', '#52BCA3', '#99C945', 
          '#CC61B0', '#24796C', '#DAA51B', '#2F8AC4']

# Plotting the Treemap
plt.figure(figsize=(16, 9))  # Change width and height reasonably
squarify.plot(sizes=df['Units Sold'], label=df['Manufacturer'], color=colors, alpha=0.8)
plt.title('Global Smartphone Sales by Manufacturer - Q4 2021 (Millions of Units)')
plt.axis('off')
plt.show()