
import matplotlib.pyplot as plt

# Data
quarters = ['2019-Q1', '2019-Q2', '2019-Q3', '2019-Q4', '2020-Q1', '2020-Q2', '2020-Q3', '2020-Q4']
revenue = [20, 25, 22, 30, 32, 38, 35, 45]

# Plotting the line chart
plt.figure(figsize=(10, 5))  # Change width and height
plt.plot(quarters, revenue, color='#ff5733', marker='o')  # Specific color codes and marker style

# Annotate a specific point with the label
plt.annotate('Highest Revenue', xy=('2020-Q4', 45), xytext=('2020-Q3', 40),
             arrowprops=dict(facecolor='#000000', shrink=0.05))

# Adding a title and labels
plt.title('Quarterly Revenue for XYZ Corp')  # Change the topic/headline
plt.xlabel('Quarter')
plt.ylabel('Revenue (in millions)')

# Show the plot
plt.show()