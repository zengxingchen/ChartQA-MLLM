
import matplotlib.pyplot as plt

# Given table data
data = [
    {'Week': 1, 'Price($)': 2.8},
    {'Week': 2, 'Price($)': 2.75},
    {'Week': 3, 'Price($)': 2.7},
    {'Week': 4, 'Price($)': 2.65},
    {'Week': 5, 'Price($)': 2.6},
    {'Week': 6, 'Price($)': 2.85},
    {'Week': 7, 'Price($)': 2.9},
    {'Week': 8, 'Price($)': 2.95},
    {'Week': 9, 'Price($)': 2.5},
    {'Week': 10, 'Price($)': 2.45},
    {'Week': 11, 'Price($)': 2.4},
    {'Week': 12, 'Price($)': 2.8},
    {'Week': 13, 'Price($)': 2.75},
    {'Week': 14, 'Price($)': 2.7},
    {'Week': 15, 'Price($)': 2.65}
]

# Extracting the prices
prices = [entry['Price($)'] for entry in data]

# Creating a histogram with diversified visual encoding
plt.figure(figsize=(10, 5))  # Setting the figure size

# Creating a histogram
n, bins, patches = plt.hist(prices, bins=len(set(prices)), color='skyblue', alpha=0.7)

# Highlighting the median price bin
median_price = sorted(prices)[len(prices) // 2]
median_bin = None
for bin_left, patch in zip(bins, patches):
    if bin_left <= median_price < (bin_left + (bins[1] - bins[0])):
        median_bin = patch
        break

if median_bin:
    median_bin.set_facecolor('salmon')
    median_bin.set_label('Median Price Bin')

# Adding a title and labels
plt.title('Distribution of Prices Over 15 Weeks')
plt.xlabel('Price ($)')
plt.ylabel('Frequency')

# Adding grid lines for better readability
plt.grid(axis='y', alpha=0.75)

# Adding a legend if median bin was highlighted
if median_bin:
    plt.legend()

# Displaying the plot
plt.show()