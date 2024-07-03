
import matplotlib.pyplot as plt
import squarify

# Data
categories = ['Science & Nature', 'Health & Psychology', 'Business & Entrepreneurship', 
              'Fashion & Beauty', 'Astronomy & Space Exploration', 'Music & Performing Arts', 
              'Future Technologies & Society', 'Entertainment & Leisure', 'Travel & Adventure', 
              'Environment & Climate Change', 'Sports & Fitness', 'Culture & Society', 
              'Politics & Governance', 'Art & Design', 'Food & Nutrition', 'Education & Learning', 
              'Philosophy & Ethics', 'Literature & Writing', 'Economics & Finance', 
              'History & Archaeology']
revenue = [10000, 9000, 12000, 7000, 5000, 4000, 11000, 6000, 8000, 3000, 8500, 2000, 
           1500, 9500, 6500, 2500, 1400, 5500, 4500, 3500]

# Colors
colors = ['#1F78B4', '#33A02C', '#FB9A99', '#E31A1C', '#FF7F00', '#6A3D9A', '#B2DF8A', 
          '#FDBF6F', '#CAB2D6', '#FFFF99', '#A6CEE3', '#B15928', '#CCCCFF', '#B0E0E6', 
          '#FFD700', '#FFA07A', '#20B2AA', '#8470FF', '#DDA0DD', '#8FBC8F']

plt.figure(figsize=(18, 10))

# Treemap
squarify.plot(sizes=revenue, label=categories, color=colors, alpha=0.8)

plt.title('Insights into Different Strategic Domains', fontsize=20, pad=20)

# Removing axes
plt.axis('off')

# Display the plot
plt.show()