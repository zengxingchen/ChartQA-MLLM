
import matplotlib.pyplot as plt

# Data
days = [str(day) for day in range(1, 32)]
visitors = [120, 135, 150, 145, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275, 280, 285]

# Creating the figure and specifying figure size
plt.figure(figsize=(14, 8))

# Creating the bar chart as a vertical chart
plt.bar(days, visitors, width=0.6, color=['#004c6d', '#005a73', '#00677a', '#007481', '#008188', '#008f8f', '#009c96', '#00a99c', '#00b6a3', '#00c3aa', '#00d0b1', '#00ddb7', '#00eabe', '#00f7c5', '#00ffcc', '#1fffcf', '#3ffff2', '#5ffff5', '#7ffff8', '#9ffffb', '#bffffe', '#dfffff', '#ffccff', '#ffb8ff', '#ffa3ff', '#ff8eff', '#ff79ff', '#ff64ff', '#ff50ff', '#ff3bff', '#ff26ff'])

# Adding labels and title
plt.ylabel('Number of Visitors')
plt.xlabel('Day of the Month')
plt.title('Daily Visitors to Museum Y - October 2023')

# Show the plot
plt.show()