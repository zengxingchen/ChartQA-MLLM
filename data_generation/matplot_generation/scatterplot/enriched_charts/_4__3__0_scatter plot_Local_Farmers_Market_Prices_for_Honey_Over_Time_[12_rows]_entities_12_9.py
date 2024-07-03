
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
calories_burned = [2300, 2200, 2100, 2400, 2350, 2250, 2450, 2550, 2600, 2700, 
                   2750, 2800, 2850, 2900, 2950, 3000, 3100, 3200, 3300, 3400, 
                   3450, 3500, 3550, 3600, 3650, 3700, 3750, 3800, 3850, 3900]
exercise_minutes = [45, 50, 40, 55, 50, 48, 53, 60, 62, 65, 66, 68, 70, 72, 73, 
                    75, 78, 80, 82, 85, 88, 90, 92, 93, 95, 97, 98, 100, 102, 105]

plt.figure(figsize=(12, 8))
plt.scatter(calories_burned, exercise_minutes, color='#FF5733')

plt.xlabel('Calories Burned')
plt.ylabel('Exercise Minutes')
plt.title('Daily Exercise: Calories Burned vs Exercise Minutes')

plt.show()