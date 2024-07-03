
import matplotlib.pyplot as plt

# Data points
age_groups = [
    '0-9', '10-19', '20-29', '30-39', '40-49',
    '50-59', '60-69', '70-79', '80+'
]

percentage = [
    10.0, 15.0, 20.0, 18.0, 12.0,
    10.0, 8.0, 5.0, 2.0
]

# Colors for each section
colors = [
    '#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0',
    '#ffb3e6', '#c4e17f', '#76d7c4', '#ffdf7e'
]

# Resize the chart
plt.figure(figsize=(10, 7))

# Create the pie chart
plt.pie(percentage, labels=age_groups, colors=colors, autopct='%1.1f%%', startangle=140)

# Set the title
plt.title('Population Distribution by Age Group in 2023', fontsize=14, pad=20)

# Display the chart
plt.show()