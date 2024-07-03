
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Let's define our dataframe
data = {
    'Brand': ['Apple', 'Samsung', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Motorola', 'Nokia', 'Google', 'Sony'],
    'Market Share': [30, 25, 15, 10, 8, 5, 3, 2, 1, 1]
}

df = pd.DataFrame(data)

# Define color list
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FF66B2', '#FFF599', '#CC99FF', '#FF9966', '#99FFFF', '#C4FF99']

# Plot
plt.figure(figsize=(16, 8))
squarify.plot(sizes=df['Market Share'], label=df['Brand'], color=colors, alpha=0.7)

# If you want to remove the axes, uncomment the next line
# plt.axis('off')

plt.title('Smartphone Market Share in 2023')
plt.show()