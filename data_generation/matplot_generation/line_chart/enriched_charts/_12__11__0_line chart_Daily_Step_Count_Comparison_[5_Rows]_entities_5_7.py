
import matplotlib.pyplot as plt

# Data
dates = ['2019-Q1', '2019-Q2', '2019-Q3', '2019-Q4', '2020-Q1', '2020-Q2', '2020-Q3', '2020-Q4', 
         '2021-Q1', '2021-Q2', '2021-Q3', '2021-Q4', '2022-Q1', '2022-Q2', '2022-Q3', '2022-Q4']
value = [45, 50, 55, 60, 65, 55, 50, 60, 70, 75, 80, 85, 90, 85, 80, 75]

# Plotting the line chart
plt.figure(figsize=(14, 7))  # Change width and height
plt.plot(dates, value, color='#ff7f0e', marker='s')  # Specific color codes and marker style

# Annotate a specific point with the label
plt.annotate('Highest Point', xy=('2022-Q1', 90), xytext=('2021-Q2', 80),
             arrowprops=dict(facecolor='#2ca02c', shrink=0.05))

# Adding a title and labels
plt.title('Trends in Consumer Spending Over Time')  # Change the topic/headline
plt.xlabel('Date')
plt.ylabel('Spending Value ($)')

# Show the plot
plt.show()