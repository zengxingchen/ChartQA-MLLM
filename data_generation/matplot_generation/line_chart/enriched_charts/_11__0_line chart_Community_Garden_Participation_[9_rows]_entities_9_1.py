
import matplotlib.pyplot as plt

# Data
days = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", 
        "Day 7", "Day 8", "Day 9", "Day 10", "Day 11", "Day 12", 
        "Day 13", "Day 14", "Day 15", "Day 16", "Day 17", "Day 18", 
        "Day 19", "Day 20", "Day 21", "Day 22", "Day 23", "Day 24", 
        "Day 25", "Day 26", "Day 27", "Day 28", "Day 29", "Day 30"]
active_users = [150, 160, 170, 165, 180, 200, 220, 230, 240, 250, 
                245, 255, 265, 270, 280, 290, 300, 310, 320, 330, 
                340, 350, 355, 360, 370, 380, 390, 400, 410, 420]

plt.figure(figsize=(14, 7))
plt.plot(days, active_users, marker='o', color='#FF5733', linewidth=2)

plt.annotate('Lowest Activity', xy=(0, 150), xytext=(1, 140),
             arrowprops=dict(facecolor='#3498db', shrink=0.05))
plt.annotate('Highest Activity', xy=(29, 420), xytext=(28, 430),
             arrowprops=dict(facecolor='#9b59b6', shrink=0.05))

plt.title('Daily Active Users Over a Month')
plt.xlabel('Day')
plt.ylabel('Active Users')
plt.grid(True)

plt.show()