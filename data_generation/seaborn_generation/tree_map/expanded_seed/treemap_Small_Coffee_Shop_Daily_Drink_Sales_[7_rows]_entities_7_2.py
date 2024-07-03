
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Provided table data
table_data = [
    {'Date': '2023-04-01', 'Espresso': 50, 'Americano': 45, 'Cappuccino': 60, 'Latte': 40, 'Mocha': 55, 'Frappe': 30},
    {'Date': '2023-04-02', 'Espresso': 55, 'Americano': 50, 'Cappuccino': 55, 'Latte': 35, 'Mocha': 60, 'Frappe': 25},
    {'Date': '2023-04-03', 'Espresso': 45, 'Americano': 35, 'Cappuccino': 65, 'Latte': 50, 'Mocha': 40, 'Frappe': 20},
    {'Date': '2023-04-04', 'Espresso': 60, 'Americano': 55, 'Cappuccino': 70, 'Latte': 45, 'Mocha': 65, 'Frappe': 35},
    {'Date': '2023-04-05', 'Espresso': 50, 'Americano': 45, 'Cappuccino': 55, 'Latte': 40, 'Mocha': 50, 'Frappe': 30},
    {'Date': '2023-04-06', 'Espresso': 65, 'Americano': 60, 'Cappuccino': 75, 'Latte': 50, 'Mocha': 55, 'Frappe': 40},
    {'Date': '2023-04-07', 'Espresso': 55, 'Americano': 50, 'Cappuccino': 80, 'Latte': 60, 'Mocha': 65, 'Frappe': 45}
]

# Convert to pandas DataFrame
df = pd.DataFrame(table_data)

# Melt DataFrame to long format for use with squarify
df_long = pd.melt(df, id_vars='Date', var_name='Coffee_Type', value_name='Sales')

# Aggregate sales data to obtain total sales for each coffee type
total_sales = df_long.groupby('Coffee_Type').Sales.sum().reset_index()

# Create sizes for squarify
sizes = total_sales['Sales'].values

# Create a color list (feel free to customize this)
colors = [plt.cm.Spectral(i/float(len(sizes))) for i in range(len(sizes))]

# Create a treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=sizes, label=total_sales['Coffee_Type'], color=colors, alpha=0.8)
plt.title('Coffee Sales Treemap')
plt.axis('off')
plt.show()