
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Category': ['Electronics', 'Clothing', 'Home Appliances', 'Books', 'Toys', 'Groceries', 'Furniture', 'Beauty Products', 'Sports Equipment', 'Stationery'],
    'Sales': [1500, 2300, 1800, 1200, 1700, 2500, 1600, 1900, 2200, 1300]
}

df = pd.DataFrame(data)

plt.figure(figsize=(10, 8))

sns.barplot(
    y='Category',
    x='Sales',
    data=df,
    palette=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'],
    dodge=False
)

plt.title('Sales by Category')
plt.xlabel('Sales')
plt.ylabel('Category')

for patch in plt.gca().patches:
    patch.set_height(0.6)

plt.show()