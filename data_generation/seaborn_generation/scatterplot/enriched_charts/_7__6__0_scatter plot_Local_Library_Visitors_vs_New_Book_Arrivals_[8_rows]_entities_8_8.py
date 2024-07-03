
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Generate the data
data = {
    'Fruit': [
        'Apple', 'Banana', 'Orange', 'Strawberry', 'Grapes', 'Pineapple', 'Mango', 
        'Blueberry', 'Peach', 'Plum', 'Watermelon', 'Pear', 'Cherry', 'Lemon', 
        'Kiwi', 'Pomegranate', 'Coconut', 'Papaya', 'Lychee', 'Avocado'
    ],
    'Price': [
        1.20, 0.50, 0.80, 1.50, 2.00, 1.75, 1.60, 2.50, 1.10, 1.30, 3.00, 
        1.25, 2.75, 0.90, 1.40, 2.20, 2.10, 1.90, 2.30, 1.70
    ]
}

# Create a Pandas DataFrame
df = pd.DataFrame(data)

# Define a color palette
palette = {
    1.20: "#1f77b4",
    0.50: "#ff7f0e",
    0.80: "#2ca02c",
    1.50: "#d62728",
    2.00: "#9467bd",
    1.75: "#8c564b",
    1.60: "#e377c2",
    2.50: "#7f7f7f",
    1.10: "#bcbd22",
    1.30: "#17becf",
    3.00: "#1f77b4",
    1.25: "#ff7f0e",
    2.75: "#2ca02c",
    0.90: "#d62728",
    1.40: "#9467bd",
    2.20: "#8c564b",
    2.10: "#e377c2",
    1.90: "#7f7f7f",
    2.30: "#bcbd22",
    1.70: "#17becf",
}

# Create a scatter plot
plt.figure(figsize=(14, 10))
sns.scatterplot(x='Fruit', y='Price', data=df, palette=palette, hue='Price', s=150, edgecolor='#333333', linewidth=1.2)

# Title and labels
plt.title('Price Variation of Different Fruits', fontsize=20, pad=20)
plt.xlabel('Fruit', fontsize=14)
plt.ylabel('Price (USD)', fontsize=14)

# Show plot
plt.legend(title='Price (USD)', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()