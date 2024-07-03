
import matplotlib.pyplot as plt
import numpy as np

# Generated data points representing the exercise duration of a group of people
exercise_durations = np.array([5, 10, 10, 10, 10, 15, 15, 15, 15, 15, 15, 20, 20, 20, 20, 20, 25, 25, 25, 25, 25, 30, 30, 30, 30, 30, 35, 35, 35, 35, 35, 40, 40, 40, 40, 40, 45, 45, 45, 45, 45, 50, 50, 50, 50, 50, 55, 55, 55, 55, 55, 60, 60, 60, 60, 60, 65, 65, 65, 65, 65, 70, 70, 70, 70, 70, 75, 75, 75, 75, 75, 80, 80, 80, 80, 80, 85, 85, 85, 85, 85, 90, 90, 90, 90, 90, 95, 95, 95, 95, 95, 100, 100, 100, 100, 100, 105, 105, 105, 105, 105, 110, 110, 110, 110, 110, 115, 115, 115, 115, 115, 120, 120, 120, 120, 120])

plt.figure(figsize=(10, 6))
plt.hist(exercise_durations, bins=24, color='#3498DB', rwidth=0.9)

plt.title('Exercise Duration Distribution in a Group')
plt.ylabel('Number of Individuals')
plt.xlabel('Exercise Duration (minutes)')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()