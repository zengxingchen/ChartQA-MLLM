
import matplotlib.pyplot as plt

# Data points for advertising budget (in thousands) vs sales (in millions)
advertising_spending = [10, 20, 25, 30, 35, 40, 50, 60, 75, 80, 90, 100, 110, 125]
sales_revenue = [1, 1.9, 2.2, 2.6, 2.9, 3.3, 4.0, 4.5, 5.5, 5.9, 6.3, 6.8, 7.2, 8.0]

# Creating the scatter plot
plt.figure(figsize=(12, 6))  # modify width and height of the chart
plt.scatter(advertising_spending, sales_revenue, color='#FF5733')  # Change to an RGB color code

# Adding chart labels and title
plt.title('Impact of Advertising on Sales Revenue')
plt.xlabel('Advertising Spending (Thousands of $)')
plt.ylabel('Sales Revenue (Millions of $)')

# Show the figure
plt.show()