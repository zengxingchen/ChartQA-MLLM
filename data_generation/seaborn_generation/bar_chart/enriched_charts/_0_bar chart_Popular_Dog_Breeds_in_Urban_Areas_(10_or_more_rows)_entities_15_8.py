
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Given dataset in a dictionary
data = {
    'Store': ['Store A', 'Store B', 'Store C', 'Store D', 'Store E'],
    'Electronics': [15000, 20000, 18000, 22000, 14000],
    'Furniture': [9500, 18500, 16500, 17000, 13500],
    'Clothing': [12000, 24000, 15500, 17500, 11000],
    'Home Appliances': [13000, 21500, 14000, 19000, 12000],
    'Groceries': [16000, 27500, 23000, 28000, 15000]
}

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(data)

# Unpivot the DataFrame from wide to long format
df_long = pd.melt(df, id_vars='Store', var_name='Category', value_name='Sales')

# Create a horizontal bar plot
plt.figure(figsize=(14, 8))
sns.barplot(
    x='Sales', 
    y='Category', 
    hue='Store', 
    data=df_long,
    palette=['#FF5733', '#33FF57', '#3357FF', '#FF33A7', '#FFC233'],
    dodge=True,
    edgecolor='.2',
    linewidth=.6,
    orient='h'
)

# Adjusting the bar width (by adjusting the distance between the bars)
plt.yticks(rotation=0)
plt.legend(title='Store')

# Set the title and the labels of the plot
plt.title('Sales Comparison Among Different Stores')
plt.xlabel('Total Sales')
plt.ylabel('Product Category')

# Show the plot
plt.show()