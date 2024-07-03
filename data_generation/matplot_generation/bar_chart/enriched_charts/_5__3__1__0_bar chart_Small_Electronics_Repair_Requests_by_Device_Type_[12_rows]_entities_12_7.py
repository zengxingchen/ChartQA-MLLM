
import matplotlib.pyplot as plt

# Data
days = [str(day) for day in range(1, 31)]
temperatures = [72, 75, 70, 77, 74, 73, 76, 78, 75, 79, 80, 82, 83, 85, 87, 88, 86, 84, 81, 80, 79, 77, 76, 75, 74, 73, 72, 71, 70, 69]

# Creating the figure and specifying figure size
plt.figure(figsize=(10, 8))

# Creating the bar chart as a vertical chart
plt.bar(days, temperatures, width=0.6, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
                                              '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
                                              '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
                                              '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
                                              '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
                                              '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#1f77b4'])

# Setting the y-axis limits to truncate the view
plt.ylim(68, 90)

# Adding labels and title
plt.xlabel('Day of the Month')
plt.ylabel('Temperature (°F)')
plt.title('Daily Temperature Fluctuations - June 2024')

# Show the plot
plt.show()