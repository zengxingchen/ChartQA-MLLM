
import matplotlib.pyplot as plt

# Data
dates = ['2019-Q1', '2019-Q2', '2019-Q3', '2019-Q4', '2020-Q1', '2020-Q2', '2020-Q3', '2020-Q4', 
         '2021-Q1', '2021-Q2', '2021-Q3', '2021-Q4', '2022-Q1', '2022-Q2', '2022-Q3', '2022-Q4']
value = [40, 45, 50, 48, 52, 55, 58, 60, 65, 63, 68, 70, 75, 78, 80, 85]

# Plotting the line chart
plt.figure(figsize=(16, 8))  # Change width and height
plt.plot(dates, value, color='#1f77b4', marker='o')  # Specific color codes and marker style

# Annotate a specific point with the label
plt.annotate('Highest Point', xy=('2022-Q4', 85), xytext=('2021-Q3', 75),
             arrowprops=dict(facecolor='#d62728', shrink=0.05))

# Adding a title and labels
plt.title('Trends in Renewable Energy Investment Over Time')  # Change the topic/headline
plt.xlabel('Date')
plt.ylabel('Investment Value (in billions $)')
plt.gca().invert_yaxis()  # Invert y-axis

# Show the plot
plt.show()