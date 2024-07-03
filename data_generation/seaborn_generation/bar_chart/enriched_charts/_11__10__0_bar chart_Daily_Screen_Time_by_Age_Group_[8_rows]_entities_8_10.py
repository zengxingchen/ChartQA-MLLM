
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Category': ['Clothing', 'Electronics', 'Books', 'Groceries', 'Furniture', 'Toys', 'Cosmetics'],
    'AmountSpent': [300, 450, 200, 600, 350, 150, 250]
}
df = pd.DataFrame(data)

colors = ['#ff6347', '#4682b4', '#6a5acd', '#ffd700', '#40e0d0', '#ff69b4', '#dda0dd']

f, ax = plt.subplots(figsize=(10, 6))

sns.barplot(y='Category', x='AmountSpent', data=df, palette=colors)

for container in ax.containers:
    plt.setp(container, height=0.6)

plt.title('Average Monthly Spending on Various Categories', pad=20)
plt.xlabel('Amount Spent (USD)')
plt.ylabel('Category')

plt.show()