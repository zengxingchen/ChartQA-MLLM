
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data preparation
data = {
    'Category': ['Transportation', 'Food and Dining', 'Utilities', 'Entertainment', 
                 'Healthcare', 'Education', 'Apparel', 'Savings', 'Miscellaneous'],
    'Value': [25, 40, 30, 15, 20, 10, 5, 35, 20]
}
df = pd.DataFrame(data)

# Colors
colors = ['#6e5773', '#d45d79', '#ea9085', '#e3de8f', '#55b3b1', '#917db2', '#e06377', '#8ece7c', '#f9c74f']

# Plot configuration
plt.figure(figsize=(12, 8))
plt.pie(df['Value'], labels=df['Category'], colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Title and other configurations
plt.title('Personal Monthly Expenditure Breakdown')

plt.show()