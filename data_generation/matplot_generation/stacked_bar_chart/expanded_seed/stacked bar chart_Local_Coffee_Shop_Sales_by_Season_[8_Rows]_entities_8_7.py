
import matplotlib.pyplot as plt

# Provided data
data = [
    {'Season': 'Spring 2021', 'Espresso': 450, 'Latte': 520, 'Cappuccino': 390, 'Americano': 310, 'Mocha': 280},
    {'Season': 'Summer 2021', 'Espresso': 470, 'Latte': 500, 'Cappuccino': 320, 'Americano': 460, 'Mocha': 300},
    {'Season': 'Fall 2021', 'Espresso': 430, 'Latte': 540, 'Cappuccino': 410, 'Americano': 390, 'Mocha': 310},
    {'Season': 'Winter 2021', 'Espresso': 480, 'Latte': 600, 'Cappuccino': 450, 'Americano': 420, 'Mocha': 390},
    {'Season': 'Spring 2022', 'Espresso': 460, 'Latte': 530, 'Cappuccino': 400, 'Americano': 320, 'Mocha': 290},
    {'Season': 'Summer 2022', 'Espresso': 480, 'Latte': 490, 'Cappuccino': 330, 'Americano': 470, 'Mocha': 310},
    {'Season': 'Fall 2022', 'Espresso': 440, 'Latte': 550, 'Cappuccino': 420, 'Americano': 400, 'Mocha': 320},
    {'Season': 'Winter 2022', 'Espresso': 490, 'Latte': 610, 'Cappuccino': 460, 'Americano': 430, 'Mocha': 400}
]

# Extracting categories and seasons
seasons = [d['Season'] for d in data]
categories = list(data[0].keys())[1:]  # Ignore the first key 'Season'

# Preparing data for the stacked bar chart
espresso = [d['Espresso'] for d in data]
latte = [d['Latte'] for d in data]
cappuccino = [d['Cappuccino'] for d in data]
americano = [d['Americano'] for d in data]
mocha = [d['Mocha'] for d in data]

# The position of the bars on the x-axis
r = range(len(data))

# Plotting the bars
plt.figure(figsize=(10, 7))

barWidth = 0.85
plt.bar(r, espresso, color='brown', edgecolor='white', width=barWidth, label='Espresso')
plt.bar(r, latte, bottom=espresso, color='beige', edgecolor='white', width=barWidth, label='Latte')
plt.bar(r, cappuccino, bottom=[i+j for i,j in zip(espresso, latte)], color='darkorange', edgecolor='white', width=barWidth, label='Cappuccino')
plt.bar(r, americano, bottom=[i+j+k for i,j,k in zip(espresso, latte, cappuccino)], color='grey', edgecolor='white', width=barWidth, label='Americano')
plt.bar(r, mocha, bottom=[i+j+k+l for i,j,k,l in zip(espresso, latte, cappuccino, americano)], color='black', edgecolor='white', width=barWidth, label='Mocha')

# Adding labels
plt.xlabel('Season', fontweight='bold')
plt.xticks(r, seasons, rotation=45, ha="right")
plt.ylabel('Sales', fontweight='bold')
plt.title('Coffee Sales by Season (2021-2022)', fontweight='bold')

# Create legend & Show graphic
plt.legend()
plt.tight_layout()
plt.show()