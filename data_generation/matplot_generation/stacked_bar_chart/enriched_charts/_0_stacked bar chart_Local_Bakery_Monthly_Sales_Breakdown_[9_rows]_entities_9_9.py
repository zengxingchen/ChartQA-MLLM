
import matplotlib.pyplot as plt

# Data
years = ['2018', '2019', '2020', '2021', '2022']
product_a_sales = [450, 470, 480, 500, 520]
product_b_sales = [300, 320, 340, 360, 380]

# Colors
colors_a = ['#FF5733', '#FFC300', '#FFFD71', '#DAF7A6', '#33FFCE']
colors_b = ['#1F618D', '#34495E', '#5DADE2', '#76D7C4', '#1ABC9C']

# Plot
fig, ax = plt.subplots(figsize=(10, 8))  # Change width and height of the chart

bar_width = 0.75  # Change band width for bars

# Creating a horizontal stacked bar chart
bars_a = plt.barh(years, product_a_sales, color=colors_a, edgecolor='white', height=bar_width)
bars_b = plt.barh(years, product_b_sales, left=product_a_sales, color=colors_b, edgecolor='white', height=bar_width)

# Adding labels and title
plt.xlabel('Sales')
plt.title('Annual Sales Comparison between Product A and Product B')

# Customizing the axes
plt.xlim(0, 1000)  # Adjust the x-axis limit to accommodate the stack

# Display the plot
plt.show()