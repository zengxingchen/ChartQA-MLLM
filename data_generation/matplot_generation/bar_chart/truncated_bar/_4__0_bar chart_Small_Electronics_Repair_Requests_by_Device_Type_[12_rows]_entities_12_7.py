
import matplotlib.pyplot as plt

# Data
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
sales = [500, 520, 480, 550, 600, 610, 620, 640, 630, 590, 580, 600]

# Creating the figure and specifying figure size
plt.figure(figsize=(12, 8))

# Creating the bar chart as a vertical chart with modified width of bars
plt.bar(months, sales, width=0.5, color=['#FF6347', '#FFD700', '#8A2BE2', '#00FF7F',
                                         '#DC143C', '#00CED1', '#9400D3', '#FF4500',
                                         '#2E8B57', '#FFA500', '#4682B4', '#FF1493'])

# Setting y-axis limits to start from a specific value other than zero
plt.ylim(450, 650)

# Adding labels and title
plt.ylabel('Monthly Sales (in Units)')
plt.xlabel('Month')
plt.title('Monthly Sales Data for Company Y - 2023')

# Show the plot
plt.show()