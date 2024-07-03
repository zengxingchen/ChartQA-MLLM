
import matplotlib.pyplot as plt

# Data to plot
categories = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
amounts = [800, 950, 1200, 1100, 1000, 1050, 1400, 1350, 1300, 1250, 1150, 900]

# Plot a vertical bar chart
plt.figure(figsize=(12, 10))  # Width and height of the chart
plt.bar(x=categories, height=amounts, color=[
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', 
    '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', 
    '#bcbd22', '#17becf', '#e7969c', '#f7b6d2'], 
    width=0.6)  # Bar width

# Set the title and labels
plt.title('Monthly Expenditure on Travel in 2023', fontsize=18, pad=20)
plt.ylabel('Amount (in USD)', fontsize=14)
plt.xlabel('Month', fontsize=14)

# Set y-axis limits to truncate the chart
plt.ylim(800, 1500)

# Display the chart
plt.tight_layout()  # Adjust the padding between and around subplots.
plt.show()