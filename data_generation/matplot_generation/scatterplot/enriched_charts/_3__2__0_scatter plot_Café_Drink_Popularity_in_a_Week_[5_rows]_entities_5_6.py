
import matplotlib.pyplot as plt

days = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30
]
practice_hours = [
    2, 2.5, 3, 1.5, 2.8, 3.2, 2.1, 3.4, 2.6, 3.1,
    2.9, 3.5, 1.8, 2.7, 3.6, 1.9, 2.4, 3.3, 2.2, 3.0,
    1.7, 2.5, 3.7, 2.0, 2.8, 3.4, 2.1, 3.2, 2.9, 3.5
]
pieces_learned = [
    1, 1, 2, 1, 2, 3, 1, 2, 2, 3,
    2, 3, 1, 2, 3, 1, 2, 3, 2, 3,
    1, 2, 4, 2, 3, 3, 1, 3, 2, 3
]
difficulty = [
    50, 60, 70, 40, 55, 65, 45, 75, 50, 70,
    60, 80, 40, 55, 75, 45, 50, 70, 60, 80,
    35, 50, 85, 55, 65, 75, 40, 70, 60, 80
]

difficulty_colors = [
    '#FF5733', '#FFBD33', '#FF33FF', '#33FF57', '#33FFBD', '#337BFF', '#5733FF', '#BD33FF', '#BD5733', '#5733BD',
    '#33BDFF', '#33FFD2', '#BDFF33', '#FFD233', '#FF337B', '#D2FF33', '#BDFF57', '#5733D2', '#33FFD2', '#FFD233',
    '#5733FF', '#33BDFF', '#FF337B', '#33FFBD', '#337BFF', '#33FFD2', '#FF33FF', '#FFBD33', '#BD33FF', '#5733BD'
]

fig, ax = plt.subplots(figsize=(14, 10))
sc = ax.scatter(days, practice_hours, s=[d for d in difficulty], c=difficulty_colors, alpha=0.75)

ax.set_xlabel('Day of the Month')
ax.set_ylabel('Practice Hours')
ax.set_title('Daily Music Practice and Pieces Learned', pad=20)
ax.grid(True)

plt.show()