
import matplotlib.pyplot as plt

# Data
months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]
average_spending = [200, 180, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400]

# Creating horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 8))  # Change the width and height of the chart

ax.barh(months, average_spending, color=[
    '#FF5733', '#FF8D1A', '#FFC300', '#DAF7A6',
    '#33FF57', '#1AFF8D', '#00FFC3', '#33D7FF',
    '#1A8DFF', '#5733FF', '#8D1AFF', '#C300FF'
], height=0.5)  # Change bar color and width

# Adding labels and title
ax.set_xlabel('Average Spending (in USD)')
ax.set_title('Average Monthly Spending in a Year', pad=20)

# Show the plot
plt.show()