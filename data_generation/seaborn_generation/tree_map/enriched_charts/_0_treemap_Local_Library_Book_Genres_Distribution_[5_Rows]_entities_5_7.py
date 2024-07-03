
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Prepare the data
data = {
    'Manufacturer': ['Samsung', 'Apple', 'Huawei', 'Xiaomi', 'OPPO', 'Vivo', 
                     'Motorola', 'Lenovo', 'LG', 'Realme', 'Others'],
    'Market Share': [31.1, 21.2, 9.1, 8.9, 5.7, 4.7, 3.4, 2.9, 2.6, 1.9, 8.5]
}
df = pd.DataFrame(data)

# Create a color palette, mapped to these values
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FFFF99', 
          '#FF66CC', '#CC99FF', '#FF9966', '#99CCFF', '#66FFB2', '#C0C0C0']

# Plot
plt.figure(figsize=(20, 10))
squarify.plot(sizes=df['Market Share'], label=df['Manufacturer'], color=colors, alpha=0.7)
plt.title('Global Smartphone Market Share by Manufacturer', fontsize=20, fontweight='bold')
plt.axis('off')  # Removes the axes to create a treemap
plt.show()