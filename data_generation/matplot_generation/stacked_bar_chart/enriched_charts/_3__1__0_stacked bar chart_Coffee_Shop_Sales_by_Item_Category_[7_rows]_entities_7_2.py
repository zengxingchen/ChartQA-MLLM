
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
red_apples = [120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230]
green_apples = [100, 90, 110, 95, 120, 130, 140, 150, 160, 170, 180, 190]

# Plot setup
fig, ax = plt.subplots(figsize=(12, 8))

# Stacked bar chart (horizontal)
plt.barh(months, red_apples, color='#FF5733', edgecolor='white', height=0.6, label='Red Apples')
plt.barh(months, green_apples, left=red_apples, color='#28B463', edgecolor='white', height=0.6, label='Green Apples')

# Labels, title and legend
plt.xlabel('Number of Apples Sold')
plt.title('Monthly Sales of Red and Green Apples', pad=20)
plt.legend(loc='lower right')

# Numerical labels on bars
for i in range(len(months)):
    plt.text(red_apples[i] / 2, i, str(red_apples[i]), va='center', ha='center', color='white')
    plt.text(red_apples[i] + green_apples[i] / 2, i, str(green_apples[i]), va='center', ha='center', color='white')

# Show the plot
plt.show()