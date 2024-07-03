
import matplotlib.pyplot as plt

# Data
years_quarters = ['2019-Q1', '2019-Q2', '2019-Q3', '2019-Q4', '2020-Q1', '2020-Q2', '2020-Q3', '2020-Q4', 
                  '2021-Q1', '2021-Q2', '2021-Q3', '2021-Q4', '2022-Q1', '2022-Q2', '2022-Q3', '2022-Q4']
revenue = [20, 25, 22, 30, 32, 28, 35, 45, 48, 50, 55, 60, 58, 62, 66, 70]

# Plotting the line chart
plt.figure(figsize=(12, 6))  # Change width and height
plt.plot(years_quarters, revenue, color='#1f77b4', marker='o')  # Specific color codes and marker style

# Annotate a specific point with the label
plt.annotate('Peak Revenue', xy=('2022-Q4', 70), xytext=('2022-Q2', 60),
             arrowprops=dict(facecolor='#d62728', shrink=0.05))

# Adding a title and labels
plt.title('Quarterly Revenue for XYZ Corp', fontsize=14)  # Change the topic/headline
plt.xlabel('Quarter')
plt.ylabel('Revenue (in millions)')

# Show the plot
plt.show()