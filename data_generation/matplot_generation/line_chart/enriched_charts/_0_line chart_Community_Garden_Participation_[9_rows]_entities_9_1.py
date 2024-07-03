
import matplotlib.pyplot as plt

# Data
months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]
temperatures = [5, 7, 10, 15, 20, 25, 28, 27, 22, 17, 10, 6]

plt.figure(figsize=(12, 6))  # Changing width and height of the chart
plt.plot(months, temperatures, marker='o', color='#FF5733', linewidth=2)  # Modified color scheme

# Adding annotations for the hottest and coldest months
plt.annotate('Coldest Month', xy=(0, 5), xytext=(1, 5),
             arrowprops=dict(facecolor='#3498db', shrink=0.05))
plt.annotate('Hottest Month', xy=(6, 28), xytext=(5, 29),
             arrowprops=dict(facecolor='#9b59b6', shrink=0.05))

plt.title('Average Monthly Temperature')  # New headline which fits the topic
plt.xlabel('Month')  # Changing labels to fit the new data type
plt.ylabel('Temperature (°C)')
plt.grid(True)

plt.show()