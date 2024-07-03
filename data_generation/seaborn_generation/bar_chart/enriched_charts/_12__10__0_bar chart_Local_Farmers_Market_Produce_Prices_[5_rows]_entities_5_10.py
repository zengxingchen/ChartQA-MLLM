
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Given dataset
data = {
    'Category': ['Shirts', 'Jeans', 'Dresses', 'Shoes', 'Accessories', 'Jackets', 'Hats', 'Scarves', 'Bags', 'Belts'],
    'Sales': [150, 200, 180, 220, 130, 170, 90, 110, 160, 140]
}

# Create DataFrame
df = pd.DataFrame(data)

# Initialize a Matplotlib figure and set its size
plt.figure(figsize=(10, 8))

# Create horizontal bar chart
sns.barplot(
    x='Sales',
    y='Category',
    data=df,
    palette=[
        '#5DA5DA', '#FAA43A', '#60BD68', '#F17CB0', '#B2912F',
        '#B276B2', '#DECF3F', '#F15854', '#4D4D4D', '#8C564B'
    ],
    dodge=False
)

# Customize the chart
plt.title('Fashion Category Sales', pad=20)
plt.xlabel('Sales')
plt.ylabel('Category')

# Adjust the height of the bars
for patch in plt.gca().patches:
    patch.set_height(0.5)

# Show the plot
plt.show()