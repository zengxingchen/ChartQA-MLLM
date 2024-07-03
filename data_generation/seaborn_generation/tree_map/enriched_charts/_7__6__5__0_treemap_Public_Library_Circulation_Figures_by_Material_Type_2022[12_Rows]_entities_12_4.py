
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data for the treemap
data = {
    'Category': ['Fashion', 'Beauty', 'Jewelry', 'Footwear', 'Apparel', 'Accessories', 
                 'Cosmetics', 'Skincare', 'Hairstyles', 'Trends', 'Makeup', 'Perfumes', 
                 'Luxury Brands', 'Ethnic Wear', 'Streetwear', 'Vintage Fashion'],
    'Interest': [800, 600, 550, 500, 450, 400, 350, 300, 250, 200, 150, 100, 80, 60, 40, 20],
    'Percentage': [0.20, 0.15, 0.1375, 0.125, 0.1125, 0.10, 0.0875, 0.075, 0.0625, 0.05, 
                   0.0375, 0.025, 0.02, 0.015, 0.01, 0.005]
}

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Define color list
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#CC99FF', '#FF9966', 
          '#FF66B2', '#6699FF', '#FFB266', '#66FFB2', '#CC66FF', '#B2FF66', 
          '#FF6699', '#66CCFF', '#FF66CC', '#99FF66']

# Plot the Treemap
plt.figure(figsize=(18, 14))
squarify.plot(sizes=df['Percentage'], label=df['Category'], color=colors, alpha=0.8)
plt.title('Interest in Various Fashion & Beauty Categories among Enthusiasts', fontsize=22, pad=30)
plt.axis('off')
plt.show()