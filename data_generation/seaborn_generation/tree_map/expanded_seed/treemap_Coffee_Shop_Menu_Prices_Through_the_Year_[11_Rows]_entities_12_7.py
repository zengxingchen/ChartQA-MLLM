
import pandas as pd
import matplotlib.pyplot as plt
import squarify  # you might need to install with pip install squarify

# Your data
data = [
    {'Month': 'January', 'Americano Price': 2.5, 'Latte Price': 3.6, 'Espresso Price': 2.0, 'Cappuccino Price': 3.75},
    {'Month': 'February', 'Americano Price': 2.5, 'Latte Price': 3.6, 'Espresso Price': 2.0, 'Cappuccino Price': 3.75},
    # ... (other months)
    {'Month': 'December', 'Americano Price': 2.8, 'Latte Price': 4.0, 'Espresso Price': 2.4, 'Cappuccino Price': 4.15}
]

# Turn data into DataFrame
df = pd.DataFrame(data)

# Melt the dataframe to long format
df_long = df.melt(id_vars='Month', var_name='Coffee Type', value_name='Price')

# Calculate the size of each square
sizes = df_long['Price'].values

# Define color labels by coffee type
coffee_types = df_long['Coffee Type'].unique()
colors = plt.cm.viridis(np.linspace(0, 1, len(coffee_types)))
color_dict = dict(zip(coffee_types, colors))

# Define the labels for each rectangle
labels = ["{} \n {}\n ${:.2f}".format(row['Month'], row['Coffee Type'], row['Price']) for index, row in df_long.iterrows()]

# Create the treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=sizes, label=labels, color=[color_dict[coffee_type] for coffee_type in df_long['Coffee Type']], alpha=0.8)
plt.title('Coffee Price Distribution by Month and Type')

# Remove the axis for a cleaner look
plt.axis('off')

# Show the plot
plt.show()