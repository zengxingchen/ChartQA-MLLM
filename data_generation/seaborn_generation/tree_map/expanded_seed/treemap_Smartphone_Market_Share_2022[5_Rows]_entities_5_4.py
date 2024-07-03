
import matplotlib.pyplot as plt
import squarify    # you may need to install it using pip

# Data
table_data = [
    {'Brand': 'Samsung', 'Market Share (%)': 20.5},
    {'Brand': 'Apple', 'Market Share (%)': 17.2},
    {'Brand': 'Xiaomi', 'Market Share (%)': 11.7},
    {'Brand': 'OPPO', 'Market Share (%)': 8.4},
    {'Brand': 'Vivo', 'Market Share (%)': 8.1}
]

# Extracting the brand names and their corresponding market shares
brands = [entry['Brand'] for entry in table_data]
market_shares = [entry['Market Share (%)'] for entry in table_data]

# Colors for each section
colors = [plt.cm.Spectral(i/float(len(market_shares))) for i in range(len(market_shares))]

# Using squarify to plot the treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=market_shares, label=brands, color=colors, alpha=0.6)

# Customizing the plot
plt.title('Market Share by Brand', fontsize=18)
plt.axis('off')  # Disable the axis lines and labels

# Display the plot
plt.show()