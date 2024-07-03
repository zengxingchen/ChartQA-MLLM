
import matplotlib.pyplot as plt

# Define the data
companies = [
    "Apple", "Microsoft", "Amazon", "Google", "Berkshire Hathaway", "Facebook", "Tesla",
    "Alibaba", "Tencent", "Johnson & Johnson", "Procter & Gamble", "JPMorgan Chase", "Nestle", 
    "Visa", "Roche", "Mastercard", "ExxonMobil", "Chevron", "Walmart", "Samsung"
]
market_cap = [2600, 2500, 1700, 1600, 700, 600, 800, 700, 500, 450, 350, 450, 300, 350, 300, 300, 350, 300, 400, 450] # in billion dollars
bubble_size = [150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 50, 40, 40, 30, 30, 20, 20, 20, 10]
colors = [
    "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2", 
    "#7f7f7f", "#bcbd22", "#17becf", "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", 
    "#9467bd", "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"
]

# Create the plot
plt.figure(figsize=(16, 10))

for i in range(len(companies)):
    plt.scatter(market_cap[i], bubble_size[i], s=bubble_size[i]*10, c=colors[i], alpha=0.6, edgecolors="w", linewidth=2)

# Customizations
plt.title('Market Capitalization of Major Companies', pad=20)
plt.xlabel('Market Cap in Billion Dollars')
plt.ylabel('Bubble Size Indicator')
plt.grid(True)

# Add a legend for company colors
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=colors[i], label=companies[i]) for i in range(len(companies))]
plt.legend(handles=legend_elements, title="Companies", bbox_to_anchor=(1.05, 1), loc='upper left')

plt.show()