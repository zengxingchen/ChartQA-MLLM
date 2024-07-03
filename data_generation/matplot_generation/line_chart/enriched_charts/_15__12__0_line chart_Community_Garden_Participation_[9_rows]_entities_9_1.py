
import matplotlib.pyplot as plt

# Data
months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]
happiness_score = [75, 85, 90, 70, 60, 55, 50, 45, 60, 65, 70, 80]

plt.figure(figsize=(12, 6))  # Changing width and height of the chart
plt.plot(months, happiness_score, marker='s', color='#1E90FF', linewidth=2)  # Modified color scheme

# Adding annotations for the highest and lowest happiness scores
plt.annotate('Lowest Happiness', xy=(7, 45), xytext=(8, 50),
             arrowprops=dict(facecolor='#FF1493', shrink=0.05))
plt.annotate('Highest Happiness', xy=(2, 90), xytext=(3, 95),
             arrowprops=dict(facecolor='#00FA9A', shrink=0.05))

plt.title('Monthly Happiness Scores in a Community', pad=20)  # New headline fitting the topic
plt.xlabel('Month')  # Changing labels to fit the new data type
plt.ylabel('Happiness Score')
plt.grid(True)
plt.gca().invert_yaxis()  # Invert the y-axis to make higher values lower

plt.show()