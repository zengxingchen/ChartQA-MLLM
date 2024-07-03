
import matplotlib.pyplot as plt

# Data
dates = ['2019-Q1', '2019-Q2', '2019-Q3', '2019-Q4', '2020-Q1', '2020-Q2', '2020-Q3', '2020-Q4', 
         '2021-Q1', '2021-Q2', '2021-Q3', '2021-Q4', '2022-Q1', '2022-Q2', '2022-Q3', '2022-Q4']
adoption_rate = [15, 18, 22, 30, 35, 40, 42, 50, 55, 60, 65, 70, 75, 78, 80, 85]

# Plotting the line chart
plt.figure(figsize=(12, 6))  # Change width and height
plt.plot(dates, adoption_rate, color='#1f77b4', marker='o')  # Specific color codes and marker style

# Annotate a specific point with the label
plt.annotate('Peak Adoption', xy=('2022-Q4', 85), xytext=('2021-Q4', 75),
             arrowprops=dict(facecolor='#d62728', shrink=0.05))

# Adding a title and labels
plt.title('Technology Adoption Rate Over Time')  # Change the topic/headline
plt.xlabel('Date')
plt.ylabel('Adoption Rate (%)')

# Show the plot
plt.show()