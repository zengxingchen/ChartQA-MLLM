
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Create a DataFrame with the data
data = {
    'Category': ['Painting', 'Sculpture', 'Drawing', 'Architecture', 'Fashion Design', 'Graphic Design', 'Interior Design', 'Industrial Design', 'Photography', 'Film', 'Animation', 'Calligraphy', 'Textile Art', 'Ceramics', 'Printmaking', 'Jewelry Design', 'Landscape Design', 'Performing Arts', 'Literature', 'Music'],
    'Value': [80, 70, 75, 90, 85, 65, 55, 60, 50, 45, 95, 85, 70, 80, 75, 65, 60, 55, 85, 90],
    'Aspect': ['Art & Design'] * 20
}
df = pd.DataFrame(data)

# Plot parameters
plt.figure(figsize=(16, 12))
cmap = ['#4daf4a', '#377eb8', '#ff7f00', '#984ea3', '#e41a1c', 
        '#f781bf', '#a65628', '#999999', '#66c2a5', '#fc8d62',
        '#8da0cb', '#e78ac3', '#a6d854', '#ffd92f', '#e5c494',
        '#b3b3b3', '#8dd3c7', '#ffffb3', '#bebada', '#fb8072']

# Create a treemap
squarify.plot(sizes=df['Value'], label=df['Category'], color=cmap, alpha=0.8)

plt.title('Elements of Art & Design by Importance', fontsize=18)
plt.axis('off')

plt.show()