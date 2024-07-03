
import matplotlib.pyplot as plt
import squarify

# Data points
companies = ['Apple', 'Samsung', 'Amazon', 'Alphabet', 'Microsoft', 'Huawei', 'Dell', 
             'Sony', 'Panasonic', 'HP', 'Lenovo', 'Intel', 'LG', 'Cisco', 'IBM', 
             'Tencent', 'Oracle', 'Xiaomi', 'Nvidia', 'Salesforce', 'Spotify', 'Snap']
revenue_in_billions = [274.5, 200.7, 386.1, 182.5, 143, 136.7, 94.4, 84.8, 68.9, 58.7, 
                       50.7, 77.9, 56.3, 49.3, 73.6, 70.9, 39.1, 37.6, 26.9, 21.3, 7.9, 2.5]
colors = ['#FF5733', '#33FF57', '#3357FF', '#57FF33', '#FF33A8', '#FF8333', 
          '#33FF83', '#5733FF', '#33FFF4', '#FF3381', '#FF5733', '#FF33C4', 
          '#FF5733', '#33FFB2', '#FF33EC', '#5733FF', '#33FFD5', '#FF3381', 
          '#FF5733', '#FF33B2', '#FF8333', '#FF3381']

# Plot Dimensions
plt.figure(figsize=(14, 10))

# Create a treemap
squarify.plot(sizes=revenue_in_billions, label=companies, color=colors, alpha=0.8)

# Title
plt.title('Annual Revenue of Top Tech Companies in Billions', fontsize=20, pad=20)

# Remove axes
plt.axis('off')

# Show plot
plt.show()