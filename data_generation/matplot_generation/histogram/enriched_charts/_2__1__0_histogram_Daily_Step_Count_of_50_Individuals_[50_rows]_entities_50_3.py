import matplotlib.pyplot as plt

time_spent = [
    32, 45, 54, 60, 70, 85, 120, 130, 150, 45, 60, 75, 90, 110, 100, 55, 65, 40, 50, 75,
    85, 95, 105, 115, 80, 90, 100, 110, 120, 130, 140, 75, 85, 95, 105, 115, 125, 135, 70, 
    80, 90, 100, 110, 120, 130, 140, 150
]

plt.figure(figsize=(12, 8))

plt.hist(time_spent, bins=10, color='#3498db', edgecolor='#2c3e50', linewidth=1.2, orientation='horizontal')

plt.title('Time Spent on Online Learning Platforms', pad=20)
plt.xlabel('Number of Students')
plt.ylabel('Time Spent (minutes)')

plt.show()