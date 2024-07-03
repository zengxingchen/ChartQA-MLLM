
import matplotlib.pyplot as plt

# Given data
data = [
    {'Beverage': 'Espresso', ' Price (USD)': 2.75},
    {'Beverage': 'Americano', ' Price (USD)': 3.0},
    {'Beverage': 'Latte', ' Price (USD)': 3.95},
    {'Beverage': 'Cappuccino', ' Price (USD)': 3.85},
    {'Beverage': 'Mocha', ' Price (USD)': 4.1},
    {'Beverage': 'Flat White', ' Price (USD)': 3.65},
    {'Beverage': 'Cortado', ' Price (USD)': 3.1},
    {'Beverage': 'Cold Brew', ' Price (USD)': 3.5},
    {'Beverage': 'Frappuccino', ' Price (USD)': 4.45},
    {'Beverage': 'Macchiato', ' Price (USD)': 3.25},
    {'Beverage': 'Espresso', ' Price (USD)': 2.8},
    {'Beverage': 'Americano', ' Price (USD)': 3.05},
    {'Beverage': 'Latte', ' Price (USD)': 3.9},
    {'Beverage': 'Cappuccino', ' Price (USD)': 3.8},
    {'Beverage': 'Mocha', ' Price (USD)': 4.15}
]

# Extract the prices from the data
prices = [item[' Price (USD)'] for item in data]

# Create a histogram
plt.figure(figsize=(10, 6))  # Set the size of the histogram

# Create bins for the histogram
bin_width = 0.1  # Determine the width of each bin
price_range = max(prices) - min(prices)
bins = int(price_range / bin_width)  # Number of bins
plt.hist(prices, bins=bins, color='skyblue', edgecolor='black')

# Add diversified visual encodings
plt.title('Histogram of Beverage Prices', fontsize=16)
plt.xlabel('Price (USD)', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.grid(True, linestyle='--', linewidth=0.5, color='gray', alpha=0.7)  # Add grid with semi-transparent dashed lines

# Enhance x-axis with ticks for every beverage price
plt.xticks([round(min(prices) + bin_width * i, 2) for i in range(bins + 1)], rotation=45)

# Add a mean price line
mean_price = sum(prices) / len(prices)
plt.axvline(mean_price, color='red', linestyle='dashed', linewidth=1, label=f'Mean Price: {mean_price:.2f} USD')

plt.legend()  # Show legend

# Show the plot
plt.tight_layout()  # Ensure everything fits without overlapping
plt.show()