
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
flights = [800, 850, 900, 750, 820, 880, 900, 850, 830, 870, 920, 950]
accommodations = [500, 550, 520, 530, 510, 540, 600, 570, 560, 580, 590, 610]
food = [300, 310, 320, 340, 330, 350, 360, 370, 380, 390, 400, 410]
entertainment = [150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260]
transport = [100, 120, 130, 140, 110, 150, 160, 170, 180, 190, 200, 210]

# Stacked Bar Chart
fig, ax = plt.subplots(figsize=(12, 8))  # changing width and height of the chart

bar_width = 0.6  # change width of bars
index = range(len(months))

p1 = plt.bar(index, flights, bar_width, label='Flights', color='#FF5733')
p2 = plt.bar(index, accommodations, bar_width, bottom=flights, label='Accommodations', color='#33FF57')
p3 = plt.bar(index, food, bar_width, bottom=[f + a for f, a in zip(flights, accommodations)], label='Food', color='#3357FF')
p4 = plt.bar(index, entertainment, bar_width, bottom=[f + a + fo for f, a, fo in zip(flights, accommodations, food)], label='Entertainment', color='#FF33A5')
p5 = plt.bar(index, transport, bar_width, bottom=[f + a + fo + e for f, a, fo, e in zip(flights, accommodations, food, entertainment)], label='Transport', color='#33A5FF')

plt.ylabel('Expenses in USD')
plt.xticks(index, months)
plt.title('Monthly Travel Expenses')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), shadow=True, ncol=3)

# Customizing the grid
plt.grid(axis='y')

plt.show()