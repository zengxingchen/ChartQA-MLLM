
import matplotlib.pyplot as plt

# Data
day = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
steps = [3521, 4895, 4232, 5123, 4731, 5612, 4928, 4450, 5341, 4822, 4990, 5233, 4410, 4625, 5400, 4100, 4890, 5300, 4725, 4950, 4500, 4680, 5150, 5200, 4700, 4450, 4600, 4850, 4900, 4750, 5000]
burned_calories = [150, 200, 180, 220, 205, 240, 210, 190, 225, 205, 215, 230, 185, 195, 235, 175, 210, 225, 205, 215, 190, 200, 230, 230, 205, 195, 200, 210, 215, 205, 220]

plt.figure(figsize=(16, 12))
plt.scatter(steps, burned_calories, color='#FF5733')
plt.xlabel('Daily Steps')
plt.ylabel('Burned Calories')
plt.title('Correlation between Daily Steps and Burned Calories', fontsize=14, pad=20)
plt.show()