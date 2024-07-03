
import matplotlib.pyplot as plt

manufacturers = ['Gucci', 'Chanel', 'Louis Vuitton', 'Prada', 'Hermes', 'Dior', 'Versace', 'Fendi', 'Burberry', 'Ralph Lauren', 'Dolce & Gabbana', 'Givenchy', 'Balenciaga', 'Valentino', 'Tom Ford', 'Yves Saint Laurent', 'Armani', 'Marc Jacobs', 'Bottega Veneta', 'Alexander McQueen']
market_shares = [4.5, 6.2, 7.8, 3.4, 5.6, 8.1, 2.9, 3.1, 4.0, 4.8, 3.7, 2.5, 1.9, 2.3, 3.0, 6.0, 4.1, 2.7, 1.8, 2.6]
units_sold = [45, 70, 90, 35, 60, 100, 30, 40, 50, 55, 38, 28, 20, 25, 32, 65, 48, 22, 18, 27]
average_prices = [1500, 1700, 1800, 1400, 1600, 1750, 1200, 1300, 1450, 1350, 1250, 1150, 1100, 1050, 1500, 1550, 1400, 1180, 1300, 1270]

fig, ax = plt.subplots(figsize=(14, 10))

sizes = [units * 5 for units in units_sold]

colors = ['#FF6347', '#FFD700', '#ADFF2F', '#00BFFF', '#8A2BE2', '#FF1493', '#00CED1', '#FF4500', '#DA70D6', '#7FFF00', '#FF00FF', '#6495ED', '#FF8C00', '#4B0082', '#BA55D3', '#FF69B4', '#4682B4', '#D2691E', '#8B0000', '#00FF7F']

for (manufacturer, share, units, price, size, color) in zip(manufacturers, market_shares, units_sold, average_prices, sizes, colors):
    ax.scatter(share, price, s=size, label=manufacturer, alpha=0.6, edgecolors='w', color=color)

plt.title('Market Share and Average Price of Luxury Fashion Brands', pad=20)
plt.xlabel('Market Share (%)')
plt.ylabel('Average Price ($)')

handles, labels = ax.get_legend_handles_labels()
hl = sorted(zip(handles, labels), key=lambda x: x[1])
handles2, labels2 = zip(*hl)
ax.legend(handles2, labels2, loc="upper left", title="Brands")

plt.show()