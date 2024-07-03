
import matplotlib.pyplot as plt

# Provided data
data = [
    {'Week': 'Week 1', 'Price of Milk (1 gallon)': '$3.29', 'Price of Bread (1 loaf)': '$2.49', 'Price of Rice (1 lb)': '$1.20'},
    {'Week': 'Week 2', 'Price of Milk (1 gallon)': '$3.35', 'Price of Bread (1 loaf)': '$2.45', 'Price of Rice (1 lb)': '$1.22'},
    {'Week': 'Week 3', 'Price of Milk (1 gallon)': '$3.40', 'Price of Bread (1 loaf)': '$2.50', 'Price of Rice (1 lb)': '$1.25'},
    {'Week': 'Week 4', 'Price of Milk (1 gallon)': '$3.46', 'Price of Bread (1 loaf)': '$2.55', 'Price of Rice (1 lb)': '$1.30'},
    {'Week': 'Week 5', 'Price of Milk (1 gallon)': '$3.50', 'Price of Bread (1 loaf)': '$2.65', 'Price of Rice (1 lb)': '$1.33'},
    {'Week': 'Week 6', 'Price of Milk (1 gallon)': '$3.55', 'Price of Bread (1 loaf)': '$2.70', 'Price of Rice (1 lb)': '$1.35'},
    {'Week': 'Week 7', 'Price of Milk (1 gallon)': '$3.58', 'Price of Bread (1 loaf)': '$2.75', 'Price of Rice (1 lb)': '$1.37'},
    {'Week': 'Week 8', 'Price of Milk (1 gallon)': '$3.60', 'Price of Bread (1 loaf)': '$2.80', 'Price of Rice (1 lb)': '$1.40'},
    {'Week': 'Week 9', 'Price of Milk (1 gallon)': '$3.65', 'Price of Bread (1 loaf)': '$2.85', 'Price of Rice (1 lb)': '$1.43'},
    {'Week': 'Week 10', 'Price of Milk (1 gallon)': '$3.70', 'Price of Bread (1 loaf)': '$2.90', 'Price of Rice (1 lb)': '$1.45'},
    {'Week': 'Week 11', 'Price of Milk (1 gallon)': '$3.75', 'Price of Bread (1 loaf)': '$2.95', 'Price of Rice (1 lb)': '$1.50'},
    {'Week': 'Week 12', 'Price of Milk (1 gallon)': '$3.80', 'Price of Bread (1 loaf)': '$3.00', 'Price of Rice (1 lb)': '$1.55'}
]

# Extracting individual lists for plot
weeks = [d['Week'] for d in data]
milk_prices = [float(d['Price of Milk (1 gallon)'].strip('$')) for d in data]
bread_prices = [float(d['Price of Bread (1 loaf)'].strip('$')) for d in data]
rice_prices = [float(d['Price of Rice (1 lb)'].strip('$')) for d in data]

# Plotting
plt.figure(figsize=(12, 6))

# Line for Milks
plt.plot(weeks, milk_prices, label='Milk (per gallon)', marker='o', linestyle='-', color='blue')

# Line for Breads
plt.plot(weeks, bread_prices, label='Bread (per loaf)', marker='s', linestyle='--', color='green')

# Line for Rices
plt.plot(weeks, rice_prices, label='Rice (per lb)', marker='^', linestyle='-.', color='red')

# Customizing the plot
plt.title('Weekly Price Changes of Milk, Bread and Rice')
plt.xlabel('Weeks')
plt.ylabel('Price in USD')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)

# Show plot
plt.tight_layout()
plt.show()