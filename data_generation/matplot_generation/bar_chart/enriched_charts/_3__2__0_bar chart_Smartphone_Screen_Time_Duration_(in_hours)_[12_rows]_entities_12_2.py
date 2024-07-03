
import matplotlib.pyplot as plt

# Data to plot
categories = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
amounts = [300, 450, 600, 700, 850, 950, 1200, 1100, 1000, 900, 650, 500]

# Plot a horizontal bar chart
plt.figure(figsize=(14, 8))  # Width and height of the chart
plt.barh(y=categories, width=amounts, color=[
    '#4daf4a', '#377eb8', '#ff7f00', '#984ea3', 
    '#e41a1c', '#f781bf', '#a65628', '#999999', 
    '#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3'], 
    height=0.7)  # Band height of the bars

# Set the title and labels
plt.title('Monthly Expenditure on Food in 2023', fontsize=18, pad=20)
plt.xlabel('Amount (in USD)', fontsize=14)
plt.ylabel('Month', fontsize=14)

# Display the chart
plt.tight_layout()  # Adjust the padding between and around subplots.
plt.show()