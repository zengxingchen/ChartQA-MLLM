
import matplotlib.pyplot as plt

# Data
dates = ['2019-Q1', '2019-Q2', '2019-Q3', '2019-Q4', '2020-Q1', '2020-Q2', '2020-Q3', '2020-Q4', 
         '2021-Q1', '2021-Q2', '2021-Q3', '2021-Q4', '2022-Q1', '2022-Q2', '2022-Q3', '2022-Q4']
average_temperature = [85, 82, 80, 78, 75, 70, 68, 65, 63, 60, 58, 55, 52, 50, 48, 45]

# Plotting the line chart
plt.figure(figsize=(10, 5))  # Change width and height
plt.plot(dates, average_temperature, color='#ff5733', marker='s')  # Specific color codes and marker style

# Annotate a specific point with the label
plt.annotate('Lowest Temperature', xy=('2022-Q4', 45), xytext=('2021-Q3', 58),
             arrowprops=dict(facecolor='#2ca02c', shrink=0.05))

# Adding a title and labels
plt.title('Average Temperature Over Time (Inverted Y-Axis)')
plt.xlabel('Date')
plt.ylabel('Average Temperature (°F)')
plt.gca().invert_yaxis()  # Invert the y-axis

# Show the plot
plt.show()