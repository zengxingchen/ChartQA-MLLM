
import matplotlib.pyplot as plt

# Data
days = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", 
        "Day 7", "Day 8", "Day 9", "Day 10", "Day 11", "Day 12", 
        "Day 13", "Day 14", "Day 15", "Day 16", "Day 17", "Day 18", 
        "Day 19", "Day 20", "Day 21", "Day 22", "Day 23", "Day 24", 
        "Day 25", "Day 26", "Day 27", "Day 28", "Day 29", "Day 30"]
stock_prices = [1000, 980, 960, 950, 940, 930, 920, 910, 905, 900, 
                890, 880, 875, 870, 860, 850, 840, 830, 820, 815, 
                810, 800, 790, 780, 770, 765, 760, 750, 740, 730]

plt.figure(figsize=(16, 8))
plt.plot(days, stock_prices, marker='o', color='#1f77b4', linewidth=2)

plt.annotate('Start of Decline', xy=(0, 1000), xytext=(2, 1050),
             arrowprops=dict(facecolor='#ff7f0e', shrink=0.05))
plt.annotate('Lowest Price', xy=(29, 730), xytext=(27, 720),
             arrowprops=dict(facecolor='#2ca02c', shrink=0.05))

plt.title('Daily Stock Prices Over a Month', pad=20)
plt.xlabel('Day')
plt.ylabel('Stock Price')
plt.grid(True)
plt.gca().invert_yaxis()

plt.show()