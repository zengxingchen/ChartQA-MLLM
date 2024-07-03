
import matplotlib.pyplot as plt

# Data
quarters = ['2019-Q1', '2019-Q2', '2019-Q3', '2019-Q4', '2020-Q1', '2020-Q2', '2020-Q3', '2020-Q4']
revenue = [50, 48, 45, 43, 41, 38, 36, 33]

# Plotting the line chart
plt.figure(figsize=(12, 6))  # Change width and height
plt.plot(quarters, revenue, color='#1f77b4', marker='s')  # Specific color codes and marker style

# Annotate a specific point with the label
plt.annotate('Lowest Revenue', xy=('2020-Q4', 33), xytext=('2020-Q3', 37),
             arrowprops=dict(facecolor='#ff5733', shrink=0.05))

# Adding a title and labels
plt.title('Quarterly Revenue Decrease for XYZ Corp', pad=20)  # Change the topic/headline
plt.xlabel('Quarter')
plt.ylabel('Revenue (in millions)')

# Show the plot
plt.gca().invert_yaxis()  # Inverse the y-axis
plt.show()