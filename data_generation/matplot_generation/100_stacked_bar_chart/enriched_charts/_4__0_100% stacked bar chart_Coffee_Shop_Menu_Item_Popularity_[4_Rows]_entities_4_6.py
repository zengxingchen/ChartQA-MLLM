
import matplotlib.pyplot as plt
import numpy as np

data = """
Day,Apple,Orange,Banana,Grapes
Monday,25,30,20,25
Tuesday,30,25,25,20
Wednesday,35,20,15,30
Thursday,40,20,20,20
Friday,30,25,30,15
Saturday,45,15,25,15
Sunday,50,10,20,20
"""

days, apple, orange, banana, grapes = [], [], [], [], []
for i, line in enumerate(data.strip().split('\n')):
    if i > 0:
        parts = line.split(',')
        days.append(parts[0])
        apple.append(int(parts[1]))
        orange.append(int(parts[2]))
        banana.append(int(parts[3]))
        grapes.append(int(parts[4]))

apple = np.array(apple)
orange = np.array(orange)
banana = np.array(banana)
grapes = np.array(grapes)

totals = apple + orange + banana + grapes
apple_percentage = apple / totals * 100
orange_percentage = orange / totals * 100
banana_percentage = banana / totals * 100
grapes_percentage = grapes / totals * 100

barWidth = 0.6
plt.figure(figsize=(12, 10))

plt.bar(days, apple_percentage, color='#8B0000', edgecolor='white', width=barWidth, label='Apple')
plt.bar(days, orange_percentage, bottom=apple_percentage, color='#FF8C00', edgecolor='white', width=barWidth, label='Orange')
plt.bar(days, banana_percentage, bottom=apple_percentage + orange_percentage, color='#FFD700', edgecolor='white', width=barWidth, label='Banana')
plt.bar(days, grapes_percentage, bottom=apple_percentage + orange_percentage + banana_percentage, color='#32CD32', edgecolor='white', width=barWidth, label='Grapes')

plt.ylabel('Percentage (%)', fontsize=15)
plt.xlabel('Day of the Week', fontsize=15)
plt.title('Fruit Consumption Over a Week (in %)', fontsize=18, pad=20)
plt.legend(loc='upper right')

plt.tight_layout()
plt.show()