
import matplotlib.pyplot as plt

# Data
weeks = list(range(1, 41))
adventures = [30, 45, 50, 60, 70, 65, 80, 90, 85, 95, 100, 110, 105, 115, 120, 130, 135, 140, 150, 155, 160, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260]
preparation_hours = [3, 4.2, 4.5, 4.8, 5.1, 5.3, 5.6, 5.8, 6, 6.2, 6.5, 6.7, 6.9, 7, 7.2, 7.4, 7.6, 7.8, 8, 8.2, 8.4, 8.6, 8.8, 9, 9.2, 9.4, 9.6, 9.8, 10, 10.2, 10.4, 10.6, 10.8, 11, 11.2, 11.4, 11.6, 11.8, 12, 12.2]

# Scatter plot
plt.figure(figsize=(16, 9))
plt.scatter(weeks, adventures, color='#FF5733', label='Adventures')  # Orange
plt.scatter(weeks, preparation_hours, color='#3498DB', label='Preparation Hours')  # Blue

# Customize the plot
plt.title('Weekly Adventures and Preparation Hours Over 40 Weeks', pad=20)
plt.xlabel('Week')
plt.ylabel('Count')
plt.legend(loc='upper left')
plt.grid(True)

# Show the plot
plt.show()