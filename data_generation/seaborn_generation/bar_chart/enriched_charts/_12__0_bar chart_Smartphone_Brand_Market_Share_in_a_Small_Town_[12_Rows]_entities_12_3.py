
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data: Annual Revenue of Tech Companies in 2023 (in billions USD)
data = {
    'Company': ['Apple', 'Microsoft', 'Alphabet', 'Amazon', 'Meta', 'Tesla', 
                'NVIDIA', 'Intel', 'IBM', 'Oracle', 'Adobe', 'Salesforce', 
                'Cisco', 'Qualcomm', 'PayPal'],
    'Annual_Revenue': [394, 198, 257, 514, 118, 81, 27, 79, 57, 50, 19, 26, 52, 44, 25]
}

# Create DataFrame
df = pd.DataFrame(data)

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(12, 10))

# Custom color palette
palette = ['#FF5733', '#33FF57', '#3357FF', '#F333FF', '#FF33F3', '#33FFF6', 
           '#5733FF', '#57FF33', '#F6FF33', '#FF3357', '#FFB833', '#33FFB8', 
           '#B833FF', '#FF8C33', '#33D1FF']

# Plot a vertical bar chart
sns.barplot(x='Company', y='Annual_Revenue', data=df, 
            palette=palette, ax=ax, dodge=False)

# Customize the Axes
ax.set(ylim=(0, 600), ylabel="Annual Revenue (Billions USD)", xlabel="Company")
ax.set_title('Annual Revenue of Tech Companies in 2023')

# Adjust bar width
for container in ax.containers:
    ax.bar_label(container, label_type='edge', padding=3)

# Rotate x-tick labels for better readability
plt.xticks(rotation=45, ha='right')

plt.show()