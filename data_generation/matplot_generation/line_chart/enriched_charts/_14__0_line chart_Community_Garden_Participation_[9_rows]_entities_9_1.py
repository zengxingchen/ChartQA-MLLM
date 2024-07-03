
import matplotlib.pyplot as plt

# Data
months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]
visitors = [1200, 1500, 1800, 2200, 2600, 3000, 3300, 3200, 2800, 2400, 2000, 1700]

plt.figure(figsize=(14, 7))
plt.plot(months, visitors, marker='s', color='#4CAF50', linewidth=3)

# Adding annotations for peak and lowest visitors months
plt.annotate('Lowest Visitors', xy=(0, 1200), xytext=(2, 1400),
             arrowprops=dict(facecolor='#E74C3C', shrink=0.05))
plt.annotate('Peak Visitors', xy=(6, 3300), xytext=(7, 3500),
             arrowprops=dict(facecolor='#3498DB', shrink=0.05))

plt.title('Monthly Visitors to the Museum', fontsize=14)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Number of Visitors', fontsize=12)
plt.grid(True)
plt.gca().invert_yaxis()  # Inverting the y-axis

plt.show()