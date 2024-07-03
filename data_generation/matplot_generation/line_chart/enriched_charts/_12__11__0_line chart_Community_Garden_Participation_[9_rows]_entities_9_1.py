
import matplotlib.pyplot as plt

# Data
days = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", 
        "Day 7", "Day 8", "Day 9", "Day 10", "Day 11", "Day 12", 
        "Day 13", "Day 14", "Day 15", "Day 16", "Day 17", "Day 18", 
        "Day 19", "Day 20", "Day 21", "Day 22", "Day 23", "Day 24", 
        "Day 25", "Day 26", "Day 27", "Day 28", "Day 29", "Day 30"]
exercise_hours = [1.2, 1.4, 1.5, 1.3, 1.6, 1.8, 2.0, 2.1, 2.3, 2.2, 
                  2.5, 2.6, 2.8, 3.0, 3.2, 3.1, 3.3, 3.4, 3.6, 3.7, 
                  3.9, 4.0, 4.1, 4.2, 4.3, 4.5, 4.6, 4.8, 4.9, 5.0]

plt.figure(figsize=(16, 8))
plt.plot(days, exercise_hours, marker='o', color='#4CAF50', linewidth=2)

plt.annotate('Start of Exercise', xy=(0, 1.2), xytext=(2, 0.8),
             arrowprops=dict(facecolor='#FF5733', shrink=0.05))
plt.annotate('Peak Exercise', xy=(29, 5.0), xytext=(27, 5.2),
             arrowprops=dict(facecolor='#3498db', shrink=0.05))

plt.title('Daily Exercise Hours Over a Month')
plt.xlabel('Day')
plt.ylabel('Exercise Hours')
plt.grid(True)

plt.show()