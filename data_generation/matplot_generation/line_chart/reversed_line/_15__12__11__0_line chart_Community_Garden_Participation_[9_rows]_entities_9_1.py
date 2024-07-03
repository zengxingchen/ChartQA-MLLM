
import matplotlib.pyplot as plt

# Data
days = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", 
        "Day 7", "Day 8", "Day 9", "Day 10", "Day 11", "Day 12", 
        "Day 13", "Day 14", "Day 15", "Day 16", "Day 17", "Day 18", 
        "Day 19", "Day 20", "Day 21", "Day 22", "Day 23", "Day 24", 
        "Day 25", "Day 26", "Day 27", "Day 28", "Day 29", "Day 30"]
reading_hours = [5.0, 4.8, 4.7, 4.5, 4.3, 4.1, 4.0, 3.9, 3.7, 3.5, 
                 3.4, 3.2, 3.0, 2.8, 2.7, 2.5, 2.3, 2.1, 2.0, 1.9, 
                 1.7, 1.5, 1.4, 1.2, 1.0, 0.8, 0.7, 0.5, 0.3, 0.2]

plt.figure(figsize=(14, 7))
plt.plot(days, reading_hours, marker='o', color='#FF5733', linewidth=2)

plt.annotate('Start of Reading', xy=(0, 5.0), xytext=(2, 5.2),
             arrowprops=dict(facecolor='#3498db', shrink=0.05))
plt.annotate('Lowest Reading Time', xy=(29, 0.2), xytext=(27, 0.5),
             arrowprops=dict(facecolor='#4CAF50', shrink=0.05))

plt.title('Daily Reading Time Over a Month')
plt.xlabel('Day')
plt.ylabel('Reading Time (hours)')
plt.grid(True)
plt.gca().invert_yaxis()

plt.show()