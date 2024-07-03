
import matplotlib.pyplot as plt

# Data
days = list(range(1, 93))
values = [
    100, 98, 97, 95, 94, 93, 91, 90, 88, 87, 85, 84, 82, 81, 79, 78, 76, 75, 73, 72,
    71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52,
    51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32,
    31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12,
    11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0
]

# Plotting
plt.figure(figsize=(12, 6))  # Change width and height

plt.plot(days, values, color='#ff5733')  # Using a specific color code

plt.title('Daily Productivity Index', loc='left')  # Change the topic and headline
plt.xlabel('Day of the Quarter')
plt.ylabel('Productivity Index')

# Annotation
plt.annotate('Steep Decline', xy=(75, values[74]), xytext=(50, values[49] + 5),
             arrowprops=dict(facecolor='#2ca02c', shrink=0.05))

plt.tight_layout()
plt.show()