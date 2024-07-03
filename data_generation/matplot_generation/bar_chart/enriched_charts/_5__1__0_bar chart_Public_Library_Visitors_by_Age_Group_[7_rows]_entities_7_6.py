
import matplotlib.pyplot as plt

# Data
months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]
population_growth_rate = [1.2, 1.5, 1.8, 2.1, 2.3, 2.6, 2.9, 3.0, 2.7, 2.4, 1.9, 1.6]

# Creating horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 8))

ax.barh(months, population_growth_rate, color=[
    '#FF5733', '#FF8D1A', '#FFC300', '#DAF7A6',
    '#33FF57', '#1AFF8D', '#1AD7FF', '#3357FF',
    '#8D33FF', '#C300FF', '#FF33A1', '#FF3357'
], height=0.5)  # Change bar color and height

# Setting y-axis limit
ax.set_xlim(1, 3.5)  # Truncate y-axis to start from 1

# Adding labels and title
ax.set_xlabel('Population Growth Rate (%)')
ax.set_title('Monthly Population Growth Rate in a Fictional City', pad=20)

# Show the plot
plt.show()