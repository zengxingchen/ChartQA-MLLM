
import matplotlib.pyplot as plt

# Data
days = [str(day) for day in range(1, 32)]
temperatures = [16.0, 16.5, 17.0, 16.2, 17.5, 18.0, 18.3, 17.8, 16.9, 17.6, 18.1, 17.7, 16.4,
                18.8, 19.0, 19.5, 20.0, 19.8, 18.5, 17.9, 18.2, 18.6, 19.2, 19.7, 20.1, 20.3,
                20.5, 20.8, 19.1, 18.7, 17.9]

# Creating the figure and specifying figure size
plt.figure(figsize=(14, 8))

# Creating the bar chart as a vertical chart
plt.bar(days, temperatures, width=0.6, color=['#1f77b4', '#ffbb78', '#2ca02c', '#d62728',
                                              '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
                                              '#bcbd22', '#17becf', '#1f77b4', '#ffbb78',
                                              '#2ca02c', '#d62728', '#9467bd', '#8c564b',
                                              '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
                                              '#1f77b4', '#ffbb78', '#2ca02c', '#d62728',
                                              '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
                                              '#bcbd22', '#17becf', '#1f77b4'])

# Adding labels and title
plt.ylabel('Average Daily Temperature (°C)')
plt.xlabel('Day of the Month')
plt.title('Average Daily Temperatures for City X - October 2023')

# Show the plot
plt.show()