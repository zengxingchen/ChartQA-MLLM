
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
calories_burned = [400, 420, 390, 440, 415, 410, 430, 450, 420, 410, 455, 430, 415, 435, 460, 410, 450, 425, 440, 415, 430, 445, 460, 455, 420, 410, 435, 400, 450, 465, 430]
exercise_minutes = [30, 32, 28, 35, 33, 30, 34, 36, 32, 30, 37, 34, 33, 35, 38, 30, 36, 33, 35, 32, 34, 35, 37, 36, 32, 30, 34, 28, 36, 38, 34]

plt.figure(figsize=(16, 12))
plt.scatter(calories_burned, exercise_minutes, color='#FF5733')
plt.xlabel('Calories Burned')
plt.ylabel('Exercise Minutes')
plt.title('Calories Burned vs. Exercise Minutes in a Month')
plt.show()