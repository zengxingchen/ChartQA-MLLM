
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data
data = {
    'Manufacturer': ['Apple', 'Samsung', 'Xiaomi', 'Oppo', 'Vivo', 
                     'Huawei', 'Realme', 'Lenovo', 'OnePlus', 'Google',
                     'Sony', 'LG', 'Nokia', 'Motorola', 'HTC', 'ZTE',
                     'Asus', 'TCL', 'Alcatel', 'Others'],
    'Units Sold': [80.8, 69, 44.3, 34.7, 32.1, 9.8, 15.7, 12.1, 20.5, 10.3,
                   8.6, 6.2, 5.7, 4.5, 3.1, 2.8, 2.2, 1.9, 1.5, 45.6]
}

df = pd.DataFrame(data)

# Color scheme picked to be distinct and colorblind accessible
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
          '#ff9896', '#98df8a', '#ffbb78', '#c5b0d5', '#c49c94',
          '#f7b6d2', '#c7c7c7', '#dbdb8d', '#9edae5', '#c7c7c7']

# Plotting the Treemap
plt.figure(figsize=(18, 10))  # Change width and height reasonably
squarify.plot(sizes=df['Units Sold'], label=df['Manufacturer'], color=colors, alpha=0.8)
plt.title('Global Smartphone Sales by Manufacturer - Q4 2021 (Millions of Units)')
plt.axis('off')
plt.show()