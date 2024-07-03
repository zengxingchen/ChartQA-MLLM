
import matplotlib.pyplot as plt

# Monthly visitor data for a museum
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
visitors = [300, 350, 400, 380, 420, 460, 500, 520, 480, 450, 430, 470]

# Color scheme using specific color codes for each month
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#FF8F33',
    '#33FFF6', '#FF33F4', '#A6FF33', '#33D4FF', '#FF3333',
    '#57FF33', '#5733FF'
]

# Create horizontal bar chart
plt.figure(figsize=(10, 8))  # Width and height of the chart
plt.barh(months, visitors, color=colors, height=0.6)  # Bar color and band height

# Set the title and labels
plt.title('Monthly Museum Visitors', pad=20)
plt.xlabel('Number of Visitors')
plt.ylabel('Month')

# Display the bar chart
plt.show()