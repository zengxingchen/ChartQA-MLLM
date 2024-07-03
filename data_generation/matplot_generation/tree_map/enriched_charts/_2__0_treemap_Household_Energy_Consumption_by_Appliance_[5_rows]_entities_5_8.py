
import matplotlib.pyplot as plt
import squarify

# Data
sector = ['Technology', 'Healthcare', 'Finance', 'Consumer Goods', 'Energy', 'Industrials', 'Utilities', 'Real Estate', 'Telecommunications', 'Materials']
market_share = [25.3, 17.9, 14.5, 10.1, 8.4, 7.3, 6.2, 5.7, 4.6, 3.0]
color_code = ['#4F81BD', '#C0504D', '#9BBB59', '#8064A2', '#4BACC6', '#F79646', '#92D050', '#E36C09', '#31859B', '#82A3B6']

# Plot
plt.figure(figsize=(14, 10))
squarify.plot(sizes=market_share, label=sector, color=color_code, alpha=0.8)
plt.title('Market Share of Different Economic Sectors in 2022', fontsize=20, y=1.05)
plt.axis('off')
plt.show()