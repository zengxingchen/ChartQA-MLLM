
import matplotlib.pyplot as plt

# Data
months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]
visitor_count = [120, 200, 340, 450, 620, 800, 980, 1100, 950, 700, 450, 250]

plt.figure(figsize=(14, 7))  # Changing width and height of the chart
plt.plot(months, visitor_count, marker='o', color='#2E8B57', linewidth=2)  # Modified color scheme

# Adding annotations for the highest and lowest visitor counts
plt.annotate('Lowest Visitors', xy=(0, 120), xytext=(1, 150),
             arrowprops=dict(facecolor='#FF6347', shrink=0.05))
plt.annotate('Highest Visitors', xy=(7, 1100), xytext=(6, 1150),
             arrowprops=dict(facecolor='#4682B4', shrink=0.05))

plt.title('Monthly Visitor Count in a National Park')  # New headline which fits the topic
plt.xlabel('Month')  # Changing labels to fit the new data type
plt.ylabel('Visitor Count')
plt.grid(True)

plt.show()