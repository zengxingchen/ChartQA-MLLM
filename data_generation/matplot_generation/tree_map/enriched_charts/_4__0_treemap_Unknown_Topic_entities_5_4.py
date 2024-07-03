
import matplotlib.pyplot as plt
import squarify

# Data
categories = ['Graphene Applications', 'Quantum Computing', 'Robotic Automation', 'Augmented Reality', 
              'Biotechnology', 'Renewable Energy', 'Space Exploration', 'Cyber Security', 
              'AI in Healthcare', 'Smart Wearables', 'Electric Vehicles', 'E-education']
revenue = [210000, 165000, 135000, 115000, 95000, 75000, 55000, 43000, 32000, 29000, 
           25000, 20000]

# Colors
colors = ['#264653', '#2A9D8F', '#E9C46A', '#F4A261', '#E76F51', '#D62828', '#C71585', '#00B4D8', '#0077B6', 
          '#023E8A', '#03045E', '#48CAE4']

plt.figure(figsize=(12, 6))

# Treemap
squarify.plot(sizes=revenue, label=categories, color=colors, alpha=0.8, text_kwargs={'fontsize':8, 'weight':'bold'})

plt.title('Future Technologies & Society - Revenue Forecast', fontsize=20, pad=20)

# Removing axes
plt.axis('off')

# Display the plot
plt.show()