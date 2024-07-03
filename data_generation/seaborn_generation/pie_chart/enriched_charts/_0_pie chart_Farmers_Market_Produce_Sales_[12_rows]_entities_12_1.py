
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data
data = {
    'Product': ['Laptops', 'Phones', 'Tablets', 'Headphones', 'Accessories', 'Cameras', 'Smartwatches', 'Speakers', 'Printers', 'Monitors'],
    'Sales': [320, 450, 180, 220, 95, 150, 85, 130, 60, 110]
}
df = pd.DataFrame(data)

# Define color palette
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

# Plot
plt.figure(figsize=(10, 8))
plt.pie(df['Sales'], labels=df['Product'], colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Sales Performance by Product')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()