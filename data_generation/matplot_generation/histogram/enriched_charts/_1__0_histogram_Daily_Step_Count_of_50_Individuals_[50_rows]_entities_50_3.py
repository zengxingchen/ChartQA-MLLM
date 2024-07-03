
import matplotlib.pyplot as plt

scores = [
    72, 85, 90, 77, 66, 93, 88, 95, 81, 69, 84, 92, 89, 87, 73, 91, 75, 78, 94, 70,
    96, 86, 79, 80, 82, 83, 97, 76, 74, 71, 68, 67, 65, 64, 63, 62, 61, 60, 59, 58,
    57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38,
    37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18
]

plt.figure(figsize=(8, 6))

plt.hist(scores, bins=15, color='#8e44ad', edgecolor='#ffffff', linewidth=1.5)

plt.title('Student Scores Distribution')
plt.xlabel('Scores')
plt.ylabel('Number of Students')

plt.show()