
import matplotlib.pyplot as plt

# Data points
periods = ['Iron Age', 'Classical Antiquity', 'Middle Ages', 'Renaissance', 'Industrial Revolution', 'Modern Era', 'Postmodern Era', 'Information Age']
amounts = [200, 300, 150, 250, 350, 400, 280, 320]

# Colors for each bar
colors = ['#FF5733', '#33BEFF', '#FFC733', '#33FF57', '#8E33FF', '#FF3380', '#33FFF6', '#FFAB33']

# Create a vertical bar chart
plt.figure(figsize=(12, 7))
plt.bar(periods, amounts, color=colors, width=0.5)

# Modify the ticks, labels, and title
plt.ylabel('Amount (in million units)')
plt.title('Historical Periods and Their Contributions to Human Development', pad=20)
plt.ylim(0, 450)

# Display the plot
plt.show()