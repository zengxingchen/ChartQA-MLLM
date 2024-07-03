
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Create the dataframe
df = pd.DataFrame({
    'Field': ['Apple', 'Microsoft', 'Amazon', 'Google', 'Facebook', 'Tesla', 'Alibaba', 'Samsung', 'Intel', 
              'IBM', 'Sony', 'Tencent', 'NVIDIA', 'Oracle', 'Netflix', 'Adobe', 'Salesforce', 'Uber', 
              'Spotify', 'Zoom', 'Snap', 'Shopify', 'PayPal', 'Twitter', 'Square'],
    'Revenue (in billions)': [274.5, 143.0, 386.1, 181.7, 85.9, 31.5, 109.5, 200.7, 77.9, 73.6, 76.2, 69.9, 
                              16.7, 40.5, 25.0, 12.9, 21.3, 11.1, 9.0, 2.6, 2.5, 2.9, 21.4, 3.7, 9.5]
})

# Custom colors for the treemap
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', 
          '#17becf', '#aec7e8', '#ffbb78', '#98df8a', '#ff9896', '#c5b0d5', '#c49c94', '#f7b6d2', '#c7c7c7', 
          '#dbdb8d', '#9edae5', '#ffbb78', '#98df8a', '#ff9896', '#c5b0d5', '#c49c94']

# Create a figure and a set of subplots
plt.figure(figsize=(20, 12))

# Using squarify to plot the treemap
squarify.plot(sizes=df['Revenue (in billions)'], label=df['Field'], color=colors, alpha=0.8)

plt.title("Annual Revenue of Top Technology Companies (in billions)", fontsize=26, fontweight='bold', y=1.05)
plt.axis('off')  # Disable the axis

plt.show()