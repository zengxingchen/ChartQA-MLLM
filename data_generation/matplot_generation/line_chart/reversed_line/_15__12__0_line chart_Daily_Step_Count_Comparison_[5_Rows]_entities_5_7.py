
import matplotlib.pyplot as plt

# Data
years_quarters = ['2019-Q1', '2019-Q2', '2019-Q3', '2019-Q4', '2020-Q1', '2020-Q2', '2020-Q3', '2020-Q4', 
                  '2021-Q1', '2021-Q2', '2021-Q3', '2021-Q4', '2022-Q1', '2022-Q2', '2022-Q3', '2022-Q4']
revenue = [70, 68, 66, 63, 60, 57, 55, 52, 50, 48, 45, 43, 40, 38, 35, 32]

# Plotting the line chart
plt.figure(figsize=(10, 8))  # Change width and height
plt.plot(years_quarters, revenue, color='#FF5733', marker='s')  # Specific color codes and marker style

# Annotate a specific point with the label
plt.annotate('Revenue Drop', xy=('2022-Q4', 32), xytext=('2021-Q2', 50),
             arrowprops=dict(facecolor='#900C3F', shrink=0.05))

# Adding a title and labels
plt.title('Quarterly Revenue for XYZ Corp - Downward Trend', fontsize=16, loc='left')  # Change the topic/headline
plt.xlabel('Quarter')
plt.ylabel('Revenue (in millions)')

# Invert the y-axis
plt.gca().invert_yaxis()

# Show the plot
plt.show()