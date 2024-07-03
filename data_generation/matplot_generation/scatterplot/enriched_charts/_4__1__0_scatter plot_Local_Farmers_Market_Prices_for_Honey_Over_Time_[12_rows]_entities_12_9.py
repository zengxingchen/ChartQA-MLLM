
import matplotlib.pyplot as plt

distance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
luminosity = [100, 150, 130, 170, 120, 140, 160, 135, 145, 155, 165, 175, 185, 195, 205, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360]

plt.figure(figsize=(16, 12))
plt.scatter(distance, luminosity, color='#FF5733')
plt.xlabel('Distance from Earth (Light Years)')
plt.ylabel('Star Luminosity (Relative Units)')
plt.title('Observations of Star Luminosity vs. Distance', pad=20)
plt.show()