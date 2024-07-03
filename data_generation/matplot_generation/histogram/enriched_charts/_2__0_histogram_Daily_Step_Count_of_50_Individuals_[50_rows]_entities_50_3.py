
import matplotlib.pyplot as plt

sales = [
    100, 102, 105, 107, 110, 112, 115, 118, 120, 123, 125, 128, 130, 133, 135, 138, 140, 143, 145, 148,
    150, 153, 155, 158, 160, 163, 165, 168, 170, 173, 175, 178, 180, 183, 185, 188, 190, 193, 195, 198,
    200, 203, 205, 208, 210, 213, 215, 218, 220, 223, 225, 228, 230, 233, 235, 238, 240, 243, 245, 248,
    250, 253, 255, 258, 260, 263, 265, 268, 270, 273, 275, 278, 280, 283, 285, 288, 290, 293, 295, 298,
    300
]

plt.figure(figsize=(12, 8))
plt.hist(sales, bins=15, orientation='vertical', color='#1abc9c', edgecolor='#2c3e50', linewidth=1.5)

plt.title('Monthly Sales Distribution in ABC Company')
plt.xlabel('Sales (in thousands)')
plt.ylabel('Number of Months')

plt.show()