
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Data for treemap
data = {
    'Category': [
        'Market Analysis', 'Financial Planning', 'Product Development', 
        'Brand Management', 'Customer Service', 'Sales Strategies', 
        'Innovation & Creativity', 'Leadership Skills', 'Digital Marketing', 
        'Supply Chain Management', 'Business Ethics', 'Entrepreneurial Mindset', 
        'Risk Management', 'Corporate Social Responsibility', 'E-commerce Trends', 
        'Business Analytics', 'Negotiation Techniques', 'Investment Strategies', 
        'Startup Ecosystems', 'Global Business Trends'
    ],
    'Values': [
        200, 180, 220, 160, 170, 210, 190, 200, 230, 175, 195, 205, 185, 
        215, 225, 190, 180, 195, 205, 210
    ]
}

# Convert the data into DataFrame
df = pd.DataFrame(data)

# Define color palette
colors = [
    '#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1',
    '#955251', '#B565A7', '#009B77', '#DD4124', '#45B8AC',
    '#EFC050', '#5B5EA6', '#9B2335', '#BC243C', '#C3447A',
    '#98B4D4', '#C94C4C', '#034F84', '#E57373', '#FFC107'
]

# Create figure and axes for Matplotlib
fig, ax = plt.subplots(1, figsize=(18, 14))

# Create a treemap
squarify.plot(sizes=df['Values'], label=df['Category'], alpha=0.8, color=colors)

# Remove the axes
plt.axis('off')

# Add a title
plt.title('Business & Entrepreneurship Topics and Their Importance', fontsize=22, y=1.05)

# Show the plot
plt.show()