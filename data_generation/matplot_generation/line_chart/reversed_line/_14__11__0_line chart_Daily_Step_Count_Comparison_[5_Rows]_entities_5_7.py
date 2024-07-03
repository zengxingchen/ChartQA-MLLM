
import matplotlib.pyplot as plt

# Data
dates = ['2019-Q1', '2019-Q2', '2019-Q3', '2019-Q4', '2020-Q1', '2020-Q2', '2020-Q3', '2020-Q4', 
         '2021-Q1', '2021-Q2', '2021-Q3', '2021-Q4', '2022-Q1', '2022-Q2', '2022-Q3', '2022-Q4']
adoption_rate = [85, 80, 78, 75, 70, 65, 60, 55, 50, 42, 40, 35, 30, 25, 20, 15]

# Plotting the line chart
plt.figure(figsize=(10, 8))  # Change width and height
plt.plot(dates, adoption_rate, color='#FF5733', marker='s')  # Specific color codes and marker style

# Annotate a specific point with the label
plt.annotate('Lowest Point', xy=('2022-Q4', 15), xytext=('2021-Q4', 30),
             arrowprops=dict(facecolor='#2ECC71', shrink=0.05))

# Adding a title and labels
plt.title('Health & Psychology: Stress Level Over Time')  # Change the topic/headline
plt.xlabel('Date')
plt.ylabel('Stress Level (%)')
plt.gca().invert_yaxis()  # Invert y-axis

# Show the plot
plt.show()