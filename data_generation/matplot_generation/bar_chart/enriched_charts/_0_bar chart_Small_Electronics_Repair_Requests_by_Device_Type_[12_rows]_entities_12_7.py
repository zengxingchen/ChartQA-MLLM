
import matplotlib.pyplot as plt

# Data
days = [str(day) for day in range(1, 32)]
temperatures = [16, 16.5, 17, 16.2, 17.5, 18, 18.3, 17.8, 16.9, 17.6, 18.1, 17.7, 16.4,
                18.8, 19, 19.5, 20, 19.8, 18.5, 17.9, 18.2, 18.6, 19.2, 19.7, 20.1, 20.3,
                20.5, 20.8, 19.1, 18.7, 17.9]

# Creating the figure and specifying figure size
plt.figure(figsize=(10, 12))

# Creating the bar chart as a horizontal chart
plt.barh(days, temperatures, height=0.7, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
                                                 '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
                                                 '#bcbd22', '#17becf', '#1f77b4', '#ff7f0e',
                                                 '#2ca02c', '#d62728', '#9467bd', '#8c564b',
                                                 '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
                                                 '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
                                                 '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
                                                 '#bcbd22', '#17becf', '#1f77b4'])

# Adding labels and title
plt.xlabel('Average Daily Temperature (°C)')
plt.ylabel('Day of the Month')
plt.title('Average Daily Temperatures for City X - October 2023')

# Show the plot
plt.show()